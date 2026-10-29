
# EJERCICIO AUTOMATA

def analizar_token(cadena):
    cadena = cadena.strip()
    if not cadena:
        return "Cadena vacía"
        
    # Palabras reservadas
    palabras_reservadas = {
        "inicio", "fin", "entero", "real", "cadena",
        "booleano", "leer", "mostrar", "si", "sino",
        "mientras", "verdadero", "falso", "Y", "O", "NO"
    }
    
    estado = 0
    i = 0
    operadores = {'+', '-', '*', '/', '=', '<', '>', '%'}
    while i < len(cadena):
        c = cadena[i]
        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1 # Estado para Identificador o Palabra reservada
            elif c.isdigit():
                estado = 2 # Estado para Número (Entero)
            elif c in operadores:
                estado = 4 # Estado para Operador
            else:
                return "No válido / Desconocido"
        elif estado == 1: # Procesando Identificador
            if not (c.isalnum() or c == '_'):
                return "Identificador no válido"
        elif estado == 2: # Procesando Número Entero
            if c == '.':
                estado = 3 # Transición a número decimal
            elif not c.isdigit():
                return "Número no válido"
        elif estado == 3: # Procesando parte decimal
            if not c.isdigit():
                return "Número decimal no válido"
        elif estado == 4: # Procesando Operador
            return "Operador no válido (demasiados caracteres)"
        i += 1
    # Clasificación final según el estado en el que terminó
    if estado == 1:
        if cadena in palabras_reservadas:
            return "Palabra reservada válida"
        return "Identificador válido"
    elif estado == 2:
        return "Número entero válido"
    elif estado == 3:
        if cadena.endswith('.'):
            return "Número real no válido"
        return "Número real válido"
    elif estado == 4:
        return "Operador válido"
        
    return "Cadena no válida"""


# --- Pruebas ---
entradas = ["inicio", "verdadero", "variable1+", "125", "45.67", "+", "_contador", "99num", "++"]
for e in entradas:
    print(f"'{e}' -> {analizar_token(e)}")
