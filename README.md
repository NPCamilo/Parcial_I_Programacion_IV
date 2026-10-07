# Parcial I - Programación Orientada a Objetos (POO)

Este repositorio contiene la solución del taller de sustentación del Parcial I.

## Contenido

### 1. Conceptos
Tema 1 es una reflexión conceptual (Clase, Objeto, Self, Constructor, POO,
Método, Instancia). No requiere código; conviene repasarlos para la
sustentación.

### 2. `ejercicio2_empleados.py`
Sistema de Gestión de Empleados.
- Clase `Empleado` con nombre, ID, salario base y años de experiencia.
- Método `calcular_salario()` que aplica bono según años de experiencia
  (5%, 10% o 15% del salario base).
- Clase `GestorEmpleados` con métodos para agregar, eliminar, buscar, editar,
  mostrar, guardar y cargar empleados.
- Persistencia con archivo de texto plano (`empleados.txt`).
- Menú interactivo en consola.

### 3. `ejercicio3_tienda.py`
Sistema de Ventas de Productos con Inventario.
- Clases `Producto`, `Cliente` y `Tienda`.
- Manejo de inventario (`disminuir_inventario`, `aumentar_inventario`).
- `realizar_compra` / `realizar_venta` validan stock y saldo.
- Persistencia con archivo XML (`tienda.xml`).
- Menú interactivo en consola.

### 4. `ejercicio4_numero4cifras.py`
Programa que recibe un entero de 4 cifras (sin POO) y:
- Indica si el primer dígito es múltiplo del cuarto dígito.
- Muestra la suma del segundo y tercer dígito.
- Usa operaciones aritméticas (`//`, `%`) para descomponer el número.

### 5. `ejercicio5_cesar.py`
Cifrado y descifrado César con POO, listas y archivos.
- Clase `CifradoCesar` con métodos `cifrar` y `descifrar`.
- El alfabeto se maneja como lista.
- El texto cifrado se guarda en `cifrado.txt` y se puede descifrar después.
- Menú interactivo en consola.

## Cómo ejecutar

```bash
python ejercicio2_empleados.py
python ejercicio3_tienda.py
python ejercicio4_numero4cifras.py
python ejercicio5_cesar.py
```

Requiere Python 3. Los archivos de datos (`empleados.txt`, `tienda.xml`,
`cifrado.txt`) se generan automáticamente al usar los programas.
