def promedio(datos):
    """
    Calcula el promedio de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: El promedio de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    return sum(data_sin_nan) / len(data_sin_nan)


def mediana(datos):
    """
    Calcula la mediana de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: La mediana de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    ordenado = sorted(data_sin_nan)
    n = len(ordenado)
    if n % 2 == 0:
        medio_izquierdo = ordenado[n // 2 - 1]
        medio_derecho = ordenado[n // 2]
        mediana = (medio_izquierdo + medio_derecho) / 2
    else:
        mediana = ordenado[n // 2]
    return mediana


def moda(datos):
    """
    Calcula la moda de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    list: Una lista con los modos (puede ser más de uno).
    """
    data_sin_nan = [x for x in datos if x == x]
    categorias_unicas = set(data_sin_nan)
    frecuencias = {categoria: data_sin_nan.count(categoria) for categoria in categorias_unicas}
    max_frecuencia = max(frecuencias.values())
    moda = [categoria for categoria, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
    return moda


def rango(datos):
    """
    Calcula el rango de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: El rango de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    return max(data_sin_nan) - min(data_sin_nan)


def frecuencia_abs(datos):
    """
    Calcula la frecuencia absoluta de cada elemento en una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    dict: Un diccionario donde las claves son los elementos y los valores son sus frecuencias.
    """
    data_sin_nan = [x for x in datos if x == x]
    frecuencia = {}
    for elemento in data_sin_nan:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia


def varianza(datos):
    """
    Calcula la varianza de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: La varianza de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    promedio = sum(data_sin_nan) / len(data_sin_nan)
    suma_cuadrados = sum((x - promedio) ** 2 for x in data_sin_nan)
    return suma_cuadrados / (len(data_sin_nan) - 1)


def desviacion(datos):
    """
    Calcula la desviación estándar de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: La desviación estándar de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    promedio = sum(data_sin_nan) / len(data_sin_nan)
    suma_cuadrados = sum((x - promedio) ** 2 for x in data_sin_nan)
    varianza = suma_cuadrados / (len(data_sin_nan) - 1)
    return varianza ** 0.5


def cuartiles(datos):
    """
    Calcula la diferencia entre el tercer y primer cuartil de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: La diferencia entre el tercer y primer cuartil.
    """
    data_sin_nan = [x for x in datos if x == x]
    ordenado = sorted(data_sin_nan)
    n = len(ordenado)
    q1 = ordenado[n // 4] if n % 4 != 0 else (ordenado[n // 4 - 1] + ordenado[n // 4]) / 2
    q3 = ordenado[n // 4 * 3] if n % 4 != 0 else (ordenado[n // 4 * 3 - 1] + ordenado[n // 4 * 3]) / 2
    return q3 - q1


def percentil(datos, percentil):
    """
    Calcula un percentil específico de un conjunto de datos.
    Parámetros:
    datos (list): Una lista de datos numéricos.
    percentil (int): El percentil que se desea calcular.

    Retorna:
    float: El valor del percentil especificado.
    """
    data_sin_nan = [x for x in datos if x == x]
    datos_ordenados = sorted(data_sin_nan)
    posicion = (percentil / 100) * (len(datos_ordenados) - 1)

    # Si la posición es un entero, el percentil es el dato en esa posición.
    if isinstance(posicion, int):
        return datos_ordenados[int(posicion)]
    else:
        # Si la posición no es un entero, se interpola entre los datos.
        k = int(posicion)
        f = posicion - k
        return (1 - f) * datos_ordenados[k] + f * datos_ordenados[k + 1]


def mediana_abs(datos):
    """
    Calcula la mediana absoluta de una lista de datos.

    Parámetros:
    datos (list): Una lista de datos numéricos.

    Retorna:
    float: La mediana absoluta de los datos.
    """
    data_sin_nan = [x for x in datos if x == x]
    ordenado = sorted(data_sin_nan)
    n = len(ordenado)
    mediana = ordenado[n // 2] if n % 2 != 0 else (ordenado[n // 2 - 1] + ordenado[n // 2]) / 2
    diferencias_absolutas = [abs(x - mediana) for x in ordenado]
    n = len(diferencias_absolutas)
    if n % 2 != 0:
      mediana_abs = sorted(diferencias_absolutas)[n // 2]
    else:
      median_abs = (sorted(diferencias_absolutas)[n // 2 - 1] + sorted(diferencias_absolutas)[n // 2]) / 2
    return mediana_abs


