import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from tabla_simbolos import TablaSimbolos
from listener import AnalizadorSemantico
from generadorIR_visitor import GeneradorCodigo
from visitor import AnalizadorVisitor

class MiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error sintáctico en línea {line}:{column} - {msg}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_entrada>")
        return

    # Análisis Léxico/Sintáctico
    input_stream = FileStream(sys.argv[1])
    lexer = GramaticaLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MiErrorListener())
    
    tokens = CommonTokenStream(lexer)
    parser = GramaticaParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(MiErrorListener())
    
    try:
        tree = parser.gramatica()
    except Exception as e:
        print(f"Error durante el parsing:\n{e}")
        return

    # Análisis Semántico
    tabla_simbolos = TablaSimbolos()
    analizador = AnalizadorSemantico(tabla_simbolos)
    walker = ParseTreeWalker()
    
    try:
        walker.walk(analizador, tree)
    except Exception as e:
        print(f"Error semántico:\n{e}")
        return
    #valida las operaciones y las muestra en pantalla antes de mostrar el mensaje de compilacion exitosa
    Analizador = AnalizadorVisitor()
    try:
        Analizador.visit(tree)  # Esto ejecutará los prints y mostrará los valores
    except Exception as e:
        print(f"Error durante evaluación:\n{e}")
        return
    
    # Después del análisis semántico
    #print("Variables registradas:", tabla_simbolos.entornos)
    #print("Contenido real:", [e for e in dir(tabla_simbolos) if not e.startswith('__')])

    # Generación de Código
    generador = GeneradorCodigo(tabla_simbolos)
    #print("Tabla de símbolos a usar:", generador.ts.entornos)  # <-- Ahora después de crear generador

    try:
        modulo_llvm = generador.visit(tree)
        with open("output.ll", "w") as f:
            f.write(str(modulo_llvm))
        print("Compilación finalizada. Código LLVM IR generado en output.ll")
    except Exception as e:
        print(f"Error durante la generación de código:\n{e}")

if __name__ == '__main__':
    main()
