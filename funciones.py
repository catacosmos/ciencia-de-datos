def promedio(datos):
datos = [x for x in datos if x == x]
  return sum(datos) / len(datos)


def mediana(datos):
  ordenado = sorted(datos)
  n = len(ordenado)
  if n % 2 == 0:
      medio_izquierdo = ordenado[n // 2 - 1]
      medio_derecho = ordenado[n // 2]
      mediana = (medio_izquierdo + medio_derecho) / 2
  else:
      mediana = ordenado[n // 2]
  return mediana


def moda(datos):
  categorias_unicas = set(datos)
  frecuencias = {categoria: datos.count(categoria) for categoria in categorias_unicas}
  max_frecuencia = max(frecuencias.values())
  moda = [categoria for categoria, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
  return moda


def rango(datos):
  return max(datos) - min(datos)


def frecuencia_abs(datos):
  frecuencia = {}
  for elemento in datos:
    if elemento in frecuencia:
        frecuencia[elemento] += 1
    else:
        frecuencia[elemento] = 1
  return frecuencia


def varianza(datos):
  promedio = sum(datos) / len(datos)
  suma_cuadrados = sum((x - promedio) ** 2 for x in datos)
  return suma_cuadrados / (len(datos) - 1)


def desviación(datos):
  promedio = sum(datos) / len(datos)
  suma_cuadrados = sum((x - promedio) ** 2 for x in datos)
  varianza = suma_cuadrados / (len(datos) - 1)
  return varianza ** 0.5


def cuartiles(datos):
  ordenado = sorted(datos)
  n = len(ordenado)
  q1 = ordenado[n // 4] if n % 4 != 0 else (ordenado[n // 4 - 1] + ordenado[n // 4]) / 2
  q3 = ordenado[n // 4 * 3] if n % 4 != 0 else (ordenado[n // 4 * 3 - 1] + ordenado[n // 4 * 3]) / 2
  return q3 - q1
def percentil(datos, percentil):
    """
    Calcula un percentil específico de un conjunto de datos sin usar NumPy.

    Parámetros:
    datos (list): Una lista de datos numéricos.
    percentil (int): El percentil que se desea calcular.

    Retorna:
    float: El valor del percentil especificado.
    """
    datos_ordenados = sorted(datos)
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
  ordenado = sorted(datos)
  n = len(ordenado)
  mediana = ordenado[n // 2] if n % 2 != 0 else (ordenado[n // 2 - 1] + ordenado[n // 2]) / 2
  diferencias_absolutas = [abs(x - mediana) for x in ordenado]
  n = len(diferencias_absolutas)
  if n % 2 != 0:
    mediana_abs = sorted(diferencias_absolutas)[n // 2]
  else:
    median_abs = (sorted(diferencias_absolutas)[n // 2 - 1] + sorted(diferencias_absolutas)[n // 2]) / 2
  return mediana_abs


