from GramaticaListener import GramaticaListener
from GramaticaParser import GramaticaParser
from tabla_simbolos import TablaSimbolos

class ValidacionListener(GramaticaListener):
    def __init__(self):
        self.ts = TablaSimbolos()#instancia para crear la tabla de simbolos

    # Métodos para el control de entornos
    def enterBloque(self, ctx: GramaticaParser.BloqueContext):
        self.ts.push_env()

    def exitBloque(self, ctx: GramaticaParser.BloqueContext):
        self.ts.pop_env()

    # Control de ámbitos para funciones
    def enterFuncion(self, ctx: GramaticaParser.FuncionContext):
        self.ts.push_env()#crea un entorno nuevo para variables cuando es una funcion
        #declaracion de parametros en un entorno
        if ctx.parametros():
            for i in range(len(ctx.parametros().tipo())):
                tipo = ctx.parametros().tipo(i).getText()
                nombre = ctx.parametros().VARIABLE(i).getText()
                self.ts.agregar_variable(nombre, tipo)

    def exitFuncion(self, ctx: GramaticaParser.FuncionContext):
        #registra la funcion en la tabla
        nombre_funcion = ctx.VARIABLE().getText()
        parametros = []
        if ctx.parametros():
            for i in range(len(ctx.parametros().tipo())):
                tipo = ctx.parametros().tipo(i).getText()
                nombre = ctx.parametros().VARIABLE(i).getText()
                parametros.append((tipo, nombre))
        tipo_retorno = ctx.tipo().getText()  if ctx.tipo() else "void"
        self.ts.agregar_funcion(nombre_funcion, tipo_retorno, parametros)
        # Salir del ámbito local de la función
        self.ts.pop_env()

    # Validación de declaraciones y asignaciones
    def exitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        if ctx.tipo():
            declared_type = ctx.tipo().getText()
            self.ts.agregar_variable(var_name, declared_type)
        else:
            # para reasignaciond de variables que ya existen
            if not self.ts.existe_variable(var_name):
                raise Exception(f"Error semántico: La variable '{var_name}' no está declarada.")

    # Valida el uso de variables en expresiones
    def exitExpr(self, ctx: GramaticaParser.ExprContext):
        # Si la expresión es una llamada a función no se valida como variable.
        if ctx.getChildCount() == 1 and ctx.llamada_funcion() is not None:
            return

        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if (not text.startswith('"') and text not in ["true", "false"]) and not self.is_number(text):
                # Verifica que la variable exista en la tabla de símbolos
                if not self.ts.existe_variable(text):
                    raise Exception(f"Error semántico: La variable '{text}' no está declarada.")

    def is_number(self, text):
        try:
            float(text)
            return True
        except ValueError:
            return False
