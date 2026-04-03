def cantidad_total_de_lineas (text):
    return len(text.split("\n"))

def cantidad_total_de_palabras (text):
    return len(text.split( ))

def calcular_promedio(cantidad_lineas, cantidad_palabras):
    return cantidad_palabras / cantidad_lineas

def lineas_por_encima_del_promedio (text, promedio):
    palabras_por_linea = []
    lineas = text.split("\n")
    for linea in lineas: 
        cant_palabras_por_linea = len(linea.split())
        if cant_palabras_por_linea > promedio: 
            palabras_por_linea.append((linea, cant_palabras_por_linea))
    return palabras_por_linea