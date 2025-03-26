# Generated from Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete listener for a parse tree produced by GramaticaParser.
class GramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by GramaticaParser#gramatica.
    def enterGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass

    # Exit a parse tree produced by GramaticaParser#gramatica.
    def exitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        pass


    # Enter a parse tree produced by GramaticaParser#instruccion.
    def enterInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#instruccion.
    def exitInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#declaracion_y_asignacion.
    def enterDeclaracion_y_asignacion(self, ctx:GramaticaParser.Declaracion_y_asignacionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#declaracion_y_asignacion.
    def exitDeclaracion_y_asignacion(self, ctx:GramaticaParser.Declaracion_y_asignacionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#tipo.
    def enterTipo(self, ctx:GramaticaParser.TipoContext):
        pass

    # Exit a parse tree produced by GramaticaParser#tipo.
    def exitTipo(self, ctx:GramaticaParser.TipoContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_print.
    def enterSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_print.
    def exitSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_if.
    def enterSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_if.
    def exitSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_while.
    def enterSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_while.
    def exitSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        pass


    # Enter a parse tree produced by GramaticaParser#sentencia_for.
    def enterSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        pass

    # Exit a parse tree produced by GramaticaParser#sentencia_for.
    def exitSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        pass


    # Enter a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def enterFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        pass

    # Exit a parse tree produced by GramaticaParser#for_incremento_y_disminucion.
    def exitFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        pass


    # Enter a parse tree produced by GramaticaParser#bloque.
    def enterBloque(self, ctx:GramaticaParser.BloqueContext):
        pass

    # Exit a parse tree produced by GramaticaParser#bloque.
    def exitBloque(self, ctx:GramaticaParser.BloqueContext):
        pass


    # Enter a parse tree produced by GramaticaParser#expr.
    def enterExpr(self, ctx:GramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by GramaticaParser#expr.
    def exitExpr(self, ctx:GramaticaParser.ExprContext):
        pass



del GramaticaParser