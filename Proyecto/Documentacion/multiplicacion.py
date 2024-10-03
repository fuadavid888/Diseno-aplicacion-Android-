import time

def karatsuba(x, y, depth=0):
    indent = "  " * depth  # Para la indentación en la salida

    # Obtener el tamaño más grande entre las dos cadenas
    n = max(len(str(x)), len(str(y)))

    # Si el tamaño es pequeño, usar multiplicación directa
    if n <= 1:
        return x * y

    # Dividir el tamaño en mitades
    m = n // 2

    # Dividir x e y en partes altas y bajas
    x_high = x // 10**m
    x_low = x % 10**m
    y_high = y // 10**m
    y_low = y % 10**m

    if depth == 0:
        print(f"Multiplicando {x} y {y}")
        print(f"Dividido {x} en {x_high} (alto) y {x_low} (bajo)")
        print(f"Dividido {y} en {y_high} (alto) y {y_low} (bajo)")

    # Recursión para las tres multiplicaciones
    p1 = karatsuba(x_high, y_high, depth + 1)
    p2 = karatsuba(x_low, y_low, depth + 1)
    p3 = karatsuba(x_high + x_low, y_high + y_low, depth + 1)

    # Cálculos intermedios separados
    part1 = p1 * 10**(2 * m)
    part2 = (p3 - p1 - p2) * 10**m
    part3 = p2

    # Combinar los resultados
    result = part1 + part2 + part3

    if depth == 0:
        print(f"Resultado de {x_high} * {y_high} = {p1}")
        print(f"Resultado de {x_low} * {y_low} = {p2}")
        print(f"Resultado de ({x_high} + {x_low}) * ({y_high} + {y_low}) = {p3}")
        print(f"Cálculo intermedio: {p1} * 10^{2 * m} = {part1}")
        print(f"Cálculo intermedio: ({p3} - {p1} - {p2}) * 10^{m} = {part2}")
        print(f"Cálculo intermedio: {p2} = {part3}")
        print(f"Resultado final: {result}")

    return result

# Solicitar los números al usuario
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))

# Medir el tiempo de ejecución
start_time = time.time()

# Ejecutar el algoritmo de Karatsuba y mostrar los pasos
result = karatsuba(x, y)

end_time = time.time()
execution_time = end_time - start_time

print(f"\nEl resultado de {x} * {y} es: {result}")
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")






