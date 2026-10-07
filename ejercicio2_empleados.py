# Sistema de Gestión de Empleados
"""
Enunciado:
2. Sistema de Gestión de Empleados
Crea una aplicación de gestión de empleados. Debes crear las siguientes clases:

Clase Empleado:
- Atributos: Nombre, ID, Salario Base, Años de Experiencia
- Métodos:
  - Constructor para inicializar todos los atributos.
  - calcular_salario(): retorna el salario total sumando un bono al salario
    base según años de experiencia:
      * Entre 0 y 2 años: bono de 5% del salario base.
      * Entre 3 y 5 años: bono de 10% del salario base.
      * Más de 5 años: bono de 15% del salario base.
  - Un método para representar al empleado en formato de texto.

Clase GestorEmpleados:
- Atributos: una lista de empleados.
- Métodos:
  - agregar_empleado(empleado): Agrega un empleado a la lista.
  - eliminar_empleado(id): Elimina un empleado según su ID.
  - buscar_empleado(id): Busca y devuelve un empleado por su ID.
  - editar_empleado(id): Edita la información de un empleado y actualiza el archivo.
  - mostrar_empleados(): Muestra todos los empleados con sus salarios totales.
  - guardar_empleados(archivo): Guarda la lista en un archivo.
  - cargar_empleados(archivo): Carga la lista desde un archivo.

Requerimiento adicional: menú que permita interactuar con GestorEmpleados.
Archivos de texto plano.
"""

ARCHIVO = "empleados.txt"


class Empleado:
    def __init__(self, nombre, id, salario_base, anos_experiencia):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base
        self.anos_experiencia = anos_experiencia

    def calcular_salario(self):
        if self.anos_experiencia <= 2:
            bono = self.salario_base * 0.05
        elif self.anos_experiencia <= 5:
            bono = self.salario_base * 0.10
        else:
            bono = self.salario_base * 0.15
        return self.salario_base + bono

    def __str__(self):
        return "ID: " + str(self.id) + " | Nombre: " + self.nombre + \
               " | Salario base: " + str(self.salario_base) + \
               " | Años: " + str(self.anos_experiencia) + \
               " | Salario total: " + str(self.calcular_salario())


class GestorEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        print("Empleado agregado.")

    def eliminar_empleado(self, id):
        encontrado = self.buscar_empleado(id)
        if encontrado != None:
            self.empleados.remove(encontrado)
            print("Empleado eliminado.")
        else:
            print("No se encontro el empleado.")

    def buscar_empleado(self, id):
        for e in self.empleados:
            if e.id == id:
                return e
        return None

    def editar_empleado(self, id):
        e = self.buscar_empleado(id)
        if e == None:
            print("No se encontro el empleado.")
            return
        print("1. Nombre\n2. Salario base\n3. Años de experiencia")
        opcion = input("Que desea editar: ")
        if opcion == "1":
            e.nombre = input("Nuevo nombre: ")
        elif opcion == "2":
            e.salario_base = float(input("Nuevo salario base: "))
        elif opcion == "3":
            e.anos_experiencia = int(input("Nuevos años: "))
        self.guardar_empleados(ARCHIVO)
        print("Empleado actualizado.")

    def mostrar_empleados(self):
        if len(self.empleados) == 0:
            print("No hay empleados.")
        for e in self.empleados:
            print(e)

    def guardar_empleados(self, archivo):
        f = open(archivo, "w")
        for e in self.empleados:
            f.write(str(e.id) + ";" + e.nombre + ";" + str(e.salario_base) + ";" + str(e.anos_experiencia) + "\n")
        f.close()

    def cargar_empleados(self, archivo):
        try:
            f = open(archivo, "r")
            self.empleados = []
            for linea in f:
                datos = linea.strip().split(";")
                if len(datos) == 4:
                    e = Empleado(datos[1], int(datos[0]), float(datos[2]), int(datos[3]))
                    self.empleados.append(e)
            f.close()
        except:
            print("No se pudo cargar el archivo.")


def menu():
    gestor = GestorEmpleados()
    gestor.cargar_empleados(ARCHIVO)
    salir = False
    while salir == False:
        print("\n--- GESTION DE EMPLEADOS ---")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Buscar empleado")
        print("4. Editar empleado")
        print("5. Mostrar empleados")
        print("6. Guardar")
        print("7. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            salario = float(input("Salario base: "))
            anos = int(input("Años de experiencia: "))
            gestor.agregar_empleado(Empleado(nombre, id, salario, anos))
        elif opcion == "2":
            gestor.eliminar_empleado(int(input("ID: ")))
        elif opcion == "3":
            e = gestor.buscar_empleado(int(input("ID: ")))
            print(e if e != None else "No encontrado.")
        elif opcion == "4":
            gestor.editar_empleado(int(input("ID: ")))
        elif opcion == "5":
            gestor.mostrar_empleados()
        elif opcion == "6":
            gestor.guardar_empleados(ARCHIVO)
            print("Guardado.")
        elif opcion == "7":
            gestor.guardar_empleados(ARCHIVO)
            salir = True
        else:
            print("Opcion invalida.")


menu()
