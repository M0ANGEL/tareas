class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f'Nombre: {self.nombre}\nCantidad: {self.cantidad}\nPrecio: {self.precio}'

def agregar_producto(inventario):
    try:
        nombre = input('Introduce el nombre del producto: ')
        cantidad = int(input('Introduce la cantidad del producto: '))
        precio = float(input('Introduce el precio del producto: '))
        producto = Producto(nombre, cantidad, precio)
        inventario.append(producto)
        print('Producto agregado exitosamente.')
    except ValueError:
        print('Entrada inválida. Asegúrate de ingresar un número válido para cantidad y precio.')
    except Exception as e:
        print(f'Error al agregar el producto: {e}')

def mostrar_inventario(inventario):
    if not inventario:
        print('No hay productos en el inventario.')
        return
    for producto in inventario:
        print(producto)
        print('-' * 20)

def buscar_producto(inventario):
    try:
        nombre_buscar = input('Introduce el nombre del producto a buscar: ').lower()
        for producto in inventario:
            if producto.nombre.lower() == nombre_buscar:
                print(producto)
                return
        print('Producto no encontrado.')
    except Exception as e:
        print(f'Error al buscar el producto: {e}')

def actualizar_producto(inventario):
    try:
        nombre_actualizar = input('Introduce el nombre del producto a actualizar: ').lower()
        for producto in inventario:
            if producto.nombre.lower() == nombre_actualizar:
                producto.cantidad = int(input('Introduce la nueva cantidad: '))
                producto.precio = float(input('Introduce el nuevo precio: '))
                print('Producto actualizado.')
                return
        print('Producto no encontrado.')
    except ValueError:
        print('Entrada inválida. Asegúrate de ingresar un número válido para cantidad y precio.')
    except Exception as e:
        print(f'Error al actualizar el producto: {e}')

def eliminar_producto(inventario):
    try:
        nombre_eliminar = input('Introduce el nombre del producto a eliminar: ').lower()
        for i, producto in enumerate(inventario):
            if producto.nombre.lower() == nombre_eliminar:
                del inventario[i]
                print('Producto eliminado.')
                return
        print('Producto no encontrado.')
    except Exception as e:
        print(f'Error al eliminar el producto: {e}')

def menu_inventario():
    inventario = []
    while True:
        print('\nSistema de Inventario')
        print('1. Agregar producto')
        print('2. Mostrar todos los productos')
        print('3. Buscar producto por nombre')
        print('4. Actualizar producto')
        print('5. Eliminar producto por nombre')
        print('6. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion == 1:
                agregar_producto(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                buscar_producto(inventario)
            elif opcion == 4:
                actualizar_producto(inventario)
            elif opcion == 5:
                eliminar_producto(inventario)
            elif opcion == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')

if __name__ == '__main__':
    menu_inventario()
