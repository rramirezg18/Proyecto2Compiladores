#A partir del AST genera el codigo intermedio utilizando llvmlite

from llvmlite import ir
from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser

class GeneradorCodigo(GramaticaVisitor):
    def __init__(self, tabla_simbolos):
        self.module = ir.Module(name="main")
        self.module = ir.Module(name="main")
        self.module.triple = "x86_64-pc-linux-gnu"  # unicamente valido para linux


        self.builder = None
        self.ts = tabla_simbolos
        self.funciones = {}
        self.locals = {}
        self.declarar_funciones_builtin()

        # Mapeo de tipos
        self.type_map = {
            'int': ir.IntType(32),
            'float': ir.DoubleType(),
            'boolean': ir.IntType(1),
            'string': ir.IntType(8).as_pointer()
        }

    def declarar_funciones_builtin(self):
        # Declarar printf
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        ir.Function(self.module, printf_ty, name="printf")

    #Métodos principales
    def visitGramatica(self, ctx: GramaticaParser.GramaticaContext):
        #Registrar prototipos de funciones para todas las funciones definidas
        for funcion in ctx.funcion():
            self.registrar_prototipo_funcion(funcion)
        
        #Procesar el bloque main
        self.visit(ctx.main())
        
        #Procesar el cuerpo de cada función
        for funcion in ctx.funcion():
            self.visit(funcion)
        
        return self.module

    def registrar_prototipo_funcion(self, ctx: GramaticaParser.FuncionContext):
        func_name = ctx.VARIABLE().getText()
        func_info = self.ts.consultar_funcion(func_name)
        ret_type = self.type_map[func_info['tipo_retorno']]
        param_types = [self.type_map[t] for t, _ in func_info['parametros']]
        func_type = ir.FunctionType(ret_type, param_types)
        
        #prototipo en el módulo LLVM y registrar en self.funciones
        function = ir.Function(self.module, func_type, name=func_name)
        self.funciones[func_name] = function


    def visitMain(self, ctx: GramaticaParser.MainContext):
        #función main en LLVM
        main_type = ir.FunctionType(ir.IntType(32), [])
        main_func = ir.Function(self.module, main_type, name="main")
        self.funciones['main'] = main_func
        
        #creabloque de entrada
        block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
        
        #procesa instrucciones del main
        for instr in ctx.instruccion():
            self.visit(instr)
        
        #retorno por defecto
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(ir.IntType(32), 0))

    #Variables y asignaciones
    def visitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        val, val_type = self.visit(ctx.expr())
        
        # obtiene el tipo de dato, si es declaracion se usa el que trae por defecto
        if ctx.tipo():
            declared_type = ctx.tipo().getText()
        else:
            if var_name in self.locals:
                #se obtiene el tipo que ya se registró en self.locals
                declared_type = self.locals[var_name][1]
            else:
                declared_type = self.ts.consultar_variable(var_name)
        
        llvm_type = self.type_map[declared_type]
        
        #se reserva espacio por si la variable no existe en un entorno local
        if var_name not in self.locals:
            alloc = self.builder.alloca(llvm_type, name=var_name)
            self.locals[var_name] = (alloc, declared_type)
        
        #conversión de tipos si es necesario
        if declared_type == 'float' and val_type == 'int':
            val = self.builder.sitofp(val, llvm_type)
        
        #almacenar el valor en la variable
        self.builder.store(val, self.locals[var_name][0])
        return (val, declared_type)

    


    def visitSentencia_print(self, ctx: GramaticaParser.Sentencia_printContext):
        #evaluar la expresión que se quiere imprimir
        value, value_type = self.visit(ctx.expr())

        # Según el tipo de la expresión, definir el formato de impresión
        if value_type == 'int':
            fmt = "%d\n\0"
        elif value_type == 'float':
            fmt = "%f\n\0"
        elif value_type == 'string':
            fmt = "%s\n\0"
        elif value_type == 'boolean':
            fmt = "%d\n\0"  #muestra 1 para true y 0 para false
        else:
            raise Exception(f"print no soporta tipo {value_type}")

        #crear una variable global para la cadena de formato
        fmt_name = "fmt_" + value_type
        if fmt_name in self.module.globals:
            fmt_global = self.module.globals[fmt_name]
        else:
            fmt_global = ir.GlobalVariable(
                self.module,
                ir.ArrayType(ir.IntType(8), len(fmt)),
                name=fmt_name
            )
            fmt_global.linkage = "internal"
            fmt_global.global_constant = True
            fmt_global.initializer = ir.Constant(
                ir.ArrayType(ir.IntType(8), len(fmt)),
                bytearray(fmt.encode("utf8"))
            )
        #obtener un puntero a la cadena de formato
        fmt_ptr = self.builder.bitcast(fmt_global, ir.IntType(8).as_pointer())

        #invocar a printf con la cadena de formato y el valor
        self.builder.call(self.module.globals["printf"], [fmt_ptr, value])


    def visitSentencia_for(self, ctx: GramaticaParser.Sentencia_forContext):
        func = self.builder.function

        #ejecuta la inicialización: declaracion_y_asignacion
        self.visit(ctx.declaracion_y_asignacion())

        #crear bloques para la condición, cuerpo, incremento y salida
        cond_bb = func.append_basic_block(name="for.cond")
        body_bb = func.append_basic_block(name="for.body")
        inc_bb = func.append_basic_block(name="for.inc")
        exit_bb = func.append_basic_block(name="for.exit")

        #se pasa  al bloque de condición
        self.builder.branch(cond_bb)

        #bloque de condición
        self.builder.position_at_start(cond_bb)
        cond_val, _ = self.visit(ctx.expr())
        self.builder.cbranch(cond_val, body_bb, exit_bb)

        #bloque del cuerpo del for
        self.builder.position_at_start(body_bb)
        self.visit(ctx.bloque())
        self.builder.branch(inc_bb)

        #bloque de incremento
        self.builder.position_at_start(inc_bb)
        self.visit(ctx.for_incremento_y_disminucion())
        self.builder.branch(cond_bb)

        #bloque de salida se posiciona al final del for
        self.builder.position_at_start(exit_bb)
        return None


    def visitFor_incremento_y_disminucion(self, ctx: GramaticaParser.For_incremento_y_disminucionContext):
        #si es post-incremento o decremento: i++ o i--
        if ctx.MASMAS() or ctx.MENOSMENOS():
            var_name = ctx.VARIABLE().getText()
            #obtener la dirección y tipo de la variable
            if var_name not in self.locals:
                raise Exception(f"Variable '{var_name}' no declarada en incremento")
            alloc, var_type = self.locals[var_name]
            current_val = self.builder.load(alloc, name=var_name)
            if ctx.MASMAS():
                #incremento
                if var_type == 'int':
                    one = ir.Constant(ir.IntType(32), 1)
                    new_val = self.builder.add(current_val, one, name=var_name+"_inc")
                elif var_type == 'float':
                    one = ir.Constant(ir.DoubleType(), 1.0)
                    new_val = self.builder.fadd(current_val, one, name=var_name+"_inc")
                else:
                    raise Exception(f"Tipo no soportado para incremento: {var_type}")
            else:
                #disminucion
                if var_type == 'int':
                    one = ir.Constant(ir.IntType(32), 1)
                    new_val = self.builder.sub(current_val, one, name=var_name+"_dec")
                elif var_type == 'float':
                    one = ir.Constant(ir.DoubleType(), 1.0)
                    new_val = self.builder.fsub(current_val, one, name=var_name+"_dec")
                else:
                    raise Exception(f"Tipo no soportado para decremento: {var_type}")
            self.builder.store(new_val, alloc)
        else:
            #si es una reasignación i = i + 2
            self.visit(ctx.declaracion_y_asignacion())
        return None


    def visitExpr(self, ctx: GramaticaParser.ExprContext):
        #print(f"\nProcesando expresión: {ctx.getText()}")
        #print(f"Tipo de contexto: {type(ctx).__name__}")
        
        #Expresiones simples 1 elemento
        if ctx.getChildCount() == 1:
            if ctx.llamada_funcion():
                return self.visit(ctx.llamada_funcion())
            
            token = ctx.getText()
            #print(f"Token simple: {token}")
            
            # Booleanos, strings, números, etc.
            if token in ['true', 'false']:
                val = 1 if token == 'true' else 0
                return (ir.Constant(ir.IntType(1), val), 'boolean')
            elif token.startswith('"'):
                str_val = token[1:-1]
                str_global = ir.GlobalVariable(
                    self.module,
                    ir.ArrayType(ir.IntType(8), len(str_val) + 1),
                    name=f"str.{hash(str_val)}"
                )
                str_global.linkage = 'internal'
                str_global.global_constant = True
                str_global.initializer = ir.Constant(
                    ir.ArrayType(ir.IntType(8), len(str_val) + 1),
                    bytearray(str_val.encode('utf-8') + b'\0')
                )
                ptr = self.builder.bitcast(str_global, ir.IntType(8).as_pointer())
                return (ptr, 'string')
            elif '.' in token:
                try:
                    float_val = float(token)
                    return (ir.Constant(ir.DoubleType(), float_val), 'float')
                except ValueError:
                    raise Exception(f"Valor float inválido: {token}")
            elif token.isdigit():
                try:
                    int_val = int(token)
                    return (ir.Constant(ir.IntType(32), int_val), 'int')
                except ValueError:
                    raise Exception(f"Valor entero inválido: {token}")
            else:
                # Manejo de variables
                #print(f"Buscando variable: {token}")
                #print(f"Variables en locals: {list(self.locals.keys())}")
                
                if token in self.locals:
                    alloc, var_type = self.locals[token]
                    loaded = self.builder.load(alloc, name=token)
                    #print(f"Variable cargada: {token} ({var_type})")
                    return (loaded, var_type)
                else:
                    try:
                        var_type = self.ts.consultar_variable(token)
                        llvm_type = self.type_map[var_type]
                        alloc = self.builder.alloca(llvm_type, name=token)
                        self.locals[token] = (alloc, var_type)
                        loaded = self.builder.load(alloc, name=token)
                        return (loaded, var_type)
                    except Exception as e:
                        #print(f"Error al buscar variable: {str(e)}")
                        raise Exception(f"Variable '{token}' no declarada")
        
        #primero verifica si es una expresión entre paréntesis
        if (ctx.getChildCount() == 3 and 
            ctx.getChild(0).getText() == '(' and 
            ctx.getChild(2).getText() == ')'):
            return self.visit(ctx.expr(0))
        
        #operaciones binarias
        elif ctx.getChildCount() == 3:
            #procesa los operandos
            left, left_type = self.visit(ctx.expr(0))
            right, right_type = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            
            #conversión de tipos si es necesario
            if left_type == 'int' and right_type == 'float':
                left = self.builder.sitofp(left, ir.DoubleType())
                left_type = 'float'
            elif left_type == 'float' and right_type == 'int':
                right = self.builder.sitofp(right, ir.DoubleType())
                right_type = 'float'
            
            #operaciones aritméticas
            if op in ['+', '-', '*', '/', '%']:
                if left_type == 'int':
                    if op == '+': val = self.builder.add(left, right)
                    elif op == '-': val = self.builder.sub(left, right)
                    elif op == '*': val = self.builder.mul(left, right)
                    elif op == '/': val = self.builder.sdiv(left, right)
                    elif op == '%': val = self.builder.srem(left, right)
                    return (val, 'int')
                else:  # float
                    if op == '+': val = self.builder.fadd(left, right)
                    elif op == '-': val = self.builder.fsub(left, right)
                    elif op == '*': val = self.builder.fmul(left, right)
                    elif op == '/': val = self.builder.fdiv(left, right)
                    elif op == '%': raise Exception("El operador % no está definido para floats")
                    return (val, 'float')
            
            #agregar manejo para la potencia
            elif op == '^':
                #convertir operandos a float si son enteros
                if left_type == 'int':
                    left = self.builder.sitofp(left, ir.DoubleType())
                    left_type = 'float'
                if right_type == 'int':
                    right = self.builder.sitofp(right, ir.DoubleType())
                    right_type = 'float'
                
                #cuscar o declarar la función intrínseca para la potencia
                pow_func = self.module.globals.get("llvm.pow.f64")
                if not pow_func:
                    pow_func_ty = ir.FunctionType(ir.DoubleType(), [ir.DoubleType(), ir.DoubleType()])
                    pow_func = ir.Function(self.module, pow_func_ty, name="llvm.pow.f64")
                
                result = self.builder.call(pow_func, [left, right])
                return (result, 'float')
            
            #operaciones de comparación
            elif op in ['<', '>', '<=', '>=', '==', '!=']:
                if left_type == 'int':
                    cmp = self.builder.icmp_signed(op, left, right)
                else:
                    cmp = self.builder.fcmp_ordered(op, left, right)
                return (cmp, 'boolean')
        
        #operador negativo
        elif (ctx.getChildCount() == 2 and 
            ctx.getChild(0).getText() == '-'):
            val, val_type = self.visit(ctx.expr(0))
            if val_type == 'int':
                return (self.builder.neg(val), 'int')
            elif val_type == 'float':
                zero = ir.Constant(ir.DoubleType(), 0.0)
                return (self.builder.fsub(zero, val), 'float')
            else:
                raise Exception(f"No se puede aplicar '-' a tipo {val_type}")
        
        #print(f"Expresión no manejada: {ctx.getText()}")  # Debug
        return (None, 'void')


    #llamadas de funciones
    def visitLlamada_funcion(self, ctx: GramaticaParser.Llamada_funcionContext):
        func_name = ctx.VARIABLE().getText()
        func = self.funciones.get(func_name)
        
        if not func:
            raise Exception(f"Función '{func_name}' no definida")
        
        #obtener información de la función para conocer los tipos de los parámetros
        func_info = self.ts.consultar_funcion(func_name)
        parametros = func_info['parametros']  # Lista de tipo, nombre
        
        args = []
        if ctx.argumentos():
            for i, expr in enumerate(ctx.argumentos().expr()):
                arg_val, arg_type = self.visit(expr)
                expected_type = parametros[i][0]
                #si el parámetro es float y se pasó un entero, se convierte
                if expected_type == 'float' and arg_type == 'int':
                    arg_val = self.builder.sitofp(arg_val, ir.DoubleType())
                args.append(arg_val)
        
        call = self.builder.call(func, args)
        return (call, func_info['tipo_retorno'])



    #funciones
    def visitFuncion(self, ctx: GramaticaParser.FuncionContext):
        func_name = ctx.VARIABLE().getText()
        #recupera la función ya registrada en la primera pasada
        function = self.funciones.get(func_name)
        if not function:
            raise Exception(f"Función '{func_name}' no definida")
        
        #obtiene los datos de la función
        func_info = self.ts.consultar_funcion(func_name)
        self.current_func_info = func_info  # Guardar info para usar en el return
        
        #crea un bloque de entrada para la función
        entry_block = function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(entry_block)
        self.locals = {}
        
        #parámetros a variables locales
        for i, (_, param_name) in enumerate(func_info['parametros']):
            alloc = self.builder.alloca(function.args[i].type, name=param_name)
            self.builder.store(function.args[i], alloc)
            self.locals[param_name] = (alloc, func_info['parametros'][i][0])
        
        #generar el cuerpo de la función
        for instr in ctx.instruccion():
            self.visit(instr)
        
        #se agrega si la funcion no termina con return
        if not self.builder.block.is_terminated:
            if func_info['tipo_retorno'] == 'void':
                self.builder.ret_void()
            else:
                self.builder.ret(ir.Constant(self.type_map[func_info['tipo_retorno']], 0))
        
        return None



    #estructuras de control
    def visitSentencia_if(self, ctx: GramaticaParser.Sentencia_ifContext):
        cond, _ = self.visit(ctx.expr(0))
        func = self.builder.function

        then_bb = func.append_basic_block(name="then")
        else_bb = func.append_basic_block(name="else")
        merge_bb = func.append_basic_block(name="ifcont")
        
        self.builder.cbranch(cond, then_bb, else_bb)
        
        #bloque then
        self.builder.position_at_start(then_bb)
        self.visit(ctx.bloque(0))
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)
        
        #bloque else
        self.builder.position_at_start(else_bb)
        if ctx.ELSE():
            self.visit(ctx.bloque(1))
        if not self.builder.block.is_terminated:
            self.builder.branch(merge_bb)
        
        self.builder.position_at_start(merge_bb)
        return None


    def visitSentencia_while(self, ctx: GramaticaParser.Sentencia_whileContext):
        func = self.builder.function
        cond_bb = func.append_basic_block(name="while.cond")
        body_bb = func.append_basic_block(name="while.body")
        end_bb = func.append_basic_block(name="while.end")
        
        self.builder.branch(cond_bb)
        
        #bloque condición
        self.builder.position_at_start(cond_bb)
        cond, _ = self.visit(ctx.expr())
        self.builder.cbranch(cond, body_bb, end_bb)

        self.builder.position_at_start(body_bb)
        self.visit(ctx.bloque())
        self.builder.branch(cond_bb)
    
        self.builder.position_at_start(end_bb)
        return None  
    
    def visitSentencia_return(self, ctx: GramaticaParser.Sentencia_returnContext):
        ret_expr, ret_type = self.visit(ctx.expr())
        expected = self.current_func_info['tipo_retorno']
        #si la función debe retornar int pero la expresión es float se hace la conversion
        if expected == 'int' and ret_type == 'float':
            ret_expr = self.builder.fptosi(ret_expr, ir.IntType(32))
        self.builder.ret(ret_expr)
