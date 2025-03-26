import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from visitor import AnalizadorVisitor

#  para errores de sintaxis
class ErrorListener(ErrorListener):
    def __init__(self):
        super(ErrorListener, self).__init__()
    # caputa los errores en sintaxis
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error sintáctico en la línea {line}, columna {column}: {msg}")

def main(argv):
    if len(argv) < 2:#valida que se pase el archivo
        print("Uso: python3 main.py <archivo>")
        return
    #lee el archivo.txt
    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")
    #lexer y tokens
    lexer = GramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramaticaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ErrorListener())

    try:
        tree = parser.gramatica()
    except Exception as e:
        print("Error de parseo:", e)
        return

    visitor = AnalizadorVisitor()
    try:
        visitor.visit(tree)
    except Exception as e:
        print("Error durante la evaluación:", e)

if __name__ == '__main__':
    main(sys.argv)