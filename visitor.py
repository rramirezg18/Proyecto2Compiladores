from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser


class AnalizadorVisitor(GramaticaVisitor):
    def __init__(self):
        self.env = {}  # Almacena variables
        self.funciones = {}  # Almacena funciones 

    def visitGramatica(self, ctx: GramaticaParser.GramaticaContext):
        # Registra todas las funcionessssssssssssssss
        for funcion in ctx.funcion():
            self.visitFuncion(funcion)

        #print("Funciones registradas:", self.funciones)  # DEBUG

        # Ejecutar las instrucciones principales
        result = None
        for instr in ctx.instruccion():  
            result = self.visit(instr)

        return result



    def visitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        if ctx.tipo() is not None:
            if var_name in self.env:
                raise Exception(f"Variable {var_name} ya está declarada.")
            self.env[var_name] = value
        else:
            if var_name not in self.env:
                raise Exception(f"Variable {var_name} no está declarada.")
            self.env[var_name] = value
        return value

    def visitSentencia_print(self, ctx: GramaticaParser.Sentencia_printContext):
        value = self.visit(ctx.expr())
        if isinstance(value, float):
            print(f"{value:.1f}")
        else:
            print(value)
        return value

    def visitSentencia_if(self, ctx: GramaticaParser.Sentencia_ifContext):
        if self.visit(ctx.expr(0)):
            return self.visit(ctx.bloque(0))
        numCondiciones = len(ctx.expr())
        for i in range(1, numCondiciones):
            if self.visit(ctx.expr(i)):
                return self.visit(ctx.bloque(i))
        if ctx.ELSE() and len(ctx.bloque()) > numCondiciones:
            return self.visit(ctx.bloque(numCondiciones))
        return None

    def visitSentencia_while(self, ctx: GramaticaParser.Sentencia_whileContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
        return None

    def visitSentencia_for(self, ctx: GramaticaParser.Sentencia_forContext):
        self.visit(ctx.declaracion_y_asignacion())  # Inicialización de una variable en fooooooooooooor
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
            self.visit(ctx.for_incremento_y_disminucion())
        return None

    def visitFor_incremento_y_disminucion(self, ctx: GramaticaParser.For_incremento_y_disminucionContext):
        if ctx.getChildCount() == 2:
            var_name = ctx.VARIABLE().getText()
            if ctx.MASMAS():
                if var_name in self.env:
                    self.env[var_name] += 1
                else:
                    raise Exception(f"Variable no definida: {var_name}")
            elif ctx.MENOSMENOS():
                if var_name in self.env:
                    self.env[var_name] -= 1
                else:
                    raise Exception(f"Variable no definida: {var_name}")
        else:
            return self.visit(ctx.declaracion_y_asignacion())
        return None

    def visitBloque(self, ctx: GramaticaParser.BloqueContext):
        for instr in ctx.instruccion():
            resultado = self.visit(instr)
            if isinstance(resultado, tuple) and resultado[0] == "return":
                return resultado  
        return None




    def visitExpr(self, ctx: GramaticaParser.ExprContext):
        # Manejo de llamadas a funciones dentro de expresiones
        if ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())

        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            expr_value = self.visit(ctx.expr(0))
            return -expr_value if expr_value is not None else 0

        if ctx.getChildCount() == 1:
            token_text = ctx.getText()
            try:
                return float(token_text)
            except ValueError:
                if token_text in self.env:
                    return self.env[token_text]
                elif token_text.startswith('"') and token_text.endswith('"'):
                    return token_text[1:-1]
                elif token_text == "true":
                    return True
                elif token_text == "false":
                    return False
                else:
                    raise Exception("Variable no definida o valor inválido: " + token_text)

        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.expr(0))
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '^':
                return left ** right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '<':
                return left < right
            elif op == '>':
                return left > right
            elif op == '<=':
                return left <= right
            elif op == '>=':
                return left >= right
            else:
                raise Exception("Operador desconocido: " + op)

        return self.visitChildren(ctx)

    def visitFuncion(self, ctx: GramaticaParser.FuncionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        parametros = self.visit(ctx.parametros()) if ctx.parametros() else []
        instrucciones = ctx.instruccion()  # Todas las instrucciones dentro de la función
        sentencia_ret = ctx.sentencia_return() if ctx.sentencia_return() else None
        # guardaambas partes
        self.funciones[nombre_funcion] = (parametros, instrucciones, sentencia_ret)
        return None



    def visitParametros(self, ctx: GramaticaParser.ParametrosContext):
        parametros = []
        for i in range(len(ctx.tipo())):
            tipo = ctx.tipo(i).getText()
            nombre = ctx.VARIABLE(i).getText()
            parametros.append((tipo, nombre))
        return parametros

    def visitLlamada_funcion(self, ctx: GramaticaParser.Llamada_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        #print(f"Llamando a la función: {nombre_funcion}") 
        if nombre_funcion not in self.funciones:
            raise Exception(f"Función {nombre_funcion} no definida.")

        parametros = self.visit(ctx.argumentos())
        #print(f"Parámetros recibidos: {parametros}")

        # trae ambas partes de la función:
        funcion_parametros, instrucciones, sentencia_ret = self.funciones[nombre_funcion]

        if len(parametros) != len(funcion_parametros):
            raise Exception(f"Cantidad de parámetros incorrecta para {nombre_funcion}.")

        # Guardar entorno actual y crear un nuevo entorno local
        entorno_anterior = self.env.copy()
        self.env = {}

        # Asignar parámetros al entorno local con conversión de tipos
        for i, (tipo, nombre) in enumerate(funcion_parametros):
            self.env[nombre] = int(parametros[i]) if tipo == "int" else parametros[i]

        # Ejecutar cada instrucción en la función
        for instr in instrucciones:
            resultado = self.visit(instr)
            if isinstance(resultado, tuple) and resultado[0] == "return":
                self.env = entorno_anterior  # Restaurar el entorno antes de salir
                return resultado[1]

        # Si ninguna instrucción produjo retorno y hay sentencia_return, evalúala
        if sentencia_ret:
            resultado = self.visit(sentencia_ret)
            if isinstance(resultado, tuple) and resultado[0] == "return":
                self.env = entorno_anterior
                return resultado[1]
            else:
                self.env = entorno_anterior
                return resultado

        # Restaurar el entorno antes de salir
        self.env = entorno_anterior
        return None





    def visitArgumentos(self, ctx: GramaticaParser.ArgumentosContext):
        argumentos = []
        for arg in ctx.expr():
            argumentos.append(self.visit(arg))
        return argumentos
    
    def visitSentencia_return(self, ctx: GramaticaParser.Sentencia_returnContext):
        return ("return", self.visit(ctx.expr()))



