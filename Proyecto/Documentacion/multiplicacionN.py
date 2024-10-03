import time

def multiplicacion_tradicional(a, b):
    a_str = str(a)
    b_str = str(b)
    len_a = len(a_str)
    len_b = len(b_str)
    
    resultados = [0] * (len_a + len_b)
    
    for i in range(len_a - 1, -1, -1):
        for j in range(len_b - 1, -1, -1):
            digito_a = int(a_str[i])
            digito_b = int(b_str[j])
            producto = digito_a * digito_b
            posicion = (len_a - 1 - i) + (len_b - 1 - j)
            resultado_total = producto + resultados[posicion]
            resultados[posicion] = resultado_total % 10
            resultados[posicion + 1] += resultado_total // 10
    
    resultado_final = ''.join(map(str, resultados[::-1]))
    return resultado_final.lstrip('0') or '0'

def main():
    try:
        # Leer números desde la consola
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        
        # Medir el tiempo de ejecución
        start_time = time.time()
        resultado = multiplicacion_tradicional(a, b)
        end_time = time.time()
        
        # Mostrar el resultado y el tiempo de ejecución
        print(f"El resultado de {a} × {b} es {resultado}")
        print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
        
    except ValueError:
        print("Por favor, introduce solo números enteros.")

if __name__ == "__main__":
    main()

