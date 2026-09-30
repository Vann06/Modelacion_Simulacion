from algoritmos import astar
from algoritmos import hill_climbing
from algoritmos import flujo_min_costo


def mostrar_menu():
    print("\n==============================")
    print("   ALGORITMOS DE BÚSQUEDA")
    print("==============================")
    print("1. A* - Ruta entre ciudades")
    print("2. Hill Climbing - Producción óptima")
    print("3. Flujo Máximo - Costo Mínimo")
    print("4. Salir")
    print("==============================")


def main():

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            astar.ejecutar()

        elif opcion == "2":
            hill_climbing.ejecutar()

        elif opcion == "3":
            flujo_min_costo.ejecutar()

        elif opcion == "4":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()