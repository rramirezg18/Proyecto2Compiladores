from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser

class AnalizadorVisitor(GramaticaVisitor):
    def __init__(self):
        self.env_stack = [{}]  # Pila de entornos
        self.funciones = {}    # Funciones

    # Métodos de manejo de entornos
    def entorno_actual(self):
        return self.env_stack[-1]

    def apilar_entorno(self):
        self.env_stack.append({})

    def desapilar_entorno(self):
        self.env_stack.pop()

    def declarar_variable(self, name, value, vtype):
        if name in self.entorno_actual():
            raise Exception(f"Variable {name} ya está declarada en este ámbito.")
        self.entorno_actual()[name] = (value, vtype)

    def asignar_variable(self, name, value, vtype):
        for env in reversed(self.env_stack):
            if name in env:
                env[name] = (value, vtype)
                return
        raise Exception(f"Variable {name} no definida.")

    def obtener_variable(self, name):
        for env in reversed(self.env_stack):
            if name in env:
                return env[name]
        raise Exception(f"Variable {name} no definida.")

    def visitGramatica(self, ctx: GramaticaParser.GramaticaContext):
        # 1) Registrar todas las funciones
        for funcion in ctx.funcion():
            self.visitFuncion(funcion)

        # 2) Ejecutar las instrucciones principales (en el entorno global)
        result = None
        for instr in ctx.instruccion():
            result = self.visit(instr)
        return result

    # -------------------------------------------------------------------
    # --------------- Declaraciones y asignaciones ----------------------
    # -------------------------------------------------------------------
    def visitDeclaracion_y_asignacion(self, ctx: GramaticaParser.Declaracion_y_asignacionContext):
        var_name = ctx.VARIABLE().getText()
        val, expr_type = self.visit(ctx.expr())

        if ctx.tipo() is not None:
            declared_type = ctx.tipo().getText()
            new_val, final_type = self.check_type_compatibility(val, expr_type, declared_type)
            self.declarar_variable(var_name, new_val, declared_type)
            return (new_val, declared_type)
        else:
            self.asignar_variable(var_name, val, expr_type)
            return (val, expr_type)

    #control de tipos de variables
    #valida si los operandos son del mismo tipo
    def check_type_compatibility(self, val, expr_type, target_type):
        if target_type == expr_type:
            return (val, expr_type)

        if target_type == "float" and expr_type == "int":
            return (float(val), "float")

        raise Exception(f"No se puede asignar {expr_type} a {target_type}.")

    def visitSentencia_print(self, ctx: GramaticaParser.Sentencia_printContext):
        val, val_type = self.visit(ctx.expr())
        
        if val_type in ("float", "int"):
            if val_type == "int":
                print(int(val))
            else:
                print(f"{val:.1f}")
        else:
            print(val)
        
        return None


    def visitSentencia_if(self, ctx: GramaticaParser.Sentencia_ifContext):
        numCondiciones = len(ctx.expr())

        for i in range(numCondiciones):
            cond_val, cond_type = self.visit(ctx.expr(i))
            
            #print(f"Condición {i}: {ctx.expr(i).getText()} -> {cond_val}, tipo {cond_type}")

            if cond_type != "boolean":
                raise Exception(f"Condición en 'if' no es booleana: {ctx.expr(i).getText()}")

            if cond_val:
                return self.visitBloque(ctx.bloque(i), new_scope=False)

        if ctx.ELSE() and len(ctx.bloque()) > numCondiciones:
            return self.visitBloque(ctx.bloque(numCondiciones), new_scope=False)

        return None

    def visitSentencia_while(self, ctx: GramaticaParser.Sentencia_whileContext):
        while True:
            cond_val, cond_type = self.visit(ctx.expr())
            if cond_type != "boolean":
                raise Exception("Condición en 'while' no es booleana.")
            if not cond_val:
                break
            self.visitBloque(ctx.bloque(), new_scope=False)
        return None

    def visitSentencia_for(self, ctx: GramaticaParser.Sentencia_forContext):
        self.visit(ctx.declaracion_y_asignacion())

        while True:
            cond_val, cond_type = self.visit(ctx.expr())
            if cond_type != "boolean":
                raise Exception("Condición en 'for' no es booleana.")
            if not cond_val:
                break
            # Se captura el resultado en el bloque del foooooooooor
            bloque_result = self.visitBloque(ctx.bloque(), new_scope=False)
            if isinstance(bloque_result, tuple) and bloque_result[0] == "return":
                return bloque_result
            self.visit(ctx.for_incremento_y_disminucion())
        return None


    def visitFor_incremento_y_disminucion(self, ctx: GramaticaParser.For_incremento_y_disminucionContext):
        if ctx.getChildCount() == 2:
            var_name = ctx.VARIABLE().getText()
            val, val_type = self.obtener_variable(var_name)
            if val_type not in ("int", "float"):
                raise Exception(f"No se puede aplicar ++/-- a tipo {val_type}.")
            if ctx.MASMAS():
                new_val = val + 1
            else:
                new_val = val - 1
            self.asignar_variable(var_name, new_val, val_type)
        else:
            self.visit(ctx.declaracion_y_asignacion())
        return None

    def visitBloque(self, ctx: GramaticaParser.BloqueContext, new_scope=True):
        if new_scope:
            self.apilar_entorno()
        retorno = None
        for instr in ctx.instruccion():
            resultado = self.visit(instr)
            if isinstance(resultado, tuple) and resultado[0] == "return":
                retorno = resultado
                break
        if new_scope:
            self.desapilar_entorno()
        return retorno

    def visitExpr(self, ctx: GramaticaParser.ExprContext):
        # Si es la alternativa de llamada a función, delega en visitLlamada_funcion.
        if ctx.getChildCount() == 1 and ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())

        # Caso de un solo hijo literal, variable
        if ctx.getChildCount() == 1:
            token_text = ctx.getText()
            if token_text.startswith('"') and token_text.endswith('"'):
                return (token_text[1:-1], "string")
            if token_text == "true":
                return (True, "boolean")
            if token_text == "false":
                return (False, "boolean")
            try:
                if '.' in token_text:
                    return (float(token_text), "float")
                else:
                    return (int(token_text), "int")
            except ValueError:
                return self.obtener_variable(token_text)
        # cuanooo es un numero negativo ejemploo -expr
        elif ctx.getChildCount() == 2:
            if ctx.getChild(0).getText() == '-':
                val, val_type = self.visit(ctx.expr(0))
                if val_type not in ("int", "float"):
                    raise Exception(f"Operador unario '-' no es válido para tipo {val_type}.")
                resultado = (-val, val_type)
            else:
                resultado = self.visitChildren(ctx)
        # Caso de expresiones binarias o paréntesis
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
                resultado = self.visit(ctx.expr(0))
            else:
                left_val, left_type = self.visit(ctx.expr(0))
                right_val, right_type = self.visit(ctx.expr(1))
                op = ctx.getChild(1).getText()
                resultado = self.operacion_binaria(left_val, left_type, right_val, right_type, op)
        else:
            resultado = self.visitChildren(ctx)

        #print(f"visitExpr -> {ctx.getText()} = {resultado}")
        return resultado

    def operacion_binaria(self, left_val, left_type, right_val, right_type, op):
        if op == '^':
            self.revisa_tipos_numericos(left_type, right_type, op)
            final_type = "float" if (left_type == "float" or right_type == "float") else "int"
            return (left_val ** right_val, final_type)
        elif op in ['*', '/', '%']:
            self.revisa_tipos_numericos(left_type, right_type, op)
            # Para '*' y '/' se calcula de forma similar.
            if op == '*':
                result = left_val * right_val
            elif op == '/':
                # Si ambos son int, convertir el resultado a float para evitar división entera
                result = left_val / right_val
            elif op == '%':
                result = left_val % right_val
            # El tipo final es "float" si alguno de los operandos es float; en caso contrario "int".
            final_type = "float" if ('float' in [left_type, right_type]) else "int"
            return (result, final_type)
        elif op in ['+', '-']:
            if op == '+':
                if left_type == "string" and right_type == "string":
                    return (left_val + right_val, "string")
                self.revisa_tipos_numericos(left_type, right_type, op)
                final_type = "float" if ('float' in [left_type, right_type]) else "int"
                return (left_val + right_val, final_type)
            else:
                self.revisa_tipos_numericos(left_type, right_type, op)
                final_type = "float" if ('float' in [left_type, right_type]) else "int"
                return (left_val - right_val, final_type)
        elif op in ['==', '!=', '<', '>', '<=', '>=']:
            if left_type in ["int", "float"] and right_type in ["int", "float"]:
                left_val, right_val = float(left_val), float(right_val)
                if op == '==':
                    return (left_val == right_val, "boolean")
                elif op == '!=':
                    return (left_val != right_val, "boolean")
                elif op == '<':
                    return (left_val < right_val, "boolean")
                elif op == '>':
                    return (left_val > right_val, "boolean")
                elif op == '<=':
                    return (left_val <= right_val, "boolean")
                elif op == '>=':
                    return (left_val >= right_val, "boolean")
            if left_type == right_type:
                if op == '==':
                    return (left_val == right_val, "boolean")
                elif op == '!=':
                    return (left_val != right_val, "boolean")
            raise Exception(f"No se puede comparar {left_type} con {right_type} usando {op}.")
        raise Exception("Operador desconocido: " + op)

    def revisa_tipos_numericos(self, t1, t2, op):
        if t1 not in ("int", "float") or t2 not in ("int", "float"):
            raise Exception(f"Operación '{op}' no válida para tipos {t1} y {t2}.")

    def visitFuncion(self, ctx: GramaticaParser.FuncionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        parametros = self.visit(ctx.parametros()) if ctx.parametros() else []
        instrucciones = ctx.instruccion()
        sentencia_ret = ctx.sentencia_return() if ctx.sentencia_return() else None

        if nombre_funcion in self.funciones:
            raise Exception(f"La función {nombre_funcion} ya está definida.")
        self.funciones[nombre_funcion] = (parametros, instrucciones, sentencia_ret)
        return None

    def visitParametros(self, ctx: GramaticaParser.ParametrosContext):
        parametros = []
        for i in range(len(ctx.tipo())):
            tipo = ctx.tipo(i).getText()
            nombre = ctx.VARIABLE(i).getText()
            parametros.append((tipo, nombre))
        return parametros

    def visitLlamada_funcion(self, ctx: GramaticaParser.Llamada_funcionContext):
        nombre_funcion = ctx.VARIABLE().getText()
        if nombre_funcion not in self.funciones:
            raise Exception(f"Función {nombre_funcion} no definida.")

        parametros_llamada = self.visit(ctx.argumentos()) if ctx.argumentos() else []
        funcion_parametros, instrucciones, sentencia_ret = self.funciones[nombre_funcion]

        if len(parametros_llamada) != len(funcion_parametros):
            raise Exception(f"Cantidad de parámetros incorrecta para {nombre_funcion}.")

        # Guardar el entorno actual y crear uno nuevo para la función
        entorno_anterior = self.env_stack
        self.env_stack = [{}]

        for (tipo_formal, nombre_formal), (val_real, type_real) in zip(funcion_parametros, parametros_llamada):
            val_asignado, final_type = self.check_type_compatibility(val_real, type_real, tipo_formal)
            self.entorno_actual()[nombre_formal] = (val_asignado, final_type)

        retorno = None
        for instr in instrucciones:
            resultado = self.visit(instr)
            if isinstance(resultado, tuple) and resultado[0] == "return":
                retorno = resultado[1]
                break

        if retorno is None and sentencia_ret:
            ret_tuple = self.visit(sentencia_ret)
            if isinstance(ret_tuple, tuple) and ret_tuple[0] == "return":
                retorno = ret_tuple[1]

        self.env_stack = entorno_anterior

        if retorno is None:
            return (None, "void")
        return retorno


    def visitArgumentos(self, ctx: GramaticaParser.ArgumentosContext):
        argumentos = []
        for arg in ctx.expr():
            argumentos.append(self.visit(arg))
        return argumentos

    def visitSentencia_return(self, ctx: GramaticaParser.Sentencia_returnContext):
        val, val_type = self.visit(ctx.expr())
        return ("return", (val, val_type))

  
    def infer_type(self, val):
        if isinstance(val, bool):
            return "boolean"
        elif isinstance(val, int):
            return "int"
        elif isinstance(val, float):
            return "float"
        elif isinstance(val, str):
            return "string"
        elif val is None:
            return "void"
        else:
            return "unknown"
