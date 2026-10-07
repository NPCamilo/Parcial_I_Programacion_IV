# Cifrado César
"""
Enunciado:
5. Implementar el algoritmo de cifrado y descifrado cesar haciendo uso de
POO, archivos y listas.

El cifrado César desplaza cada letra del texto un número fijo de
posiciones en el alfabeto.
"""

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']


class CifradoCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento

    def cifrar(self, texto):
        texto = texto.lower()
        resultado = ""
        for letra in texto:
            if letra in alfabeto:
                posicion = alfabeto.index(letra)
                nueva = (posicion + self.desplazamiento) % len(alfabeto)
                resultado = resultado + alfabeto[nueva]
            else:
                resultado = resultado + letra
        return resultado

    def descifrar(self, texto):
        texto = texto.lower()
        resultado = ""
        for letra in texto:
            if letra in alfabeto:
                posicion = alfabeto.index(letra)
                nueva = (posicion - self.desplazamiento) % len(alfabeto)
                resultado = resultado + alfabeto[nueva]
            else:
                resultado = resultado + letra
        return resultado


def menu():
    salir = False
    while salir == False:
        print("\n--- CIFRADO CESAR ---")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            desplazamiento = int(input("Desplazamiento: "))
            texto = input("Texto: ")
            cesar = CifradoCesar(desplazamiento)
            cifrado = cesar.cifrar(texto)
            print("Texto cifrado:", cifrado)
            f = open("cifrado.txt", "w")
            f.write(str(desplazamiento) + "\n" + cifrado)
            f.close()
            print("Guardado en cifrado.txt")
        elif opcion == "2":
            try:
                f = open("cifrado.txt", "r")
                desplazamiento = int(f.readline().strip())
                cifrado = f.readline().strip()
                f.close()
                cesar = CifradoCesar(desplazamiento)
                print("Texto descifrado:", cesar.descifrar(cifrado))
            except:
                print("No se encontro el archivo cifrado.txt")
        elif opcion == "3":
            salir = True
        else:
            print("Opcion invalida.")


menu()
