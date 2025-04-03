#construccion del ast a partir de GramaticaVisitor.py

from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser


#definición de nodos del AST en clases


class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, main, functions):
        self.main = main
        self.functions = functions

class Main(ASTNode):
    def __init__(self, instructions):
        self.instructions = instructions

class Function(ASTNode):
    def __init__(self, ret_type, name, params, instructions, return_expr=None):
        self.ret_type = ret_type
        self.name = name
        self.params = params  #lista de tuplas tipo y nombre
        self.instructions = instructions
        self.return_expr = return_expr

class Declaration(ASTNode):
    def __init__(self, var_type, var_name, expr):
        self.var_type = var_type  #puede ser None si se infiere
        self.var_name = var_name
        self.expr = expr

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class If(ASTNode):
    def __init__(self, cond, then_block, else_block=None, elif_blocks=None):
        self.cond = cond
        self.then_block = then_block
        self.else_block = else_block
        self.elif_blocks = elif_blocks if elif_blocks is not None else []

class While(ASTNode):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class For(ASTNode):
    def __init__(self, init, cond, inc, body):
        self.init = init
        self.cond = cond
        self.inc = inc
        self.body = body

class Return(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class FuncCall(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class Block(ASTNode):
    def __init__(self, instructions):
        self.instructions = instructions

class BinaryOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

class Literal(ASTNode):
    def __init__(self, value, lit_type):
        self.value = value
        self.lit_type = lit_type  # 'int', 'float', 'boolean', 'string'

class Variable(ASTNode):
    def __init__(self, name):
        self.name = name


#visitor para construir el AST
class ASTconstructor(GramaticaVisitor):
    def visitGramatica(self, ctx:GramaticaParser.GramaticaContext):
        main_ast = self.visit(ctx.main())
        functions = [self.visit(func) for func in ctx.funcion()]
        return Program(main_ast, functions)

    def visitMain(self, ctx:GramaticaParser.MainContext):
        instructions = [self.visit(instr) for instr in ctx.instruccion()]
        return Main(instructions)

    def visitInstruccion(self, ctx:GramaticaParser.InstruccionContext):
        if ctx.declaracion_y_asignacion():
            return self.visit(ctx.declaracion_y_asignacion())
        elif ctx.sentencia_print():
            return self.visit(ctx.sentencia_print())
        elif ctx.sentencia_if():
            return self.visit(ctx.sentencia_if())
        elif ctx.sentencia_while():
            return self.visit(ctx.sentencia_while())
        elif ctx.sentencia_for():
            return self.visit(ctx.sentencia_for())
        elif ctx.sentencia_return():
            return self.visit(ctx.sentencia_return())
        elif ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())
        else:
            return None

    def visitDeclaracion_y_asignacion(self, ctx:GramaticaParser.Declaracion_y_asignacionContext):
        var_type = self.visit(ctx.tipo()) if ctx.tipo() else None
        var_name = ctx.VARIABLE().getText()
        expr = self.visit(ctx.expr())
        return Declaration(var_type, var_name, expr)

    def visitTipo(self, ctx:GramaticaParser.TipoContext):
        return ctx.getText()

    def visitSentencia_print(self, ctx:GramaticaParser.Sentencia_printContext):
        expr = self.visit(ctx.expr())
        return Print(expr)

    def visitSentencia_if(self, ctx:GramaticaParser.Sentencia_ifContext):
        #if (expr) bloque (ELSE IF (expr) bloque)* (ELSE bloque)?
        cond = self.visit(ctx.expr(0))
        then_block = self.visit(ctx.bloque(0))
        #else if se recolectan a partir de los expr y bloques adicionales.
        elif_blocks = []
        for i in range(1, len(ctx.expr())):
            cond_elif = self.visit(ctx.expr(i))
            elif_block = self.visit(ctx.bloque(i))
            elif_blocks.append((cond_elif, elif_block))
        #si hay else, estará presente en ctx.ELSE()
        else_block = self.visit(ctx.bloque(len(ctx.bloque()) - 1)) if ctx.ELSE() else None
        return If(cond, then_block, else_block, elif_blocks)

    def visitSentencia_while(self, ctx:GramaticaParser.Sentencia_whileContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.bloque())
        return While(cond, body)

    def visitSentencia_for(self, ctx:GramaticaParser.Sentencia_forContext):
        init = self.visit(ctx.declaracion_y_asignacion())
        cond = self.visit(ctx.expr())
        inc = self.visit(ctx.for_incremento_y_disminucion())
        body = self.visit(ctx.bloque())
        return For(init, cond, inc, body)

    def visitFor_incremento_y_disminucion(self, ctx:GramaticaParser.For_incremento_y_disminucionContext):
        #VARIABLE (MASMAS | MENOSMENOS) o una reasignación
        if ctx.MASMAS() or ctx.MENOSMENOS():
            var_name = ctx.VARIABLE().getText()
            op = ctx.MASMAS().getText() if ctx.MASMAS() else ctx.MENOSMENOS().getText()
            return UnaryOp(op, Variable(var_name))
        else:
            return self.visit(ctx.declaracion_y_asignacion())

    def visitSentencia_return(self, ctx:GramaticaParser.Sentencia_returnContext):
        expr = self.visit(ctx.expr())
        return Return(expr)

    def visitFuncion(self, ctx:GramaticaParser.FuncionContext):
        ret_type = self.visit(ctx.tipo())
        func_name = ctx.VARIABLE().getText()
        params = self.visit(ctx.parametros()) if ctx.parametros() else []
        instructions = [self.visit(instr) for instr in ctx.instruccion()]
        #si se incluye sentencia_return en la función se procesa aparte
        return_expr = self.visit(ctx.sentencia_return()) if ctx.sentencia_return() else None
        return Function(ret_type, func_name, params, instructions, return_expr)

    def visitParametros(self, ctx:GramaticaParser.ParametrosContext):
        params = []
        #tipo VARIABLE (COMA tipo VARIABLE)*
        params.append((ctx.tipo(0).getText(), ctx.VARIABLE(0).getText()))
        for i in range(1, len(ctx.tipo())):
            params.append((ctx.tipo(i).getText(), ctx.VARIABLE(i).getText()))
        return params

    def visitArgumentos(self, ctx:GramaticaParser.ArgumentosContext):
        args = []
        for expr in ctx.expr():
            args.append(self.visit(expr))
        return args

    def visitLlamada_funcion(self, ctx:GramaticaParser.Llamada_funcionContext):
        func_name = ctx.VARIABLE().getText()
        args = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        return FuncCall(func_name, args)

    def visitBloque(self, ctx:GramaticaParser.BloqueContext):
        instructions = [self.visit(instr) for instr in ctx.instruccion()]
        return Block(instructions)

    def visitExpr(self, ctx:GramaticaParser.ExprContext):
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if ctx.llamada_funcion():
                return self.visit(ctx.llamada_funcion())
            if text in ['true', 'false']:
                return Literal(True if text == 'true' else False, 'boolean')
            elif text.startswith('"'):
                return Literal(text[1:-1], 'string')
            elif text.isdigit():
                return Literal(int(text), 'int')
            try:
                if '.' in text:
                    return Literal(float(text), 'float')
            except:
                pass
            return Variable(text)
        elif ctx.getChildCount() == 3:
            #puede ser una expresión entre paréntesis o una operación binaria
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.expr(0))
            else:
                left = self.visit(ctx.expr(0))
                op = ctx.getChild(1).getText()
                right = self.visit(ctx.expr(1))
                return BinaryOp(left, op, right)
        elif ctx.getChildCount() == 2:
            op = ctx.getChild(0).getText()
            operand = self.visit(ctx.expr(0))
            return UnaryOp(op, operand)
        return None