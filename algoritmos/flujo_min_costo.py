import heapq


class Arista:

    def __init__(
        self,
        destino,
        capacidad,
        costo,
        reversa
    ):

        self.destino = destino

        self.capacidad = capacidad

        self.costo = costo

        self.reversa = reversa


class GrafoFlujo:

    def __init__(self, n):

        self.n = n

        self.grafo = [
            [] for _ in range(n)
        ]


    def agregar_arista(
        self,
        origen,
        destino,
        capacidad,
        costo
    ):

        directa = Arista(
            destino,
            capacidad,
            costo,
            len(self.grafo[destino])
        )

        inversa = Arista(
            origen,
            0,
            -costo,
            len(self.grafo[origen])
        )

        self.grafo[origen].append(
            directa
        )

        self.grafo[destino].append(
            inversa
        )


    def flujo_maximo_costo_minimo(
        self,
        origen,
        destino
    ):

        flujo_total = 0

        costo_total = 0

        while True:

            distancia = [
                float("inf")
            ] * self.n

            padre_nodo = [
                -1
            ] * self.n

            padre_arista = [
                -1
            ] * self.n

            distancia[origen] = 0

            cola = [
                (0, origen)
            ]

            while cola:

                dist_actual, nodo = heapq.heappop(
                    cola
                )

                if dist_actual != distancia[nodo]:
                    continue

                for i, arista in enumerate(
                    self.grafo[nodo]
                ):

                    if (
                        arista.capacidad > 0
                        and
                        distancia[arista.destino]
                        >
                        distancia[nodo]
                        + arista.costo
                    ):

                        distancia[
                            arista.destino
                        ] = (
                            distancia[nodo]
                            + arista.costo
                        )

                        padre_nodo[
                            arista.destino
                        ] = nodo

                        padre_arista[
                            arista.destino
                        ] = i

                        heapq.heappush(
                            cola,
                            (
                                distancia[
                                    arista.destino
                                ],
                                arista.destino
                            )
                        )

            if distancia[destino] == float("inf"):
                break

            flujo = float("inf")

            nodo = destino

            while nodo != origen:

                anterior = padre_nodo[nodo]

                indice = padre_arista[nodo]

                flujo = min(
                    flujo,
                    self.grafo[
                        anterior
                    ][indice].capacidad
                )

                nodo = anterior

            nodo = destino

            while nodo != origen:

                anterior = padre_nodo[nodo]

                indice = padre_arista[nodo]

                arista = self.grafo[
                    anterior
                ][indice]

                arista.capacidad -= flujo

                self.grafo[
                    nodo
                ][
                    arista.reversa
                ].capacidad += flujo

                nodo = anterior

            flujo_total += flujo

            costo_total += (
                flujo
                * distancia[destino]
            )

        return flujo_total, costo_total


def ejecutar():

    print(
        "\n--- Flujo Máximo - Costo Mínimo ---"
    )

    # Nodos
    # 0 = Centro de distribución
    # 1 = Ruta Norte
    # 2 = Ruta Sur
    # 3 = Destino

    red = GrafoFlujo(4)

    red.agregar_arista(
        0,
        1,
        8,
        2
    )

    red.agregar_arista(
        0,
        2,
        6,
        1
    )

    red.agregar_arista(
        1,
        3,
        8,
        3
    )

    red.agregar_arista(
        2,
        3,
        6,
        2
    )

    flujo, costo = (
        red.flujo_maximo_costo_minimo(
            0,
            3
        )
        
    )

    print(
        "\nCantidad máxima de paquetes enviados:",
        flujo
    )

    print(
        "Costo mínimo total:",
        costo
    )