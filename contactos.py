class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f'Nombre: {self.nombre}\nTeléfono: {self.telefono}\nEmail: {self.email}'

def agregar_contacto(contactos):
    try:
        nombre = input('Introduce el nombre del contacto: ')
        telefono = input('Introduce el teléfono del contacto: ')
        email = input('Introduce el email del contacto: ')
        contacto = Contacto(nombre, telefono, email)
        contactos.append(contacto)
        print('Contacto agregado exitosamente.')
    except Exception as e:
        print(f'Error al agregar el contacto: {e}')

def mostrar_contactos(contactos):
    if not contactos:
        print('No hay contactos en la lista.')
        return
    for contacto in contactos:
        print(contacto)
        print('-' * 20)

def buscar_contacto(contactos):
    try:
        nombre_buscar = input('Introduce el nombre del contacto a buscar: ').lower()
        for contacto in contactos:
            if contacto.nombre.lower() == nombre_buscar:
                print(contacto)
                return
        print('Contacto no encontrado.')
    except Exception as e:
        print(f'Error al buscar el contacto: {e}')

def eliminar_contacto(contactos):
    try:
        nombre_eliminar = input('Introduce el nombre del contacto a eliminar: ').lower()
        for i, contacto in enumerate(contactos):
            if contacto.nombre.lower() == nombre_eliminar:
                del contactos[i]
                print('Contacto eliminado.')
                return
        print('Contacto no encontrado.')
    except Exception as e:
        print(f'Error al eliminar el contacto: {e}')

def menu_contactos():
    contactos = []
    while True:
        print('\nGestión de Contactos')
        print('1. Agregar contacto')
        print('2. Mostrar todos los contactos')
        print('3. Buscar contacto por nombre')
        print('4. Eliminar contacto por nombre')
        print('5. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion == 1:
                agregar_contacto(contactos)
            elif opcion == 2:
                mostrar_contactos(contactos)
            elif opcion == 3:
                buscar_contacto(contactos)
            elif opcion == 4:
                eliminar_contacto(contactos)
            elif opcion == 5:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')

if __name__ == '__main__':
    menu_contactos()
