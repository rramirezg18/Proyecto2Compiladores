import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from listener import ValidacionListener
from codegen_visitor import CodeGenVisitor

# Clase para errores de sintaxis
class MiErrorListener(ErrorListener):
    def __init__(self):
        super(MiErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = (
            f"\nError en la sintaxis\n"
            f"Línea {line}, Columna {column}\n"
            f"Token problemático: '{offendingSymbol.text if offendingSymbol else 'N/A'}'\n"
            f"Mensaje: {msg}\n"
        )
        raise Exception(error_msg)

def main(argv):
    if len(argv) < 2:
        print("Uso: python3 main.py <archivo>")
        return

    input_file = argv[1]
    # Leer el archivo de entrada
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = GramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramaticaParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MiErrorListener())

    try:
        tree = parser.gramatica()
    except Exception as e:
        print("Error de parseo:", e)
        return

    # Primera pasada: Validación semántica
    validacion_listener = ValidacionListener()
    walker = ParseTreeWalker()
    try:
        walker.walk(validacion_listener, tree)
    except Exception as e:
        print("Error de validación semántica:", e)
        return

    # Segunda pasada: Generación de código intermedio (LLVM IR)
    codegen_visitor = CodeGenVisitor()
    try:
        ir_code = codegen_visitor.visit(tree)
    except Exception as e:
        print("Error durante la generación de IR:", e)
        return

    # Escribir el IR generado en un archivo, por ejemplo, "output.ll"
    output_filename = "output.ll"
    try:
        with open(output_filename, "w") as f:
            f.write(ir_code)
        print(f"Código LLVM IR generado y guardado en {output_filename}")
    except Exception as e:
        print("Error al escribir el archivo de salida:", e)

if __name__ == '__main__':
    main(sys.argv)
