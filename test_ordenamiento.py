"""
Script de prueba para verificar el funcionamiento del programa
"""
import random
from ordenamiento import generar_lista_aleatoria, ordenamiento_burbuja, ordenamiento_insercion

# Establecer semilla para resultados reproducibles
random.seed(42)

print("="*60)
print("PRUEBA DEL PROGRAMA DE ORDENAMIENTO")
print("="*60)

# Generar lista de prueba
lista = generar_lista_aleatoria()
print(f"\nLista generada: {lista}")

# Probar ordenamiento burbuja
print("\n--- Prueba Ordenamiento Burbuja ---")
resultado_burbuja, iteraciones_burbuja = ordenamiento_burbuja(lista)
print(f"Lista ordenada: {resultado_burbuja}")
print(f"Iteraciones: {iteraciones_burbuja}")

# Probar ordenamiento inserción
print("\n--- Prueba Ordenamiento Inserción ---")
resultado_insercion, iteraciones_insercion = ordenamiento_insercion(lista)
print(f"Lista ordenada: {resultado_insercion}")
print(f"Iteraciones: {iteraciones_insercion}")

# Verificar que ambos producen el mismo resultado
print("\n--- Verificación ---")
if resultado_burbuja == resultado_insercion == sorted(lista):
    print("✓ Ambos algoritmos ordenan correctamente")
else:
    print("✗ Error: los algoritmos no coinciden")

# Comparar eficiencia
print(f"\n--- Comparación de Eficiencia ---")
if iteraciones_burbuja < iteraciones_insercion:
    print(f"Burbuja fue más eficiente: {iteraciones_burbuja} vs {iteraciones_insercion}")
    print(f"Diferencia: {iteraciones_insercion - iteraciones_burbuja} iteraciones")
elif iteraciones_insercion < iteraciones_burbuja:
    print(f"Inserción fue más eficiente: {iteraciones_insercion} vs {iteraciones_burbuja}")
    print(f"Diferencia: {iteraciones_burbuja - iteraciones_insercion} iteraciones")
else:
    print(f"Ambos usaron la misma cantidad: {iteraciones_burbuja} iteraciones")

print("\n" + "="*60)
print("✓ TODAS LAS PRUEBAS COMPLETADAS")
print("="*60)
