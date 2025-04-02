#valida las expresiones a partir del visitor original


from antlr4 import *
from GramaticaVisitor import GramaticaVisitor  # Importación faltante
from GramaticaParser import GramaticaParser

# permite devolver el valor de una funcion con return
class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class AnalizadorVisitor(GramaticaVisitor):  #hereda directamente del Visitor original generado por antlr
    def __init__(self):
        super().__init__()
        self.variables = [{}]
        self.funciones = {}
    
    def push_scope(self):
        self.variables.append({})
    
    def pop_scope(self):
        self.variables.pop()
    
    def current_scope(self):
        return self.variables[-1]
    
    # Visit a parse tree produced by GramaticaParser#gramatica.
    def visitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        # Procesar todas las funciones primero
        for funcion in ctx.funcion():
            self.visit(funcion)
        
        # Buscar y ejecutar main
        main_block = ctx.main()
        if main_block:
            return self.visit(main_block)
        return None

    # Visit a parse tree produced by GramaticaParser#main.
    def visitMain(self, ctx:GramaticaParser.MainContext):
        self.push_scope()
        for inst in ctx.instruccion():
            self.visit(inst)
        self.pop_scope()
        return None

    # Visit a parse tree produced by GramaticaParser#instruccion.
    def visitInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#declaracion_y_asignacion.
    def visitDeclaracion_y_asignacion(self, ctx:GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        
        # Buscar en qué ámbito está la variable
        for scope in reversed(self.variables):
            if var_name in scope:
                scope[var_name] = value
                #print(f"Variable {var_name} actualizada a {value}")
                return

        # Si no existe, se agrega al ámbito actual
        self.current_scope()[var_name] = value
        #print(f"Variable {var_name} declarada con valor {value}")


    # Visit a parse tree produced by GramaticaParser#tipo.
    def visitTipo(self, ctx:GramaticaParser.TipoContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by GramaticaParser#sentencia_print.
    def visitSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        value = self.visit(ctx.expr())
        print(value)
        return None

    # Visit a parse tree produced by GramaticaParser#sentencia_if.
    def visitSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        condicion = self.visit(ctx.expr(0))
        #print(f"Evaluando if, condición: {condicion}")  # <-- Depuración

        if isinstance(condicion, (int, float, bool)):  # Solo números y booleanos
            condicion = bool(condicion)
        else:
            raise Exception(f"Condición no válida en if: {condicion}")
        
        if condicion:
            return self.visit(ctx.bloque(0))

        # Evaluar else if
        for i in range(1, len(ctx.expr())):
            condicion = self.visit(ctx.expr(i))
            if isinstance(condicion, (int, float, bool)):
                condicion = bool(condicion)
            else:
                raise Exception(f"Condición no válida en else if: {condicion}")

            if condicion:
                return self.visit(ctx.bloque(i))
            if condicion:
                #print("Entrando en el bloque del if")
                self.visit(ctx.bloque(0))  # Ejecutamos el bloque
                #print(f"Valor de w después del if: {self.current_scope().get('w', 'No existe')}")


        # Evaluar else final
        bloques = ctx.bloque()
        expr_count = len(ctx.expr())
        if len(bloques) > expr_count:
            return self.visit(bloques[-1])

        return None


    # Visit a parse tree produced by GramaticaParser#sentencia_while.
    def visitSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
        return None

    # Visit a parse tree produced by GramaticaParser#sentencia_for.
    def visitSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        self.push_scope()  # Nuevo ámbito para el for
        
        # Inicialización si existe
        if ctx.declaracion_y_asignacion():
            self.visit(ctx.declaracion_y_asignacion())
        
        # Verificar condición inicial
        if not ctx.expr():
            raise Exception("El bucle for debe tener una condición")
        
        # Ejecutar el bucle
        while True:
            # Evaluar condición
            condicion = self.visit(ctx.expr())
            if not condicion:
                break
            
            # Ejecutar el cuerpo del bucle
            self.visit(ctx.bloque())
            
            # Ejecutar el incremento o disminucion si existe
            if ctx.for_incremento_y_disminucion():
                self.visit(ctx.for_incremento_y_disminucion())
        
        self.pop_scope()  # Salir del ámbito del for
        return None

    # Visit a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def visitFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        if ctx.declaracion_y_asignacion():
            return self.visit(ctx.declaracion_y_asignacion())
        else:
            var_name = ctx.VARIABLE().getText()
            current = self.current_scope().get(var_name, 0)
            if ctx.MASMAS():
                self.current_scope()[var_name] = current + 1
            else:
                self.current_scope()[var_name] = current - 1
            return None

    # Visit a parse tree produced by GramaticaParser#sentencia_return.
    def visitSentencia_return(self, ctx:GramaticaParser.Sentencia_returnContext):
        result = self.visit(ctx.expr())
        raise ReturnValue(result)  # Ya no necesita conversión aquí



    # Visit a parse tree produced by GramaticaParser#funcion.
    def visitFuncion(self, ctx:GramaticaParser.FuncionContext):
        func_name = ctx.VARIABLE().getText()
        params = self.visit(ctx.parametros()) if ctx.parametros() else []
        self.funciones[func_name] = {
            'params': params,
            'body': ctx,
            'return_type': ctx.tipo().getText() if ctx.tipo() else None
        }
        return None

    # Visit a parse tree produced by GramaticaParser#parametros.
    def visitParametros(self, ctx:GramaticaParser.ParametrosContext):
        return [(t.getText(), var.getText()) for t, var in zip(ctx.tipo(), ctx.VARIABLE())]

    # Visit a parse tree produced by GramaticaParser#argumentos.
    def visitArgumentos(self, ctx:GramaticaParser.ArgumentosContext):
        return [self.visit(expr) for expr in ctx.expr()]

    # Visit a parse tree produced by GramaticaParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:GramaticaParser.Llamada_funcionContext):
        func_name = ctx.VARIABLE().getText()
        
        if func_name not in self.funciones:
            raise Exception(f"Función no definida: {func_name}")
        
        func = self.funciones[func_name]
        args = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        
        if len(args) != len(func['params']):
            raise Exception(f"Número incorrecto de argumentos para {func_name}")
        
        self.push_scope()
        
        # Asigna los parámetros en una funcion
        for (param_type, param_name), arg_val in zip(func['params'], args):
            self.current_scope()[param_name] = arg_val
        
        result = None
        try:
            # Ejecutar todas las instrucciones de la función
            for inst in func['body'].instruccion():
                self.visit(inst)
            # En caso de que la función tenga un return fuera del bloque de instrucciones
            if func['body'].sentencia_return():
                self.visit(func['body'].sentencia_return())
        except ReturnValue as rv:
            result = rv.value
        
        self.pop_scope()
        return result

    # Visit a parse tree produced by GramaticaParser#bloque.
    def visitBloque(self, ctx:GramaticaParser.BloqueContext):
        self.push_scope()
        for inst in ctx.instruccion():
            self.visit(inst)
        self.pop_scope()
        return None

    # Visit a parse tree produced by GramaticaParser#expr.
    def visitExpr(self, ctx:GramaticaParser.ExprContext):
        if ctx.POTENCIA():
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            return left ** right
        elif ctx.MULTIPLICACION():
            return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))
        elif ctx.DIVISION():
            return self.visit(ctx.expr(0)) / self.visit(ctx.expr(1))
        elif ctx.MOD():
            return self.visit(ctx.expr(0)) % self.visit(ctx.expr(1))
        elif ctx.MAS():
            return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))
        elif ctx.MENOS():
            if ctx.getChildCount() == 2:  # Negación unaria
                return -self.visit(ctx.expr(0))
            else:  # Resta binaria
                return self.visit(ctx.expr(0)) - self.visit(ctx.expr(1))
        elif ctx.MAYOR():
            return self.visit(ctx.expr(0)) > self.visit(ctx.expr(1))
        elif ctx.MENOR():
            return self.visit(ctx.expr(0)) < self.visit(ctx.expr(1))
        elif ctx.MAYOR_IGUAL_QUE():
            return self.visit(ctx.expr(0)) >= self.visit(ctx.expr(1))
        elif ctx.MENOR_IGUAL_QUE():
            return self.visit(ctx.expr(0)) <= self.visit(ctx.expr(1))
        elif ctx.IGUAL():
            return self.visit(ctx.expr(0)) == self.visit(ctx.expr(1))
        elif ctx.DIFERENTE():
            return self.visit(ctx.expr(0)) != self.visit(ctx.expr(1))
        elif ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())
        elif ctx.VARIABLE():
            var_name = ctx.VARIABLE().getText()
            #print(f"Buscando variable: {var_name}, Variables actuales: {self.variables}")  # Debug
            for scope in reversed(self.variables):
                if var_name in scope:
                    return scope[var_name]
            raise Exception(f"Variable no definida: {var_name}")
        elif ctx.NUMERO():
            num_str = ctx.NUMERO().getText()
            return float(num_str) if '.' in num_str else int(num_str)
        elif ctx.CADENA():
            return ctx.CADENA().getText()[1:-1]  # Eliminar comillas
        elif ctx.BOOLEANO():
            valor = ctx.BOOLEANO().getText().lower()  # Convertir a minúsculas para evitar problemas con mayúsculas
            #print(f"Valor booleano detectado: {valor}")  # Debug
            if valor == 'true':
                return True
            elif valor == 'false':
                return False
            else:
                raise Exception(f"Valor booleano no reconocido: {valor}")

        elif ctx.PARENTESIS_APERTURA():
            return self.visit(ctx.expr(0))
        else:
            raise Exception("Expresión no reconocida")
