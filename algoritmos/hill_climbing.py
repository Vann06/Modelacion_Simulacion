def ganancia(x):

    return -(x - 10) ** 2 + 100


def hill_climbing(inicio):

    actual = inicio

    historial = []

    while True:

        historial.append(
            (actual, ganancia(actual))
        )

        izquierda = actual - 1

        derecha = actual + 1

        ganancia_actual = ganancia(actual)

        ganancia_izquierda = ganancia(izquierda)

        ganancia_derecha = ganancia(derecha)

        if ganancia_derecha > ganancia_actual:

            actual = derecha

        elif ganancia_izquierda > ganancia_actual:

            actual = izquierda

        else:

            break

    return actual, ganancia(actual), historial


def ejecutar():

    print("\n--- Hill Climbing - Producción óptima ---")

    inicio = 3

    mejor_produccion, mejor_ganancia, historial = hill_climbing(
        inicio
    )

    print("\nProducción inicial:", inicio)

    print("\nProceso de búsqueda:")

    for produccion, beneficio in historial:

        print(
            "Producción:",
            produccion,
            "| Ganancia:",
            beneficio
        )

    print("\nResultado:")

    print(
        "Mejor cantidad de producción:",
        mejor_produccion
    )

    print(
        "Ganancia máxima:",
        mejor_ganancia
    )