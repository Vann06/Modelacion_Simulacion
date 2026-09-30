import heapq


def heuristica(ciudad):
    valores = {
        "A": 7,
        "B": 6,
        "C": 4,
        "D": 2,
        "E": 1,
        "F": 0
    }

    return valores[ciudad]


def a_estrella(grafo, inicio, meta):

    cola = []

    heapq.heappush(cola, (0, inicio))

    costos = {inicio: 0}

    padres = {inicio: None}

    while cola:

        _, actual = heapq.heappop(cola)

        if actual == meta:
            break

        for vecino, costo in grafo[actual]:

            nuevo_costo = costos[actual] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:

                costos[vecino] = nuevo_costo

                prioridad = nuevo_costo + heuristica(vecino)

                heapq.heappush(
                    cola,
                    (prioridad, vecino)
                )

                padres[vecino] = actual

    ruta = []

    ciudad = meta

    while ciudad is not None:

        ruta.append(ciudad)

        ciudad = padres[ciudad]

    ruta.reverse()

    return ruta, costos[meta]


def ejecutar():

    grafo = {

        "A": [("B", 2), ("C", 4)],

        "B": [("A", 2), ("D", 5), ("C", 1)],

        "C": [("A", 4), ("B", 1), ("D", 2)],

        "D": [("B", 5), ("C", 2), ("E", 2)],

        "E": [("D", 2), ("F", 1)],

        "F": []
    }

    print("\n--- A* - Ruta entre ciudades ---")

    print("Ciudades disponibles: A, B, C, D, E, F")

    inicio = "A"

    destino = "F"

    ruta, costo = a_estrella(
        grafo,
        inicio,
        destino
    )

    print("\nCiudad inicial:", inicio)

    print("Destino:", destino)

    print("\nMejor ruta encontrada:")

    print(" -> ".join(ruta))

    print("\nCosto total:", costo)