import random

def generar_lista_aleatoria(n=10):
    """Genera una lista de n elementos aleatorios entre 1 y 100"""
    return [random.randint(1, 100) for _ in range(n)]

def ordenamiento_burbuja(lista):
    """Ordena la lista usando el método de burbuja y cuenta las iteraciones"""
    iteraciones = 0
    arr = lista.copy()  # Copiar para no modificar la original
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            iteraciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr, iteraciones

def ordenamiento_insercion(lista):
    """Ordena la lista usando el método de inserción y cuenta las iteraciones"""
    iteraciones = 0
    arr = lista.copy()  # Copiar para no modificar la original
    
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        
        while j >= 0 and clave < arr[j]:
            iteraciones += 1
            arr[j + 1] = arr[j]
            j -= 1
        
        iteraciones += 1  # Contar la última comparación
        arr[j + 1] = clave
    
    return arr, iteraciones

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*50)
    print("MENÚ DE ORDENAMIENTO")
    print("="*50)
    print("1. Generar nueva lista aleatoria")
    print("2. Ordenar con Método Burbuja")
    print("3. Ordenar con Método de Inserción")
    print("4. Comparar ambos métodos")
    print("5. Salir")
    print("="*50)

def main():
    lista_original = generar_lista_aleatoria()
    print("\n¡Bienvenido al Comparador de Algoritmos de Ordenamiento!")
    print(f"\nLista inicial generada: {lista_original}")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            lista_original = generar_lista_aleatoria()
            print(f"\n✓ Nueva lista generada: {lista_original}")
        
        elif opcion == "2":
            print(f"\nLista original: {lista_original}")
            lista_ordenada, iteraciones = ordenamiento_burbuja(lista_original)
            print(f"Lista ordenada (Burbuja): {lista_ordenada}")
            print(f"Iteraciones realizadas: {iteraciones}")
        
        elif opcion == "3":
            print(f"\nLista original: {lista_original}")
            lista_ordenada, iteraciones = ordenamiento_insercion(lista_original)
            print(f"Lista ordenada (Inserción): {lista_ordenada}")
            print(f"Iteraciones realizadas: {iteraciones}")
        
        elif opcion == "4":
            print(f"\nLista original: {lista_original}")
            print("\n--- COMPARACIÓN DE ALGORITMOS ---")
            
            # Ordenar con burbuja
            lista_burbuja, iteraciones_burbuja = ordenamiento_burbuja(lista_original)
            print(f"\n✓ Método Burbuja:")
            print(f"  Lista ordenada: {lista_burbuja}")
            print(f"  Iteraciones: {iteraciones_burbuja}")
            
            # Ordenar con inserción
            lista_insercion, iteraciones_insercion = ordenamiento_insercion(lista_original)
            print(f"\n✓ Método de Inserción:")
            print(f"  Lista ordenada: {lista_insercion}")
            print(f"  Iteraciones: {iteraciones_insercion}")
            
            # Comparar
            print("\n--- RESULTADO ---")
            if iteraciones_burbuja < iteraciones_insercion:
                print(f"🏆 El método Burbuja usó menos iteraciones: {iteraciones_burbuja} vs {iteraciones_insercion}")
                diferencia = iteraciones_insercion - iteraciones_burbuja
                print(f"   Diferencia: {diferencia} iteraciones")
            elif iteraciones_insercion < iteraciones_burbuja:
                print(f"🏆 El método de Inserción usó menos iteraciones: {iteraciones_insercion} vs {iteraciones_burbuja}")
                diferencia = iteraciones_burbuja - iteraciones_insercion
                print(f"   Diferencia: {diferencia} iteraciones")
            else:
                print(f"⚖️  Ambos métodos usaron la misma cantidad de iteraciones: {iteraciones_burbuja}")
        
        elif opcion == "5":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            break
        
        else:
            print("\n❌ Opción inválida. Por favor, seleccione un número entre 1 y 5.")

if __name__ == "__main__":
    main()
