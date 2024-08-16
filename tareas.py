class Tarea:
    def __init__(self, titulo, descripcion, estado='pendiente'):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f'Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}'

def agregar_tarea(tareas):
    try:
        titulo = input('Introduce el título de la tarea: ')
        descripcion = input('Introduce la descripción de la tarea: ')
        tarea = Tarea(titulo, descripcion)
        tareas.append(tarea)
        print('Tarea agregada exitosamente.')
    except Exception as e:
        print(f'Error al agregar la tarea: {e}')

def mostrar_tareas(tareas):
    if not tareas:
        print('No hay tareas en la lista.')
        return
    for tarea in tareas:
        print(tarea)
        print('-' * 20)

def buscar_tarea(tareas):
    try:
        titulo_buscar = input('Introduce el título de la tarea a buscar: ').lower()
        for tarea in tareas:
            if tarea.titulo.lower() == titulo_buscar:
                print(tarea)
                return
        print('Tarea no encontrada.')
    except Exception as e:
        print(f'Error al buscar la tarea: {e}')

def actualizar_estado_tarea(tareas):
    try:
        titulo_actualizar = input('Introduce el título de la tarea a actualizar: ').lower()
        for tarea in tareas:
            if tarea.titulo.lower() == titulo_actualizar:
                tarea.estado = 'completada'
                print('Tarea actualizada a completada.')
                return
        print('Tarea no encontrada.')
    except Exception as e:
        print(f'Error al actualizar la tarea: {e}')

def eliminar_tarea(tareas):
    try:
        titulo_eliminar = input('Introduce el título de la tarea a eliminar: ').lower()
        for i, tarea in enumerate(tareas):
            if tarea.titulo.lower() == titulo_eliminar:
                del tareas[i]
                print('Tarea eliminada.')
                return
        print('Tarea no encontrada.')
    except Exception as e:
        print(f'Error al eliminar la tarea: {e}')

def menu():
    tareas = []
    while True:
        print('\nSistema de Gestión de Tareas')
        print('1. Agregar tarea')
        print('2. Mostrar todas las tareas')
        print('3. Buscar tarea por título')
        print('4. Actualizar estado de tarea')
        print('5. Eliminar tarea por título')
        print('6. Salir')
        try:
            opcion = int(input('Selecciona una opción: '))
            if opcion == 1:
                agregar_tarea(tareas)
            elif opcion == 2:
                mostrar_tareas(tareas)
            elif opcion == 3:
                buscar_tarea(tareas)
            elif opcion == 4:
                actualizar_estado_tarea(tareas)
            elif opcion == 5:
                eliminar_tarea(tareas)
            elif opcion == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')

if __name__ == '__main__':
    menu()
