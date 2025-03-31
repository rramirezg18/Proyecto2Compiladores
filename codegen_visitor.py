import llvmlite.ir as ir
from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser

class CodeGenVisitor(GramaticaVisitor):
    def __init__(self):
        # Crear el módulo LLVM
        self.module = ir.Module(name="mi_modulo")
        # Mapeo de tipos de nuestro lenguaje a tipos LLVM
        self.type_map = {
            "int": ir.IntType(32),
            "float": ir.DoubleType(),
            "boolean": ir.IntType(1),
            "string": ir.IntType(8).as_pointer(),
            "void": ir.VoidType()
        }
        # Declarar la función printf (variádica) para la sentencia print
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")
        # Para poder construir IR en cada función
        self.builder = None
        self.entry_builder = None  # Inicialización para el builder del entry block
        # Tabla de variables locales: nombre -> alloca
        self.locals = {}
        # Tabla de funciones (nombre -> ir.Function)
        self.functions = {}

    def get_ir(self):
        return str(self.module)

    # --- Helpers ---
    def create_entry_alloca(self, function, var_name, var_type):
        entry = function.entry_basic_block
        builder = ir.IRBuilder(entry)
        builder.position_at_start(entry)
        return builder.alloca(var_type, name=var_name)



    # --- Nodo raíz: g. ---
    def visitGramatica(self, ctx: GramaticaParser.GramaticaContext):
        # Verifica si se definió una función "main" en el código fuente
        main_defined = any(func.VARIABLE().getText() == "main" for func in ctx.funcion())
        
        # Si NO se definió, genera la función "main" a partir de instrucciones globales
        if not main_defined:
            main_type = ir.FunctionType(ir.IntType(32), [])
            main_function = ir.Function(self.module, main_type, name="main")
            self.functions["main"] = main_function
            block = main_function.append_basic_block(name="entry")
            self.builder = ir.IRBuilder(block)
            self.entry_builder = self.builder  # <--- Asegurarse de asignarlo
            self.locals = {}
            
            for instr in ctx.instruccion():
                self.visit(instr)
            
            if not self.builder.block.is_terminated:
                self.builder.ret(ir.Constant(ir.IntType(32), 0))
        
        # Procesa las definiciones de función (incluida la "main" definida por el usuario)
        for func in ctx.funcion():
            self.visit(func)
        
        return self.get_ir()


    # --- Funciones ---
    def visitFuncion(self, ctx: GramaticaParser.FuncionContext):
        # Obtener el tipo de retorno y el nombre de la función
        ret_type = self.type_map[ctx.tipo().getText()] if ctx.tipo() else self.type_map["void"]
        func_name = ctx.VARIABLE().getText()
        # Procesar parámetros (si existen)
        param_types = []
        param_names = []
        if ctx.parametros():
            for i in range(len(ctx.parametros().tipo())):
                ptype = self.type_map[ctx.parametros().tipo(i).getText()]
                pname = ctx.parametros().VARIABLE(i).getText()
                param_types.append(ptype)
                param_names.append(pname)
        func_type = ir.FunctionType(ret_type, param_types)
        function = ir.Function(self.module, func_type, name=func_name)
        self.functions[func_name] = function

        # Crear bloque de entrada y dos builders:
        # uno para asignaciones (allocas) y otro para instrucciones normales.
        block = function.append_basic_block(name="entry")
        self.entry_builder = ir.IRBuilder(block)
        self.entry_builder.position_at_start(block)
        self.builder = ir.IRBuilder(block)

        self.locals = {}
        # Almacenar los parámetros en el entorno local (con alloca en el entry block)
        for i, arg in enumerate(function.args):
            arg.name = param_names[i]
            # Usa el entry_builder para crear el alloca
            alloc = self.entry_builder.alloca(param_types[i], name=arg.name)
            self.builder.store(arg, alloc)
            self.locals[arg.name] = alloc

        # Generar código para las instrucciones de la función
        for instr in ctx.instruccion():
            self.visit(instr)
        # Procesar sentencia_return (si existe)
        if ctx.sentencia_return():
            ret_val, ret_val_type = self.visit(ctx.sentencia_return())
            self.builder.ret(ret_val)
        elif ret_type == self.type_map["void"]:
            self.builder.ret_void()
        else:
            raise Exception(f"La función '{func_name}' debe retornar un valor.")

    # --- Declaración y asignación ---
    def visitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        val, expr_type = self.visit(ctx.expr())
        if ctx.tipo() is not None:
            declared_type = ctx.tipo().getText()
            llvm_type = self.type_map[declared_type]
            # Conversión int -> float si es necesario
            if declared_type == "float" and expr_type == "int":
                val = self.builder.sitofp(val, llvm_type)
                expr_type = "float"
            # Inserta el alloca en el entry block usando entry_builder
            alloc = self.entry_builder.alloca(llvm_type, name=var_name)
            self.builder.store(val, alloc)
            self.locals[var_name] = alloc
            return (val, declared_type)
        else:
            if var_name not in self.locals:
                raise Exception(f"Variable '{var_name}' no definida.")
            ptr = self.locals[var_name]
            self.builder.store(val, ptr)
            return (val, expr_type)


    # --- Sentencia print ---
    def visitSentencia_print(self, ctx: GramaticaParser.Sentencia_printContext):
        val, val_type = self.visit(ctx.expr())
        # Elegir formato según tipo
        if val_type == "int":
            fmt = "%d\n\0"
        elif val_type == "float":
            fmt = "%f\n\0"
        elif val_type == "string":
            fmt = "%s\n\0"
        else:
            fmt = "%d\n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        fmt_var_name = "fstr_" + val_type
        if fmt_var_name in self.module.globals:
            global_fmt = self.module.globals[fmt_var_name]
        else:
            global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name=fmt_var_name)
            global_fmt.linkage = "internal"
            global_fmt.global_constant = True
            global_fmt.initializer = c_fmt
        fmt_ptr = self.builder.bitcast(global_fmt, ir.IntType(8).as_pointer())
        self.builder.call(self.printf, [fmt_ptr, val])
        return None


    # --- Estructuras de control: if ---
    def visitSentencia_if(self, ctx: GramaticaParser.Sentencia_ifContext):
        cond, cond_type = self.visit(ctx.expr(0))
        if cond_type != "boolean":
            raise Exception("La condición del if debe ser booleana.")
        func = self.builder.function
        then_bb = func.append_basic_block("then")
        else_bb = func.append_basic_block("else")
        merge_bb = func.append_basic_block("ifend")
        self.builder.cbranch(cond, then_bb, else_bb)
        # Bloque then
        self.builder.position_at_start(then_bb)
        self.visit(ctx.bloque(0))
        self.builder.branch(merge_bb)
        # Bloque else (si existe)
        self.builder.position_at_start(else_bb)
        if ctx.ELSE():
            self.visit(ctx.bloque(1))
        self.builder.branch(merge_bb)
        self.builder.position_at_start(merge_bb)
        return None
    
        # --- Estructuras de control: for ---
    # --- Estructuras de control: for ---
    # --- Estructuras de control: for ---
    def visitSentencia_for(self, ctx: GramaticaParser.Sentencia_forContext):
        # Inicialización (por ejemplo, "int i = 10;")
        self.visit(ctx.declaracion_y_asignacion())
        func = self.builder.function

        # Crear bloques básicos para la estructura del for:
        cond_bb = func.append_basic_block("for.cond")
        body_bb = func.append_basic_block("for.body")
        inc_bb = func.append_basic_block("for.inc")
        after_bb = func.append_basic_block("for.after")

        # Salto al bloque de condición
        self.builder.branch(cond_bb)

        # Bloque de condición: evaluar "i >= 0"
        self.builder.position_at_start(cond_bb)
        cond, cond_type = self.visit(ctx.expr())
        if cond_type != "boolean":
            raise Exception("La condición del for debe ser booleana.")
        self.builder.cbranch(cond, body_bb, after_bb)

        # Bloque del cuerpo: ejecutar las instrucciones del for (por ejemplo, "print(i);")
        self.builder.position_at_start(body_bb)
        self.visit(ctx.bloque())
        self.builder.branch(inc_bb)

        # Bloque de incremento/decremento: ejecutar "i--" o lo definido
        self.builder.position_at_start(inc_bb)
        self.visit(ctx.for_incremento_y_disminucion())
        self.builder.branch(cond_bb)

        # Bloque de salida: continuar con el código que sigue al for
        self.builder.position_at_start(after_bb)
        return None




    def visitFor_incremento_y_disminucion(self, ctx: GramaticaParser.For_incremento_y_disminucionContext):
        # Si la regla es: VARIABLE (MASMAS | MENOSMENOS)
        if ctx.getChildCount() == 2:
            var_name = ctx.VARIABLE().getText()
            if var_name not in self.locals:
                raise Exception(f"Variable '{var_name}' no definida.")
            ptr = self.locals[var_name]
            loaded = self.builder.load(ptr, name=var_name)
            op = ctx.getChild(1).getText()
            if op == "++":
                updated = self.builder.add(loaded, ir.Constant(ir.IntType(32), 1))
            elif op == "--":
                updated = self.builder.sub(loaded, ir.Constant(ir.IntType(32), 1))
            else:
                raise Exception(f"Operador '{op}' no soportado en for_incremento_y_disminucion.")
            self.builder.store(updated, ptr)
            return None
        else:
            # Caso alternativo: delegar a la regla de declaración y asignación,
            # por ejemplo, para operaciones como "i = i + 2"
            return self.visit(ctx.declaracion_y_asignacion())







    # --- Estructuras de control: while ---
    def visitSentencia_while(self, ctx: GramaticaParser.Sentencia_whileContext):
        func = self.builder.function
        loop_bb = func.append_basic_block("while.loop")
        after_bb = func.append_basic_block("while.after")
        self.builder.branch(loop_bb)
        self.builder.position_at_start(loop_bb)
        cond, cond_type = self.visit(ctx.expr())
        if cond_type != "boolean":
            raise Exception("La condición del while debe ser booleana.")
        self.builder.cbranch(cond, loop_bb, after_bb)
        self.visit(ctx.bloque())
        self.builder.branch(loop_bb)
        self.builder.position_at_start(after_bb)
        return None

    # --- Estructuras de control: for ---
    def visitExpr(self, ctx: GramaticaParser.ExprContext):
        # Llamada a función
        if ctx.getChildCount() == 1 and ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())
        # Caso literal: variable, número, cadena o booleano
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if text.startswith('"') and text.endswith('"'):
                s = text[1:-1]
                c_str = ir.Constant(ir.ArrayType(ir.IntType(8), len(s)+1),
                                      bytearray(s.encode("utf8") + b'\0'))
                global_str = ir.GlobalVariable(self.module, c_str.type, name="str_" + s[:4])
                global_str.linkage = "internal"
                global_str.global_constant = True
                global_str.initializer = c_str
                ptr = self.builder.bitcast(global_str, ir.IntType(8).as_pointer())
                return (ptr, "string")
            if text == "true":
                return (ir.Constant(ir.IntType(1), 1), "boolean")
            if text == "false":
                return (ir.Constant(ir.IntType(1), 0), "boolean")
            try:
                if '.' in text:
                    return (ir.Constant(ir.DoubleType(), float(text)), "float")
                else:
                    return (ir.Constant(ir.IntType(32), int(text)), "int")
            except ValueError:
                # Variable: cargar su valor
                if text in self.locals:
                    ptr = self.locals[text]
                    loaded = self.builder.load(ptr, name=text)
                    for key, llvm_type in self.type_map.items():
                        if llvm_type == ptr.type.pointee:
                            return (loaded, key)
                    return (loaded, "unknown")
        # Operador unario: -expr
        if ctx.getChildCount() == 2:
            if ctx.getChild(0).getText() == '-':
                val, t = self.visit(ctx.expr(0))
                if t == "int":
                    return (self.builder.neg(val), "int")
                elif t == "float":
                    zero = ir.Constant(ir.DoubleType(), 0.0)
                    return (self.builder.fsub(zero, val), "float")
                else:
                    raise Exception(f"Operador '-' no soportado para tipo {t}")
        # Expresiones binarias o agrupadas
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.expr(0))
            else:
                left, lt = self.visit(ctx.expr(0))
                right, rt = self.visit(ctx.expr(1))
                op = ctx.getChild(1).getText()
                if op == '+':
                    if lt == "int" and rt == "int":
                        return (self.builder.add(left, right), "int")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fadd(left_val, right_val), "float")
                    elif lt == "string" and rt == "string":
                        raise Exception("Concatenación de cadenas no implementada.")
                elif op == '-':
                    if lt == "int" and rt == "int":
                        return (self.builder.sub(left, right), "int")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fsub(left_val, right_val), "float")
                elif op == '*':
                    if lt == "int" and rt == "int":
                        return (self.builder.mul(left, right), "int")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fmul(left_val, right_val), "float")
                elif op == '/':
                    if lt == "int" and rt == "int":
                        return (self.builder.sdiv(left, right), "int")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fdiv(left_val, right_val), "float")
                elif op == '^':
                    pow_fn = self.module.globals.get("pow")
                    if pow_fn is None:
                        pow_ty = ir.FunctionType(ir.DoubleType(), [ir.DoubleType(), ir.DoubleType()])
                        pow_fn = ir.Function(self.module, pow_ty, name="pow")
                    left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                    right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                    result = self.builder.call(pow_fn, [left_val, right_val])
                    return (result, "float")
                elif op == '>=':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('>=', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('>=', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '>=' no soportado para tipos distintos.")
                elif op == '<=':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('<=', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('<=', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '<=' no soportado para tipos distintos.")
                elif op == '>':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('>', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('>', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '>' no soportado para tipos distintos.")
                elif op == '<':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('<', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('<', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '<' no soportado para tipos distintos.")
                elif op == '==':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('==', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('==', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '==' no soportado para tipos distintos o complejos.")
                elif op == '!=':
                    if lt == "int" and rt == "int":
                        return (self.builder.icmp_signed('!=', left, right), "boolean")
                    elif (lt == "int" and rt == "float") or (lt == "float" and rt == "int") or (lt == "float" and rt == "float"):
                        left_val = left if lt == "float" else self.builder.sitofp(left, ir.DoubleType())
                        right_val = right if rt == "float" else self.builder.sitofp(right, ir.DoubleType())
                        return (self.builder.fcmp_ordered('!=', left_val, right_val), "boolean")
                    else:
                        raise Exception("Operador '!=' no soportado para tipos distintos.")
                else:
                    raise Exception(f"Operador '{op}' no implementado.")
        return self.visitChildren(ctx)



    # --- Llamada a función ---
    def visitLlamada_funcion(self, ctx: GramaticaParser.Llamada_funcionContext):
        func_name = ctx.VARIABLE().getText()
        if func_name not in self.functions:
            raise Exception(f"Función '{func_name}' no definida.")
        function = self.functions[func_name]
        args = []
        if ctx.argumentos():
            for expr in ctx.argumentos().expr():
                arg_val, arg_type = self.visit(expr)
                args.append(arg_val)
        ret = self.builder.call(function, args)
        # Determinar tipo de retorno (simplificado)
        ret_type = function.function_type.return_type
        for key, llvm_type in self.type_map.items():
            if llvm_type == ret_type:
                return (ret, key)
        return (ret, "unknown")

    # --- Sentencia return ---
    def visitSentencia_return(self, ctx: GramaticaParser.Sentencia_returnContext):
        ret_val, ret_type = self.visit(ctx.expr())
        return ("return", (ret_val, ret_type))
