#tabla de simbolos para el control de tipos, funciones y variables

class TablaSimbolos:
    def __init__(self):
        self.entornos = [{}]  # Pila de entornos
        self.funciones = {}    # Diccionario de funciones
        self.current_return_type = None

    #manejo de entornos
    def push_env(self):
        self.entornos.append({})

    def pop_env(self):
        if len(self.entornos) > 1:
            self.entornos.pop()

    def current_env(self):#entorno actual
        return self.entornos[-1]

    #controla las vriables
    def agregar_variable(self, nombre, tipo):
        if nombre in self.current_env():
            raise Exception(f"Variable '{nombre}' ya declarada en este ámbito")
        self.current_env()[nombre] = tipo

    def consultar_variable(self, nombre):
        for env in reversed(self.entornos):
            if nombre in env:
                return env[nombre]
        raise Exception(f"Variable '{nombre}' no declarada")

    def existe_variable(self, nombre):
        try:
            self.consultar_variable(nombre)
            return True
        except:
            return False

    #controla las funciones
    def agregar_funcion(self, nombre, tipo_retorno, parametros):
        if nombre in self.funciones:
            raise Exception(f"Función '{nombre}' ya definida")
        self.funciones[nombre] = {
            'tipo_retorno': tipo_retorno,
            'parametros': parametros
        }

    def consultar_funcion(self, nombre):
        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no definida")
        return self.funciones[nombre]

    def existe_funcion(self, nombre):
        return nombre in self.funciones

    #validacion de tipos
    def tipos_compatibles(self, target_type, expr_type):
        if target_type == expr_type:
            return True
        if target_type == "float" and expr_type == "int":
            return True
        return False