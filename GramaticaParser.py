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
        4,1,39,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,5,0,39,8,0,10,0,12,
        0,42,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,
        9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,66,8,2,1,3,3,3,69,8,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,96,8,6,10,6,12,6,99,9,
        6,1,6,1,6,3,6,103,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,123,8,9,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,3,11,133,8,11,1,11,1,11,1,11,5,11,138,8,11,10,
        11,12,11,141,9,11,1,11,3,11,144,8,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,5,12,154,8,12,10,12,12,12,157,9,12,1,13,1,13,1,13,5,
        13,162,8,13,10,13,12,13,165,9,13,1,14,1,14,1,14,3,14,170,8,14,1,
        14,1,14,3,14,174,8,14,1,15,1,15,4,15,178,8,15,11,15,12,15,179,1,
        15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,3,16,196,8,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,5,16,210,8,16,10,16,12,16,213,9,16,1,16,0,1,32,17,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,5,1,0,23,26,1,0,21,
        22,2,0,11,12,14,14,1,0,9,10,1,0,15,20,227,0,34,1,0,0,0,2,46,1,0,
        0,0,4,65,1,0,0,0,6,68,1,0,0,0,8,75,1,0,0,0,10,77,1,0,0,0,12,83,1,
        0,0,0,14,104,1,0,0,0,16,110,1,0,0,0,18,122,1,0,0,0,20,124,1,0,0,
        0,22,128,1,0,0,0,24,147,1,0,0,0,26,158,1,0,0,0,28,166,1,0,0,0,30,
        175,1,0,0,0,32,195,1,0,0,0,34,35,5,27,0,0,35,36,5,33,0,0,36,40,3,
        2,1,0,37,39,3,22,11,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,
        40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,44,5,34,0,0,44,45,5,
        0,0,1,45,1,1,0,0,0,46,47,5,1,0,0,47,48,5,31,0,0,48,49,5,32,0,0,49,
        53,5,33,0,0,50,52,3,4,2,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,34,0,0,57,
        3,1,0,0,0,58,66,3,6,3,0,59,66,3,10,5,0,60,66,3,12,6,0,61,66,3,14,
        7,0,62,66,3,16,8,0,63,66,3,20,10,0,64,66,3,28,14,0,65,58,1,0,0,0,
        65,59,1,0,0,0,65,60,1,0,0,0,65,61,1,0,0,0,65,62,1,0,0,0,65,63,1,
        0,0,0,65,64,1,0,0,0,66,5,1,0,0,0,67,69,3,8,4,0,68,67,1,0,0,0,68,
        69,1,0,0,0,69,70,1,0,0,0,70,71,5,27,0,0,71,72,5,8,0,0,72,73,3,32,
        16,0,73,74,5,35,0,0,74,7,1,0,0,0,75,76,7,0,0,0,76,9,1,0,0,0,77,78,
        5,6,0,0,78,79,5,31,0,0,79,80,3,32,16,0,80,81,5,32,0,0,81,82,5,35,
        0,0,82,11,1,0,0,0,83,84,5,2,0,0,84,85,5,31,0,0,85,86,3,32,16,0,86,
        87,5,32,0,0,87,97,3,30,15,0,88,89,5,3,0,0,89,90,5,2,0,0,90,91,5,
        31,0,0,91,92,3,32,16,0,92,93,5,32,0,0,93,94,3,30,15,0,94,96,1,0,
        0,0,95,88,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,102,
        1,0,0,0,99,97,1,0,0,0,100,101,5,3,0,0,101,103,3,30,15,0,102,100,
        1,0,0,0,102,103,1,0,0,0,103,13,1,0,0,0,104,105,5,4,0,0,105,106,5,
        31,0,0,106,107,3,32,16,0,107,108,5,32,0,0,108,109,3,30,15,0,109,
        15,1,0,0,0,110,111,5,5,0,0,111,112,5,31,0,0,112,113,3,6,3,0,113,
        114,3,32,16,0,114,115,5,35,0,0,115,116,3,18,9,0,116,117,5,32,0,0,
        117,118,3,30,15,0,118,17,1,0,0,0,119,120,5,27,0,0,120,123,7,1,0,
        0,121,123,3,6,3,0,122,119,1,0,0,0,122,121,1,0,0,0,123,19,1,0,0,0,
        124,125,5,7,0,0,125,126,3,32,16,0,126,127,5,35,0,0,127,21,1,0,0,
        0,128,129,3,8,4,0,129,130,5,27,0,0,130,132,5,31,0,0,131,133,3,24,
        12,0,132,131,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,5,32,
        0,0,135,139,5,33,0,0,136,138,3,4,2,0,137,136,1,0,0,0,138,141,1,0,
        0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,143,1,0,0,0,141,139,1,0,
        0,0,142,144,3,20,10,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,
        0,0,0,145,146,5,34,0,0,146,23,1,0,0,0,147,148,3,8,4,0,148,155,5,
        27,0,0,149,150,5,36,0,0,150,151,3,8,4,0,151,152,5,27,0,0,152,154,
        1,0,0,0,153,149,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,25,1,0,0,0,157,155,1,0,0,0,158,163,3,32,16,0,159,160,
        5,36,0,0,160,162,3,32,16,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,
        1,0,0,0,163,164,1,0,0,0,164,27,1,0,0,0,165,163,1,0,0,0,166,167,5,
        27,0,0,167,169,5,31,0,0,168,170,3,26,13,0,169,168,1,0,0,0,169,170,
        1,0,0,0,170,171,1,0,0,0,171,173,5,32,0,0,172,174,5,35,0,0,173,172,
        1,0,0,0,173,174,1,0,0,0,174,29,1,0,0,0,175,177,5,33,0,0,176,178,
        3,4,2,0,177,176,1,0,0,0,178,179,1,0,0,0,179,177,1,0,0,0,179,180,
        1,0,0,0,180,181,1,0,0,0,181,182,5,34,0,0,182,31,1,0,0,0,183,184,
        6,16,-1,0,184,185,5,10,0,0,185,196,3,32,16,7,186,187,5,31,0,0,187,
        188,3,32,16,0,188,189,5,32,0,0,189,196,1,0,0,0,190,196,3,28,14,0,
        191,196,5,27,0,0,192,196,5,28,0,0,193,196,5,29,0,0,194,196,5,30,
        0,0,195,183,1,0,0,0,195,186,1,0,0,0,195,190,1,0,0,0,195,191,1,0,
        0,0,195,192,1,0,0,0,195,193,1,0,0,0,195,194,1,0,0,0,196,211,1,0,
        0,0,197,198,10,11,0,0,198,199,5,13,0,0,199,210,3,32,16,11,200,201,
        10,10,0,0,201,202,7,2,0,0,202,210,3,32,16,11,203,204,10,9,0,0,204,
        205,7,3,0,0,205,210,3,32,16,10,206,207,10,8,0,0,207,208,7,4,0,0,
        208,210,3,32,16,9,209,197,1,0,0,0,209,200,1,0,0,0,209,203,1,0,0,
        0,209,206,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,
        0,212,33,1,0,0,0,213,211,1,0,0,0,18,40,53,65,68,97,102,122,132,139,
        143,155,163,169,173,179,195,209,211
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'if'", "'else'", "'while'", 
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
    RULE_main = 1
    RULE_instruccion = 2
    RULE_declaracion_y_asignacion = 3
    RULE_tipo = 4
    RULE_sentencia_print = 5
    RULE_sentencia_if = 6
    RULE_sentencia_while = 7
    RULE_sentencia_for = 8
    RULE_for_incremento_y_disminucion = 9
    RULE_sentencia_return = 10
    RULE_funcion = 11
    RULE_parametros = 12
    RULE_argumentos = 13
    RULE_llamada_funcion = 14
    RULE_bloque = 15
    RULE_expr = 16

    ruleNames =  [ "gramatica", "main", "instruccion", "declaracion_y_asignacion", 
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

        def LLAVE_APERTURA(self):
            return self.getToken(GramaticaParser.LLAVE_APERTURA, 0)

        def main(self):
            return self.getTypedRuleContext(GramaticaParser.MainContext,0)


        def LLAVE_CIERRE(self):
            return self.getToken(GramaticaParser.LLAVE_CIERRE, 0)

        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)

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
            self.state = 34
            self.match(GramaticaParser.VARIABLE)
            self.state = 35
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 36
            self.main()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 37
                self.funcion()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(GramaticaParser.LLAVE_CIERRE)
            self.state = 44
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(GramaticaParser.MAIN, 0)

        def PARENTESIS_APERTURA(self):
            return self.getToken(GramaticaParser.PARENTESIS_APERTURA, 0)

        def PARENTESIS_CIERRE(self):
            return self.getToken(GramaticaParser.PARENTESIS_CIERRE, 0)

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
            return GramaticaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = GramaticaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GramaticaParser.MAIN)
            self.state = 47
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 48
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 49
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 260047092) != 0):
                self.state = 50
                self.instruccion()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(GramaticaParser.LLAVE_CIERRE)
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
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.declaracion_y_asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.sentencia_print()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.sentencia_if()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.sentencia_while()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.sentencia_for()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.sentencia_return()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
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
        self.enterRule(localctx, 6, self.RULE_declaracion_y_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 67
                self.tipo()


            self.state = 70
            self.match(GramaticaParser.VARIABLE)
            self.state = 71
            self.match(GramaticaParser.ASIGNACION)
            self.state = 72
            self.expr(0)
            self.state = 73
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
        self.enterRule(localctx, 8, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
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
        self.enterRule(localctx, 10, self.RULE_sentencia_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(GramaticaParser.PRINT)
            self.state = 78
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 79
            self.expr(0)
            self.state = 80
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 81
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
        self.enterRule(localctx, 12, self.RULE_sentencia_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
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
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.match(GramaticaParser.ELSE)
                    self.state = 89
                    self.match(GramaticaParser.IF)
                    self.state = 90
                    self.match(GramaticaParser.PARENTESIS_APERTURA)
                    self.state = 91
                    self.expr(0)
                    self.state = 92
                    self.match(GramaticaParser.PARENTESIS_CIERRE)
                    self.state = 93
                    self.bloque() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 100
                self.match(GramaticaParser.ELSE)
                self.state = 101
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
        self.enterRule(localctx, 14, self.RULE_sentencia_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GramaticaParser.WHILE)
            self.state = 105
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 106
            self.expr(0)
            self.state = 107
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 108
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
        self.enterRule(localctx, 16, self.RULE_sentencia_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GramaticaParser.FOR)
            self.state = 111
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 112
            self.declaracion_y_asignacion()
            self.state = 113
            self.expr(0)
            self.state = 114
            self.match(GramaticaParser.FIN_DE_LINEA)
            self.state = 115
            self.for_incremento_y_disminucion()
            self.state = 116
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 117
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
        self.enterRule(localctx, 18, self.RULE_for_incremento_y_disminucion)
        self._la = 0 # Token type
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.match(GramaticaParser.VARIABLE)
                self.state = 120
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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
        self.enterRule(localctx, 20, self.RULE_sentencia_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(GramaticaParser.RETURN)
            self.state = 125
            self.expr(0)
            self.state = 126
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
        self.enterRule(localctx, 22, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.tipo()
            self.state = 129
            self.match(GramaticaParser.VARIABLE)
            self.state = 130
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 131
                self.parametros()


            self.state = 134
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 135
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 136
                    self.instruccion() 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 142
                self.sentencia_return()


            self.state = 145
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
        self.enterRule(localctx, 24, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.tipo()
            self.state = 148
            self.match(GramaticaParser.VARIABLE)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 149
                self.match(GramaticaParser.COMA)
                self.state = 150
                self.tipo()
                self.state = 151
                self.match(GramaticaParser.VARIABLE)
                self.state = 157
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
        self.enterRule(localctx, 26, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.expr(0)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 159
                self.match(GramaticaParser.COMA)
                self.state = 160
                self.expr(0)
                self.state = 165
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
        self.enterRule(localctx, 28, self.RULE_llamada_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(GramaticaParser.VARIABLE)
            self.state = 167
            self.match(GramaticaParser.PARENTESIS_APERTURA)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4160750592) != 0):
                self.state = 168
                self.argumentos()


            self.state = 171
            self.match(GramaticaParser.PARENTESIS_CIERRE)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 172
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
        self.enterRule(localctx, 30, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(GramaticaParser.LLAVE_APERTURA)
            self.state = 177 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 176
                self.instruccion()
                self.state = 179 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 260047092) != 0)):
                    break

            self.state = 181
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 184
                self.match(GramaticaParser.MENOS)
                self.state = 185
                self.expr(7)
                pass

            elif la_ == 2:
                self.state = 186
                self.match(GramaticaParser.PARENTESIS_APERTURA)
                self.state = 187
                self.expr(0)
                self.state = 188
                self.match(GramaticaParser.PARENTESIS_CIERRE)
                pass

            elif la_ == 3:
                self.state = 190
                self.llamada_funcion()
                pass

            elif la_ == 4:
                self.state = 191
                self.match(GramaticaParser.VARIABLE)
                pass

            elif la_ == 5:
                self.state = 192
                self.match(GramaticaParser.NUMERO)
                pass

            elif la_ == 6:
                self.state = 193
                self.match(GramaticaParser.CADENA)
                pass

            elif la_ == 7:
                self.state = 194
                self.match(GramaticaParser.BOOLEANO)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 209
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 198
                        self.match(GramaticaParser.POTENCIA)
                        self.state = 199
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 201
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 22528) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 202
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 204
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 205
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = GramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 207
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2064384) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expr(9)
                        pass

             
                self.state = 213
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
        self._predicates[16] = self.expr_sempred
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
         




