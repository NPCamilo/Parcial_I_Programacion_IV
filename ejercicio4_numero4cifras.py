# Número de 4 cifras
"""
Enunciado:
4. Diseñe un programa que reciba un numero entero de 4 cifras, diga si el
primer número es múltiplo del cuarto número y debe mostrar la suma del
segundo número y el tercero (no requiere implementar el paradigma
orientado a objetos), este punto se debe hacer usando operaciones
aritméticas para descomponer el numero de 4 cifras.
"""

n = int(input("Ingrese un numero entero de 4 cifras: "))

if n < 1000 or n > 9999:
    print("El numero debe tener 4 cifras.")
else:
    primero = n // 1000
    segundo = (n // 100) % 10
    tercero = (n // 10) % 10
    cuarto = n % 10

    print("Primer digito:", primero)
    print("Segundo digito:", segundo)
    print("Tercer digito:", tercero)
    print("Cuarto digito:", cuarto)

    if cuarto != 0 and primero % cuarto == 0:
        print("El primer digito SI es multiplo del cuarto.")
    elif cuarto == 0:
        print("El cuarto digito es 0, no se puede dividir.")
    else:
        print("El primer digito NO es multiplo del cuarto.")

    print("Suma del segundo y tercer digito:", segundo + tercero)
