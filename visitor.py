from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser

class AnalizadorVisitor(GramaticaVisitor):
    def __init__(self):
        self.env = {}  # Entorno para almacenar variables

    def visitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        # Si se incluye tipo, es declaración
        if ctx.tipo() is not None:
            if var_name in self.env:
                raise Exception(f"Variable {var_name} ya está declarada.")
            self.env[var_name] = value
        else:
            # Es reasignación; la variable debe haber sido declarada previamente
            if var_name not in self.env:
                raise Exception(f"Variable {var_name} no está declarada.")
            self.env[var_name] = value
        return value

    def visitSentencia_print(self, ctx: GramaticaParser.Sentencia_printContext):
        value = self.visit(ctx.expr())
        if isinstance(value, float):
            print(f"{value:.1f}")
        else:
            print(value)
        return value

    def visitSentencia_if(self, ctx: GramaticaParser.Sentencia_ifContext):
        # Primera condición y bloque
        if self.visit(ctx.expr(0)):
            return self.visit(ctx.bloque(0))
        # Revisa posibles "else if"
        numCondiciones = len(ctx.expr())
        for i in range(1, numCondiciones):
            if self.visit(ctx.expr(i)):
                return self.visit(ctx.bloque(i))
        # Revisa el "else"
        if ctx.ELSE() and len(ctx.bloque()) > numCondiciones:
            return self.visit(ctx.bloque(numCondiciones))
        return None

    def visitSentencia_while(self, ctx: GramaticaParser.Sentencia_whileContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
        return None

    def visitSentencia_for(self, ctx: GramaticaParser.Sentencia_forContext):
        # Estructura del for: for (inicialización ; condición ; incremento) bloque
        self.visit(ctx.declaracion_y_asignacion())  # Inicialización
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
            self.visit(ctx.for_incremento_y_disminucion())
        return None

    def visitFor_incremento_y_disminucion(self, ctx: GramaticaParser.For_incremento_y_disminucionContext):
        # Puede ser VARIABLE con MASMAS/MENOSMENOS o una declaracion_y_asignacion
        if ctx.getChildCount() == 2:
            var_name = ctx.VARIABLE().getText()
            if ctx.MASMAS():
                if var_name in self.env:
                    self.env[var_name] += 1
                else:
                    raise Exception(f"Variable no definida: {var_name}")
            elif ctx.MENOSMENOS():
                if var_name in self.env:
                    self.env[var_name] -= 1
                else:
                    raise Exception(f"Variable no definida: {var_name}")
        else:
            # Caso en el que se utilice la regla declaracion_y_asignacion
            return self.visit(ctx.declaracion_y_asignacion())
        return None

    def visitBloque(self, ctx: GramaticaParser.BloqueContext):
        result = None
        for instr in ctx.instruccion():
            result = self.visit(instr)
        return result

    def visitExpr(self, ctx: GramaticaParser.ExprContext):
        # Manejo del operador unario negativo
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            expr_value = self.visit(ctx.expr(0))
            return -expr_value if expr_value is not None else 0

        if ctx.getChildCount() == 1:
            token_text = ctx.getText()
            try:
                return float(token_text)
            except ValueError:
                if token_text in self.env:
                    return self.env[token_text]
                elif token_text.startswith('"') and token_text.endswith('"'):
                    return token_text[1:-1]
                elif token_text == "true":
                    return True
                elif token_text == "false":
                    return False
                else:
                    raise Exception("Variable no definida o valor inválido: " + token_text)

        elif ctx.getChildCount() == 3:
            # Caso de paréntesis o de operación binaria
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                return self.visit(ctx.expr(0))
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right
            elif op == '/':
                return left / right
            elif op == '^':
                return left ** right
            elif op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '<':
                return left < right
            elif op == '>':
                return left > right
            elif op == '<=':
                return left <= right
            elif op == '>=':
                return left >= right
            else:
                raise Exception("Operador desconocido: " + op)
        return self.visitChildren(ctx)
