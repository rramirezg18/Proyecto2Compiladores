# Generated from Gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,209,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,5,0,38,8,0,10,0,12,0,41,
        9,0,1,0,1,0,5,0,45,8,0,10,0,12,0,48,9,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,3,2,63,8,2,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,5,5,90,8,5,10,5,12,5,93,9,5,1,5,1,5,3,5,97,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,3,8,117,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,127,8,10,
        1,10,1,10,1,10,5,10,132,8,10,10,10,12,10,135,9,10,1,10,3,10,138,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,148,8,11,10,11,
        12,11,151,9,11,1,12,1,12,1,12,5,12,156,8,12,10,12,12,12,159,9,12,
        1,13,1,13,1,13,3,13,164,8,13,1,13,1,13,3,13,168,8,13,1,14,1,14,4,
        14,172,8,14,11,14,12,14,173,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,190,8,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,204,8,15,10,15,12,
        15,207,9,15,1,15,0,1,30,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,0,5,1,0,23,26,1,0,21,22,2,0,11,12,14,14,1,0,9,10,1,0,15,20,
        222,0,32,1,0,0,0,2,59,1,0,0,0,4,62,1,0,0,0,6,69,1,0,0,0,8,71,1,0,
        0,0,10,77,1,0,0,0,12,98,1,0,0,0,14,104,1,0,0,0,16,116,1,0,0,0,18,
        118,1,0,0,0,20,122,1,0,0,0,22,141,1,0,0,0,24,152,1,0,0,0,26,160,
        1,0,0,0,28,169,1,0,0,0,30,189,1,0,0,0,32,33,5,27,0,0,33,34,5,33,
        0,0,34,35,5,1,0,0,35,39,5,33,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,
        41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,
        0,42,46,5,34,0,0,43,45,3,20,10,0,44,43,1,0,0,0,45,48,1,0,0,0,46,
        44,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,34,
        0,0,50,51,5,0,0,1,51,1,1,0,0,0,52,60,3,4,2,0,53,60,3,8,4,0,54,60,
        3,10,5,0,55,60,3,12,6,0,56,60,3,14,7,0,57,60,3,18,9,0,58,60,3,26,
        13,0,59,52,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,
        56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,63,3,6,3,
        0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,27,0,0,65,66,
        5,8,0,0,66,67,3,30,15,0,67,68,5,35,0,0,68,5,1,0,0,0,69,70,7,0,0,
        0,70,7,1,0,0,0,71,72,5,6,0,0,72,73,5,31,0,0,73,74,3,30,15,0,74,75,
        5,32,0,0,75,76,5,35,0,0,76,9,1,0,0,0,77,78,5,2,0,0,78,79,5,31,0,
        0,79,80,3,30,15,0,80,81,5,32,0,0,81,91,3,28,14,0,82,83,5,3,0,0,83,
        84,5,2,0,0,84,85,5,31,0,0,85,86,3,30,15,0,86,87,5,32,0,0,87,88,3,
        28,14,0,88,90,1,0,0,0,89,82,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,
        91,92,1,0,0,0,92,96,1,0,0,0,93,91,1,0,0,0,94,95,5,3,0,0,95,97,3,
        28,14,0,96,94,1,0,0,0,96,97,1,0,0,0,97,11,1,0,0,0,98,99,5,4,0,0,
        99,100,5,31,0,0,100,101,3,30,15,0,101,102,5,32,0,0,102,103,3,28,
        14,0,103,13,1,0,0,0,104,105,5,5,0,0,105,106,5,31,0,0,106,107,3,4,
        2,0,107,108,3,30,15,0,108,109,5,35,0,0,109,110,3,16,8,0,110,111,
        5,32,0,0,111,112,3,28,14,0,112,15,1,0,0,0,113,114,5,27,0,0,114,117,
        7,1,0,0,115,117,3,4,2,0,116,113,1,0,0,0,116,115,1,0,0,0,117,17,1,
        0,0,0,118,119,5,7,0,0,119,120,3,30,15,0,120,121,5,35,0,0,121,19,
        1,0,0,0,122,123,3,6,3,0,123,124,5,27,0,0,124,126,5,31,0,0,125,127,
        3,22,11,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,
        5,32,0,0,129,133,5,33,0,0,130,132,3,2,1,0,131,130,1,0,0,0,132,135,
        1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,137,1,0,0,0,135,133,
        1,0,0,0,136,138,3,18,9,0,137,136,1,0,0,0,137,138,1,0,0,0,138,139,
        1,0,0,0,139,140,5,34,0,0,140,21,1,0,0,0,141,142,3,6,3,0,142,149,
        5,27,0,0,143,144,5,36,0,0,144,145,3,6,3,0,145,146,5,27,0,0,146,148,
        1,0,0,0,147,143,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,23,1,0,0,0,151,149,1,0,0,0,152,157,3,30,15,0,153,154,
        5,36,0,0,154,156,3,30,15,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,
        1,0,0,0,157,158,1,0,0,0,158,25,1,0,0,0,159,157,1,0,0,0,160,161,5,
        27,0,0,161,163,5,31,0,0,162,164,3,24,12,0,163,162,1,0,0,0,163,164,
        1,0,0,0,164,165,1,0,0,0,165,167,5,32,0,0,166,168,5,35,0,0,167,166,
        1,0,0,0,167,168,1,0,0,0,168,27,1,0,0,0,169,171,5,33,0,0,170,172,
        3,2,1,0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,1,0,0,0,173,174,
        1,0,0,0,174,175,1,0,0,0,175,176,5,34,0,0,176,29,1,0,0,0,177,178,
        6,15,-1,0,178,179,5,10,0,0,179,190,3,30,15,7,180,181,5,31,0,0,181,
        182,3,30,15,0,182,183,5,32,0,0,183,190,1,0,0,0,184,190,3,26,13,0,
        185,190,5,27,0,0,186,190,5,28,0,0,187,190,5,29,0,0,188,190,5,30,
        0,0,189,177,1,0,0,0,189,180,1,0,0,0,189,184,1,0,0,0,189,185,1,0,
        0,0,189,186,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,205,1,0,
        0,0,191,192,10,11,0,0,192,193,5,13,0,0,193,204,3,30,15,11,194,195,
        10,10,0,0,195,196,7,2,0,0,196,204,3,30,15,11,197,198,10,9,0,0,198,
        199,7,3,0,0,199,204,3,30,15,10,200,201,10,8,0,0,201,202,7,4,0,0,
        202,204,3,30,15,9,203,191,1,0,0,0,203,194,1,0,0,0,203,197,1,0,0,
        0,203,200,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,
        0,206,31,1,0,0,0,207,205,1,0,0,0,18,39,46,59,62,91,96,116,126,133,
        137,149,157,163,167,173,189,203,205
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main()'", "'if'", "'else'", "'while'", 
                     "'for'", "'print'", "'return'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'^'", "'%'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'++'", "'--'", "'int'", "'float'", 
                     "'boolean'", "'string'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "MAIN", "IF", "ELSE", "WHILE", "FOR", 
                      "PRINT", "RETURN", "ASIGNACION", "MAS", "MENOS", "MULTIPLICACION", 
                      "DIVISION", "POTENCIA", "MOD", "IGUAL", "DIFERENTE", 
                      "MENOR", "MAYOR", "MENOR_IGUAL_QUE", "MAYOR_IGUAL_QUE", 
                      "MASMAS", "MENOSMENOS", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "VARIABLE", "NUMERO", "CADENA", "BOOLEANO", 
                      "PARENTESIS_APERTURA", "PARENTESIS_CIERRE", "LLAVE_APERTURA", 
                      "LLAVE_CIERRE", "FIN_DE_LINEA", "COMA", "WS", "COMENTARIO_LINEA", 
                      "COMENTARIO_MULTILINEA" ]

    RULE_gramatica = 0
    RULE_instruccion = 1
    RULE_declaracion_y_asignacion = 2
    RULE_tipo = 3
    RULE_sentencia_print = 4
    RULE_sentencia_if = 5
    RULE_sentencia_while = 6
    RULE_sentencia_for = 7
    RULE_for_incremento_y_disminucion = 8
    RULE_sentencia_return = 9
    RULE_funcion = 10
    RULE_parametros = 11
    RULE_argumentos = 12
    RULE_llamada_funcion = 13
    RULE_bloque = 14
    RULE_expr = 15

    ruleNames =  [ "gramatica", "instruccion", "declaracion_y_asignacion", 
                   "tipo", "sentencia_print", "sentencia_if", "sentencia_while", 
                   "sentencia_for", "for_incremento_y_disminucion", "sentencia_return", 
                   "funcion", "parametros", "argumentos", "llamada_funcion", 
                   "bloque", "expr" ]

    EOF = Token.EOF
    MAIN=1
    IF=2
    ELSE=3
    WHILE=4
    FOR=5
    PRINT=6
    RETURN=7
    ASIGNACION=8
    MAS=9
    MENOS=10
    MULTIPLICACION=11
    DIVISION=12
    POTENCIA=13
    MOD=14
    IGUAL=15
    DIFERENTE=16
    MENOR=17
    MAYOR=18
    MENOR_IGUAL_QUE=19
    MAYOR_IGUAL_QUE=20
    MASMAS=21
    MENOSMENOS=22
    INT=23
    FLOAT=24
    BOOLEAN=25
    STRING=26
    VARIABLE=27
    NUMERO=28
    CADENA=29
    BOOLEANO=30
    PARENTESIS_APERTURA=31
    PARENTESIS_CIERRE=32
    LLAVE_APERTURA=33
    LLAVE_CIERRE=34
    FIN_DE_LINEA=35
    COMA=36
    WS=37
    COMENTARIO_LINEA=38
    COMENTARIO_MULTILINEA=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GramaticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def LLAVE_APERTURA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.LLAVE_APERTURA)
            else:
                return self.getToken(GramaticaParser.LLAVE_APERTURA, i)

        def MAIN(self):
            return self.getToken(GramaticaParser.MAIN, 0)

        def LLAVE_CIERRE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.LLAVE_CIERRE)
            else:
                return self.getToken(GramaticaParser.LLAVE_CIERRE, i)

        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.FuncionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.FuncionContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_gramatica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGramatica" ):
                listener.enterGramatica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGramatica" ):
                listener.exitGramatica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGramatica" ):
                return visitor.visitGramatica(self)
            else:
                return visitor.visitChildren(self)




    def gramatica(self):

        localctx = GramaticaParser.GramaticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_gramatica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(GramaticaParser.VARIABLE)
            self.state = 33
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 34
            self.match(GramaticaParser.MAIN)
            self.state = 35
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 260047092) != 0):
                self.state = 36
                self.instruccion()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(GramaticaParser.LLAVE_CIERRE)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 43
                self.funcion()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(GramaticaParser.LLAVE_CIERRE)
            self.state = 50
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion_y_asignacion(self):
            return self.getTypedRuleContext(GramaticaParser.Declaracion_y_asignacionContext,0)


        def sentencia_print(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_printContext,0)


        def sentencia_if(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_ifContext,0)


        def sentencia_while(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_whileContext,0)


        def sentencia_for(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_forContext,0)


        def sentencia_return(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_returnContext,0)


        def llamada_funcion(self):
            return self.getTypedRuleContext(GramaticaParser.Llamada_funcionContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = GramaticaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.declaracion_y_asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.sentencia_print()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.sentencia_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.sentencia_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.sentencia_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.sentencia_return()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.llamada_funcion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracion_y_asignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def ASIGNACION(self):
            return self.getToken(GramaticaParser.ASIGNACION, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def tipo(self):
            return self.getTypedRuleContext(GramaticaParser.TipoContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_declaracion_y_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion_y_asignacion" ):
                listener.enterDeclaracion_y_asignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion_y_asignacion" ):
                listener.exitDeclaracion_y_asignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion_y_asignacion" ):
                return visitor.visitDeclaracion_y_asignacion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion_y_asignacion(self):

        localctx = GramaticaParser.Declaracion_y_asignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion_y_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 61
                self.tipo()


            self.state = 64
            self.match(GramaticaParser.VARIABLE)
            self.state = 65
            self.match(GramaticaParser.ASIGNACION)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(GramaticaParser.FIN_DE_LINEA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def FLOAT(self):
            return self.getToken(GramaticaParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(GramaticaParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = GramaticaParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(GramaticaParser.PRINT, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_print" ):
                listener.enterSentencia_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_print" ):
                listener.exitSentencia_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_print" ):
                return visitor.visitSentencia_print(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_print(self):

        localctx = GramaticaParser.Sentencia_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sentencia_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(GramaticaParser.PRINT)
            self.state = 72
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 73
            self.expr(0)
            self.state = 74
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 75
            self.match(GramaticaParser.FIN_DE_LINEA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.IF)
            else:
                return self.getToken(GramaticaParser.IF, i)

        def PARENTESIS_APERTURA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_APERTURA)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_APERTURA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def PARENTESIS_CIERRE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.PARENTESIS_CIERRE)
            else:
                return self.getToken(GramaticaParser.PARENTESIS_CIERRE, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.BloqueContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.ELSE)
            else:
                return self.getToken(GramaticaParser.ELSE, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_if" ):
                listener.enterSentencia_if(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_if" ):
                listener.exitSentencia_if(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_if" ):
                return visitor.visitSentencia_if(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_if(self):

        localctx = GramaticaParser.Sentencia_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sentencia_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(GramaticaParser.IF)
            self.state = 78
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 79
            self.expr(0)
            self.state = 80
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 81
            self.bloque()
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.match(GramaticaParser.ELSE)
                    self.state = 83
                    self.match(GramaticaParser.IF)
                    self.state = 84
                    self.match(GramaticaParser.PARENTESIS_APERTURA)
                    self.state = 85
                    self.expr(0)
                    self.state = 86
                    self.match(GramaticaParser.PARENTESIS_CIERRE)
                    self.state = 87
                    self.bloque() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 94
                self.match(GramaticaParser.ELSE)
                self.state = 95
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GramaticaParser.WHILE, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_while" ):
                listener.enterSentencia_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_while" ):
                listener.exitSentencia_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_while" ):
                return visitor.visitSentencia_while(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_while(self):

        localctx = GramaticaParser.Sentencia_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GramaticaParser.WHILE)
            self.state = 99
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 102
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GramaticaParser.FOR, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def declaracion_y_asignacion(self):
            return self.getTypedRuleContext(GramaticaParser.Declaracion_y_asignacionContext,0)


        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def for_incremento_y_disminucion(self):
            return self.getTypedRuleContext(GramaticaParser.For_incremento_y_disminucionContext,0)


        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_for" ):
                listener.enterSentencia_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_for" ):
                listener.exitSentencia_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_for" ):
                return visitor.visitSentencia_for(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_for(self):

        localctx = GramaticaParser.Sentencia_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GramaticaParser.FOR)
            self.state = 105
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 106
            self.declaracion_y_asignacion()
            self.state = 107
            self.expr(0)
            self.state = 108
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 109
            self.for_incremento_y_disminucion()
            self.state = 110
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 111
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_incremento_y_disminucionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def MASMAS(self):
            return self.getToken(GramaticaParser.MASMAS, 0)

        def MENOSMENOS(self):
            return self.getToken(GramaticaParser.MENOSMENOS, 0)

        def declaracion_y_asignacion(self):
            return self.getTypedRuleContext(GramaticaParser.Declaracion_y_asignacionContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_for_incremento_y_disminucion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_incremento_y_disminucion" ):
                listener.enterFor_incremento_y_disminucion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_incremento_y_disminucion" ):
                listener.exitFor_incremento_y_disminucion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_incremento_y_disminucion" ):
                return visitor.visitFor_incremento_y_disminucion(self)
            else:
                return visitor.visitChildren(self)




    def for_incremento_y_disminucion(self):

        localctx = GramaticaParser.For_incremento_y_disminucionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_for_incremento_y_disminucion)
        self._la = 0 # Token type
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(GramaticaParser.VARIABLE)
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.declaracion_y_asignacion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GramaticaParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_return" ):
                listener.enterSentencia_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_return" ):
                listener.exitSentencia_return(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_return" ):
                return visitor.visitSentencia_return(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_return(self):

        localctx = GramaticaParser.Sentencia_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_sentencia_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(GramaticaParser.RETURN)
            self.state = 119
            self.expr(0)
            self.state = 120
            self.match(GramaticaParser.FIN_DE_LINEA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(GramaticaParser.TipoContext,0)


        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def LLAVE_APERTURA(self):
            return self.getToken(GramaticaParser.LLAVE_APERTURA, 0)

        def LLAVE_CIERRE(self):
            return self.getToken(GramaticaParser.LLAVE_CIERRE, 0)

        def parametros(self):
            return self.getTypedRuleContext(GramaticaParser.ParametrosContext,0)


        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def sentencia_return(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_returnContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = GramaticaParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.tipo()
            self.state = 123
            self.match(GramaticaParser.VARIABLE)
            self.state = 124
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 125
                self.parametros()


            self.state = 128
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 129
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 130
                    self.instruccion() 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 136
                self.sentencia_return()


            self.state = 139
            self.match(GramaticaParser.LLAVE_CIERRE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.TipoContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.TipoContext,i)


        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.VARIABLE)
            else:
                return self.getToken(GramaticaParser.VARIABLE, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = GramaticaParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.tipo()
            self.state = 142
            self.match(GramaticaParser.VARIABLE)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 143
                self.match(GramaticaParser.COMA)
                self.state = 144
                self.tipo()
                self.state = 145
                self.match(GramaticaParser.VARIABLE)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = GramaticaParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.expr(0)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 153
                self.match(GramaticaParser.COMA)
                self.state = 154
                self.expr(0)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def argumentos(self):
            return self.getTypedRuleContext(GramaticaParser.ArgumentosContext,0)


        def FIN_DE_LINEA(self):
            return self.getToken(GramaticaParser.FIN_DE_LINEA, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada_funcion" ):
                return visitor.visitLlamada_funcion(self)
            else:
                return visitor.visitChildren(self)




    def llamada_funcion(self):

        localctx = GramaticaParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_llamada_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(GramaticaParser.VARIABLE)
            self.state = 161
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4160750592) != 0):
                self.state = 162
                self.argumentos()


            self.state = 165
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 166
                self.match(GramaticaParser.FIN_DE_LINEA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_APERTURA(self):
            return self.getToken(GramaticaParser.LLAVE_APERTURA, 0)

        def LLAVE_CIERRE(self):
            return self.getToken(GramaticaParser.LLAVE_CIERRE, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = GramaticaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 171 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 170
                self.instruccion()
                self.state = 173 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 260047092) != 0)):
                    break

            self.state = 175
            self.match(GramaticaParser.LLAVE_CIERRE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(GramaticaParser.MENOS, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

        def llamada_funcion(self):
            return self.getTypedRuleContext(GramaticaParser.Llamada_funcionContext,0)


        def VARIABLE(self):
            return self.getToken(GramaticaParser.VARIABLE, 0)

        def NUMERO(self):
            return self.getToken(GramaticaParser.NUMERO, 0)

        def CADENA(self):
            return self.getToken(GramaticaParser.CADENA, 0)

        def BOOLEANO(self):
            return self.getToken(GramaticaParser.BOOLEANO, 0)

        def POTENCIA(self):
            return self.getToken(GramaticaParser.POTENCIA, 0)

        def MULTIPLICACION(self):
            return self.getToken(GramaticaParser.MULTIPLICACION, 0)

        def DIVISION(self):
            return self.getToken(GramaticaParser.DIVISION, 0)

        def MOD(self):
            return self.getToken(GramaticaParser.MOD, 0)

        def MAS(self):
            return self.getToken(GramaticaParser.MAS, 0)

        def MAYOR(self):
            return self.getToken(GramaticaParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(GramaticaParser.MENOR, 0)

        def MAYOR_IGUAL_QUE(self):
            return self.getToken(GramaticaParser.MAYOR_IGUAL_QUE, 0)

        def MENOR_IGUAL_QUE(self):
            return self.getToken(GramaticaParser.MENOR_IGUAL_QUE, 0)

        def IGUAL(self):
            return self.getToken(GramaticaParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(GramaticaParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 178
                self.match(GramaticaParser.MENOS)
                self.state = 179
                self.expr(7)
                pass

            elif la_ == 2:
                self.state = 180
                self.match(GramaticaParser.PARENTESIS_APERTURA)
                self.state = 181
                self.expr(0)
                self.state = 182
                self.match(GramaticaParser.PARENTESIS_CIERRE)
                pass

            elif la_ == 3:
                self.state = 184
                self.llamada_funcion()
                pass

            elif la_ == 4:
                self.state = 185
                self.match(GramaticaParser.VARIABLE)
                pass

            elif la_ == 5:
                self.state = 186
                self.match(GramaticaParser.NUMERO)
                pass

            elif la_ == 6:
                self.state = 187
                self.match(GramaticaParser.CADENA)
                pass

            elif la_ == 7:
                self.state = 188
                self.match(GramaticaParser.BOOLEANO)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 203
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 192
                        self.match(GramaticaParser.POTENCIA)
                        self.state = 193
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 195
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 22528) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 196
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 198
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 199
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 201
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 202
                        self.expr(9)
                        pass

             
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




