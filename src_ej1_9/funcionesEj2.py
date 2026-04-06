def convertir_a_segundos(duracion):
    minutos, segundos =  duracion.split(":")
    return int(minutos) * 60 + int(segundos)
    # Paso las duraciones a segundos para poder comparar ya que estan en formato string

def calcular_duracion_total(playlist):
    total = 0
    for cancion in playlist:
        total += convertir_a_segundos(cancion["duration"])
    return total
    # Voy sumando las duraciones en segundos para saber la duracion total

def convertir_a_min(segundos):
    minutos = segundos // 60
    seg = segundos % 60
    return minutos, seg

def encontrar_mas_larga(playlist):
    return max(playlist, key=lambda c: convertir_a_segundos(c["duration"]))


def encontrar_mas_corta(playlist):
    return min(playlist, key=lambda c: convertir_a_segundos(c["duration"]))
