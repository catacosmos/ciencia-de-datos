def moda(datos):
    categorias_unicas = set(datos)
    frecuencias = {categoria: datos.count(categoria) for categoria in categorias_unicas}
    max_frecuencia = max(frecuencias.values())
    moda = [categoria for categoria, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
    return moda
