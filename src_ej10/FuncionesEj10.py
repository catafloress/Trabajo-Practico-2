def sumar_puntajes(jueces):
    return sum(jueces.values())
    # Suma los puntajes de los jueces para cada participante

def actualizar_resultados(resultados, nombre, suma):
    resultados[nombre]['total'] += suma
    if suma > resultados[nombre]['mejor']:
        resultados[nombre]['mejor'] = suma
    # Actualiza el total y el mejor puntaje del participante

def procesar_ronda(ronda, resultados):
    puntajes_ronda = {}
    for nombre, jueces in ronda['scores'].items():
        suma = sum(jueces.values())
        puntajes_ronda[nombre] = suma
        actualizar_resultados(resultados, nombre, suma)
    
    ganador = max(puntajes_ronda, key=puntajes_ronda.get)
    resultados[ganador]['ganadas'] += 1
    return puntajes_ronda, ganador
    # Informa el ganador y los puntajes de cada participante en la ronda

def mostrar_tabla_parcial(resultados):
    for nombre,datos in resultados.items():
        print(nombre,datos['total'])

def mostrar_tabla_final(resultados,rondas):
    ordenados = sorted(resultados.items(), key=lambda x:x[1]['total'], reverse=True)
    print("\nTabla final:")
    for nombre, datos in ordenados:
        promedio = datos['total'] / len(rondas)
        print(nombre,datos['total'], datos['ganadas'], datos['mejor'], round(promedio, 1))
        # Imprime la tabla final ordenada por puntaje total con el promedio redondeado a 1 decimal.