class TablaSimbolos:
    def __init__(self):
        # Iniciamos con un entorno global para las variables
        self.env_stack = [{}]
    
        self.funciones = {} #para funciones almacena el nombre y sus parámetros y tipo de retorno

    # Métodos de entornos
    def current_env(self):
        return self.env_stack[-1]

    def push_env(self):
        self.env_stack.append({})

    def pop_env(self):
        if len(self.env_stack) == 1:
            raise Exception("No se puede eliminar el entorno global.")
        self.env_stack.pop()

    # control de variables
    def agregar_variable(self, nombre, tipo):
        if nombre in self.current_env():
            raise Exception(f"Error semántico: La variable '{nombre}' ya está declarada en este ámbito.")
        self.current_env()[nombre] = tipo

    def consultar_variable(self, nombre):
        # Busca en los entornos de forma inversa logal o global
        for env in reversed(self.env_stack):
            if nombre in env:
                return env[nombre]
        raise Exception(f"Error semántico: La variable '{nombre}' no está declarada.")

    def existe_variable(self, nombre):
        try:
            self.consultar_variable(nombre)
            return True
        except Exception:
            return False

    # control de funciones
    def agregar_funcion(self, nombre, tipo_retorno, parametros):
        if nombre in self.funciones:
            raise Exception(f"Error semántico: La función '{nombre}' ya está definida.")
        self.funciones[nombre] = {"tipo_retorno": tipo_retorno, "parametros": parametros}

    def consultar_funcion(self, nombre):
        if nombre not in self.funciones:
            raise Exception(f"Error semántico: La función '{nombre}' no está definida.")
        return self.funciones[nombre]

    def existe_funcion(self, nombre):
        return nombre in self.funciones
