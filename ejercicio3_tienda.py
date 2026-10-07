# Sistema de Ventas de Productos con Inventario
"""
Enunciado:
3. Sistema de Ventas de Productos con Inventario
Crea un sistema de ventas que gestione productos y clientes. Debe llevar
control de los productos en inventario y de las ventas realizadas.
Para este ejercicio debe implementar archivos XML.

Clase Producto:
- Atributos: Nombre, ID, Precio, Cantidad en inventario
- Métodos:
  - Constructor para inicializar los atributos.
  - disminuir_inventario(cantidad): disminuye la cantidad en inventario.
  - aumentar_inventario(cantidad): aumenta la cantidad en inventario.
  - mostrar_informacion(): muestra la información del producto.

Clase Cliente:
- Atributos: Nombre, ID, Saldo
- Métodos:
  - Constructor para inicializar los atributos.
  - realizar_compra(producto, cantidad): reduce el saldo del cliente y reduce
    el inventario del producto, siempre que el saldo y el stock lo permitan.
  - mostrar_informacion(): muestra la información del cliente.

Clase Tienda:
- Atributos: lista de productos, lista de clientes
- Métodos:
  - agregar_producto(producto)
  - agregar_cliente(cliente)
  - realizar_venta(id_cliente, id_producto, cantidad)
  - mostrar_productos()
  - mostrar_clientes()
  - guardar_datos(archivo): guarda productos y clientes en XML.
  - cargar_datos(archivo): carga productos y clientes desde XML.
"""

import xml.etree.ElementTree as ET

ARCHIVO = "tienda.xml"


class Producto:
    def __init__(self, nombre, id, precio, cantidad):
        self.nombre = nombre
        self.id = id
        self.precio = precio
        self.cantidad = cantidad

    def disminuir_inventario(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad = self.cantidad - cantidad
            return True
        return False

    def aumentar_inventario(self, cantidad):
        self.cantidad = self.cantidad + cantidad

    def mostrar_informacion(self):
        print("Producto: " + self.nombre + " | ID: " + str(self.id) +
              " | Precio: " + str(self.precio) + " | Cantidad: " + str(self.cantidad))


class Cliente:
    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = id
        self.saldo = saldo

    def realizar_compra(self, producto, cantidad):
        total = producto.precio * cantidad
        if total <= self.saldo and cantidad <= producto.cantidad:
            self.saldo = self.saldo - total
            producto.disminuir_inventario(cantidad)
            print("Compra realizada. Total: " + str(total))
            return True
        print("No se puede realizar la compra (saldo o stock insuficiente).")
        return False

    def mostrar_informacion(self):
        print("Cliente: " + self.nombre + " | ID: " + str(self.id) + " | Saldo: " + str(self.saldo))


class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Producto agregado.")

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("Cliente agregado.")

    def buscar_producto(self, id_producto):
        for p in self.productos:
            if p.id == id_producto:
                return p
        return None

    def buscar_cliente(self, id_cliente):
        for c in self.clientes:
            if c.id == id_cliente:
                return c
        return None

    def realizar_venta(self, id_cliente, id_producto, cantidad):
        cliente = self.buscar_cliente(id_cliente)
        producto = self.buscar_producto(id_producto)
        if cliente == None or producto == None:
            print("Cliente o producto no encontrado.")
        else:
            cliente.realizar_compra(producto, cantidad)

    def mostrar_productos(self):
        for p in self.productos:
            p.mostrar_informacion()

    def mostrar_clientes(self):
        for c in self.clientes:
            c.mostrar_informacion()

    def guardar_datos(self, archivo):
        raiz = ET.Element("tienda")
        productos_xml = ET.SubElement(raiz, "productos")
        for p in self.productos:
            prod = ET.SubElement(productos_xml, "producto")
            ET.SubElement(prod, "nombre").text = p.nombre
            ET.SubElement(prod, "id").text = str(p.id)
            ET.SubElement(prod, "precio").text = str(p.precio)
            ET.SubElement(prod, "cantidad").text = str(p.cantidad)
        clientes_xml = ET.SubElement(raiz, "clientes")
        for c in self.clientes:
            cli = ET.SubElement(clientes_xml, "cliente")
            ET.SubElement(cli, "nombre").text = c.nombre
            ET.SubElement(cli, "id").text = str(c.id)
            ET.SubElement(cli, "saldo").text = str(c.saldo)
        arbol = ET.ElementTree(raiz)
        arbol.write(archivo, encoding="utf-8", xml_declaration=True)

    def cargar_datos(self, archivo):
        try:
            arbol = ET.parse(archivo)
            raiz = arbol.getroot()
            self.productos = []
            self.clientes = []
            for prod in raiz.find("productos"):
                p = Producto(prod.find("nombre").text,
                             int(prod.find("id").text),
                             float(prod.find("precio").text),
                             int(prod.find("cantidad").text))
                self.productos.append(p)
            for cli in raiz.find("clientes"):
                c = Cliente(cli.find("nombre").text,
                            int(cli.find("id").text),
                            float(cli.find("saldo").text))
                self.clientes.append(c)
        except:
            print("No se pudo cargar el archivo.")


def menu():
    tienda = Tienda()
    tienda.cargar_datos(ARCHIVO)
    salir = False
    while salir == False:
        print("\n--- TIENDA ---")
        print("1. Agregar producto")
        print("2. Agregar cliente")
        print("3. Realizar venta")
        print("4. Mostrar productos")
        print("5. Mostrar clientes")
        print("6. Guardar")
        print("7. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            tienda.agregar_producto(Producto(nombre, id, precio, cantidad))
        elif opcion == "2":
            nombre = input("Nombre: ")
            id = int(input("ID: "))
            saldo = float(input("Saldo: "))
            tienda.agregar_cliente(Cliente(nombre, id, saldo))
        elif opcion == "3":
            id_cliente = int(input("ID cliente: "))
            id_producto = int(input("ID producto: "))
            cantidad = int(input("Cantidad: "))
            tienda.realizar_venta(id_cliente, id_producto, cantidad)
        elif opcion == "4":
            tienda.mostrar_productos()
        elif opcion == "5":
            tienda.mostrar_clientes()
        elif opcion == "6":
            tienda.guardar_datos(ARCHIVO)
            print("Guardado.")
        elif opcion == "7":
            tienda.guardar_datos(ARCHIVO)
            salir = True
        else:
            print("Opcion invalida.")


menu()
