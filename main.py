import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from tabla_simbolos import TablaSimbolos
from listener import AnalizadorSemantico
from constructor_ast import ASTconstructor
from generador_ir import IRgenerador
from visitor import AnalizadorVisitor
import llvmlite.binding as llvm #permite aplicar optimizaciones 

class MiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error sintáctico en línea {line}:{column} - {msg}")#errores de sintaxis

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_entrada> [archivo_salida]")#archivo entrada y salida
        return
    
    #errores de sintaxis
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

    #análisis Semántico
    tabla_simbolos = TablaSimbolos()
    analizador = AnalizadorSemantico(tabla_simbolos)
    walker = ParseTreeWalker()
    
    try:
        walker.walk(analizador, tree)
    except Exception as e:
        print(f"Error semántico:\n{e}")
        return
    
    #analiza los visitor para resolver las expresiones y mostrar los resultados
    Analizador = AnalizadorVisitor()
    try:
        Analizador.visit(tree)
    except Exception as e:
        print(f"Error durante evaluación:\n{e}")
        return
    
    #construcción del AST 
    ast_constructor = ASTconstructor()
    ast = ast_constructor.visit(tree)
    
    #generación de LLVM IR a partir del AST sin optimización
    ir_generador = IRgenerador(ast, tabla_simbolos)
    try:
        modulo_llvm = ir_generador.generar()
        output_file = sys.argv[2] if len(sys.argv) > 2 else "output.ll"
        with open(output_file, "w") as f:
            f.write(str(modulo_llvm))
        print(f"Compilación finalizada. Código LLVM IR generado en {output_file}")
    except Exception as e:
        print(f"Error durante la generación de código:\n{e}")
        return

    #aplicar optimizaciones al codigo intermedio generado
    try:
        # Inicializar llvmlite.binding
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
        #convertir el módulo generado a una cadena
        llvm_ir = str(modulo_llvm)
        #parsear el IR a un módulo LLVM
        llvm_mod = llvm.parse_assembly(llvm_ir)
        llvm_mod.verify()
        
        #crear un pass manager para el módulo
        pmb = llvm.PassManagerBuilder()
        pmb.opt_level = 2   #nivel -O2  podemos cambiar el nivel que queramooos
        pm = llvm.ModulePassManager()
        pmb.populate(pm)
        pm.run(llvm_mod)

        
        optimized_ir = str(llvm_mod)
        opt_file = "output_opt.ll"
        with open(opt_file, "w") as f:
            f.write(optimized_ir)
        print(f"Código LLVM IR optimizado generado en {opt_file}")
    except Exception as e:
        print(f"Error durante la optimización del módulo LLVM IR:\n{e}")

if __name__ == '__main__':
    main()
