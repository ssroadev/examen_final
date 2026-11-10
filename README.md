# Comparador de Algoritmos de Ordenamiento

Programa en Python que compara dos algoritmos de ordenamiento: **Método Burbuja** y **Método de Inserción**.

## Características

- ✅ Genera lista aleatoria de 10 elementos (números entre 1 y 100)
- ✅ Menú interactivo con 5 opciones
- ✅ Implementa dos métodos de ordenamiento:
  - **Ordenamiento Burbuja (Bubble Sort)**
  - **Ordenamiento por Inserción (Insertion Sort)**
- ✅ Cuenta las iteraciones de cada algoritmo
- ✅ Compara y muestra cuál algoritmo es más eficiente

## Requisitos

- Python 3.6 o superior

## Uso

Para ejecutar el programa:

```bash
python ordenamiento.py
```

## Menú del Programa

1. **Generar nueva lista aleatoria** - Crea una nueva lista de 10 elementos aleatorios
2. **Ordenar con Método Burbuja** - Ordena la lista actual usando el algoritmo de burbuja
3. **Ordenar con Método de Inserción** - Ordena la lista actual usando el algoritmo de inserción
4. **Comparar ambos métodos** - Ejecuta ambos algoritmos y compara el número de iteraciones
5. **Salir** - Termina el programa

## Ejemplo de Salida

```
Lista original: [45, 12, 89, 3, 67, 23, 91, 56, 34, 78]

--- COMPARACIÓN DE ALGORITMOS ---

✓ Método Burbuja:
  Lista ordenada: [3, 12, 23, 34, 45, 56, 67, 78, 89, 91]
  Iteraciones: 45

✓ Método de Inserción:
  Lista ordenada: [3, 12, 23, 34, 45, 56, 67, 78, 89, 91]
  Iteraciones: 28

--- RESULTADO ---
🏆 El método de Inserción usó menos iteraciones: 28 vs 45
   Diferencia: 17 iteraciones
```

## Algoritmos Implementados

### Ordenamiento Burbuja
Compara elementos adyacentes y los intercambia si están en el orden incorrecto. El proceso se repite hasta que la lista está ordenada.

**Complejidad:** O(n²) en el peor caso

### Ordenamiento por Inserción
Construye la lista ordenada de forma incremental, insertando cada elemento en su posición correcta.

**Complejidad:** O(n²) en el peor caso, pero puede ser más eficiente en listas parcialmente ordenadas

## Autor

Proyecto creado para parcial de Lógica de Programación
