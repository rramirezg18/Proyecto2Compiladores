#analizador semantico
#valida ambito de funciones, variables scopes

from GramaticaListener import GramaticaListener
from GramaticaParser import GramaticaParser
from tabla_simbolos import TablaSimbolos

class AnalizadorSemantico(GramaticaListener):
    def __init__(self, tabla_simbolos):
        self.ts = tabla_simbolos
        self.current_scope = []


    def enterGramatica(self, ctx: GramaticaParser.GramaticaContext):
        #print("Iniciando registro de funciones...")  # Debug
        for func_ctx in ctx.funcion():
            nombre = func_ctx.VARIABLE().getText()  # Asegurar que el nombre sea un string
            tipo_retorno = func_ctx.tipo().getText() if func_ctx.tipo() else "void"
            parametros = []
            
            if func_ctx.parametros():
                tipos = func_ctx.parametros().tipo()
                nombres = func_ctx.parametros().VARIABLE()
                for tipo, nombre_var in zip(tipos, nombres):
                    parametros.append((tipo.getText(), nombre_var.getText()))

            #print(f"Registrando función: {nombre} con retorno {tipo_retorno} y parámetros {parametros}")  
            self.ts.agregar_funcion(nombre, tipo_retorno, parametros)

        #print("Funciones registradas:", self.ts.funciones)  




    def enterMain(self, ctx: GramaticaParser.MainContext):
        #print("Creando ámbito para main")  
        self.ts.push_env()
        # Registrar parámetros de main (aunque no debería tener)
        #if ctx.parametros():
            #for tipo, var in zip(ctx.parametros().tipo(), ctx.parametros().VARIABLE()):
                #self.ts.agregar_variable(var.getText(), tipo.getText())


    def exitMain(self, ctx: GramaticaParser.MainContext):
        self.ts.pop_env()

    def enterBloque(self, ctx: GramaticaParser.BloqueContext):
        self.ts.push_env()

    def exitBloque(self, ctx: GramaticaParser.BloqueContext):
        self.ts.pop_env()

    def exitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        if ctx.tipo():  # Declaración con tipo de dato
            tipo = ctx.tipo().getText()
            #print(f"Registrando variable: {var_name} como {tipo}")  # Debug
            self.ts.agregar_variable(var_name, tipo)
        else:  # Re-asignación de variables
            if not self.ts.existe_variable(var_name):
                raise Exception(f"Variable '{var_name}' no declarada")

    #valida las expresiones
    def exitExpr(self, ctx: GramaticaParser.ExprContext):
        if ctx.llamada_funcion():
            self.validar_llamada_funcion(ctx.llamada_funcion())
        elif ctx.getChildCount() == 1 and not ctx.llamada_funcion():
            token = ctx.getText()
            if not (token in ['true', 'false'] or token.isdigit() or '.' in token or token.startswith('"')):
                if not self.ts.existe_variable(token):
                    raise Exception(f"Variable '{token}' no declarada")

    #Métodos Auxiliares
    def inferir_tipo_expr(self, expr_ctx):
        if expr_ctx.llamada_funcion():
            return self.validar_llamada_funcion(expr_ctx.llamada_funcion())
        elif expr_ctx.getChildCount() == 1:
            token = expr_ctx.getText()
            if token in ['true', 'false']:
                return 'boolean'
            elif token.startswith('"'):
                return 'string'
            elif '.' in token:
                return 'float'
            elif token.isdigit():
                return 'int'
            else:
                return self.ts.consultar_variable(token)
        else:
            # Para expresiones compuestas usar un metodo helper para encotrar el tipo.
            return self._compute_expr_type(expr_ctx)


    def validar_llamada_funcion(self, llamada_ctx):
        nombre = llamada_ctx.VARIABLE().getText()

        if not self.ts.existe_funcion(nombre):
            raise Exception(f"Error semántico:\nFunción '{nombre}' no definida")

        func_info = self.ts.consultar_funcion(nombre)
        args = [self.inferir_tipo_expr(e) for e in llamada_ctx.argumentos().expr()] if llamada_ctx.argumentos() else []

        if len(args) != len(func_info['parametros']):
            raise Exception(f"Error semántico:\nNúmero incorrecto de argumentos en llamada a '{nombre}'")

        for arg, (tipo_esperado, _) in zip(args, func_info['parametros']):
            if not self.ts.tipos_compatibles(tipo_esperado, arg):
                raise Exception(f"Error semántico:\nTipo de argumento '{arg}' no compatible con '{tipo_esperado}'")

        return func_info['tipo_retorno']

    

    def enterFuncion(self, ctx: GramaticaParser.FuncionContext):
        nombre = ctx.VARIABLE().getText()
        tipo_retorno = ctx.tipo().getText() if ctx.tipo() else "void"

        #print(f"Entrando en función: {nombre}")  # Debug

        # Crear nuevo ámbito para lo que encuentre deentro de la funcion mas variables solo para ese ambito
        self.ts.push_env()

        # Registrar los parámetros en la tabla de símbolos
        if ctx.parametros():
            for tipo, var in zip(ctx.parametros().tipo(), ctx.parametros().VARIABLE()):
                self.ts.agregar_variable(var.getText(), tipo.getText())
                #print(f"Parametro registrado: {var.getText()} como {tipo.getText()}")  # Debug



    def exitFuncion(self, ctx: GramaticaParser.FuncionContext):
        #print(f"Saliendo de función: {ctx.VARIABLE().getText()}")  # Debug
        self.ts.pop_env()



    def _compute_expr_type(self, ctx):
        #hoja con un solo hijo (literal o variable)
        if ctx.getChildCount() == 1:
            token = ctx.getText()
            if token in ['true', 'false']:
                return 'boolean'
            elif token.startswith('"'):
                return 'string'
            elif '.' in token:
                return 'float'
            elif token.isdigit():
                return 'int'
            else:
                return self.ts.consultar_variable(token)
        #expresión entre paréntesis
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self._compute_expr_type(ctx.expr(0))
        #operación binaria
        if ctx.getChildCount() == 3:
            left_type = self._compute_expr_type(ctx.expr(0))
            right_type = self._compute_expr_type(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op in ['+', '-', '*', '/', '%']:
                #si no es float, explicitamente sea int
                if left_type == 'float' or right_type == 'float':
                    return 'float'
                else:
                    return 'int'
            elif op == '^':
                #evalua la potencia como float
                return 'float'
            elif op in ['<', '>', '<=', '>=', '==', '!=']:
                return 'boolean'
        #operador negativo
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            return self._compute_expr_type(ctx.expr(0))
        return 'void'

