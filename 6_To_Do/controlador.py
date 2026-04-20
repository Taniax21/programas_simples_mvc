from modelo import Tarea
from vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.tareas = []

    def crear_tarea(self):
        """Crea una nueva tarea"""
        descripcion = self.vista.pedir_descripcion_tarea()
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"Tarea '{descripcion}' creada exitosamente.")

    def completar_tarea(self):
        """Marca una tarea como completada"""
        pendientes = [t for t in self.tareas if not t.estado]
        if not pendientes:
            print("No hay tareas pendientes para completar.")
            return

        print("\nTAREAS PENDIENTES:")
        for i, tarea in enumerate(pendientes, 1):
            print(f"{i}. {tarea.descripcion}")

        indice = self.vista.pedir_indice_tarea(
            pendientes,
            "Ingrese el número de la tarea a completar: "
        )

        if indice is not None:
            pendientes[indice].completar()
            print(f"Tarea '{pendientes[indice].descripcion}' marcada como completada.")

    def eliminar_tarea(self):
        """Elimina una tarea de la lista"""
        self.vista.mostrar_lista(self.tareas)
        if not self.tareas:
            return

        indice = self.vista.pedir_indice_tarea(
            self.tareas,
            "Ingrese el número de la tarea a eliminar: "
        )

        if indice is not None:
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada exitosamente.")

    def marcar_pendiente(self):
        """Marca una tarea como pendiente"""
        completadas = [t for t in self.tareas if t.estado]
        if not completadas:
            print("No hay tareas completadas para marcar como pendiente.")
            return

        print("\nTAREAS COMPLETADAS:")
        for i, tarea in enumerate(completadas, 1):
            print(f"{i}. {tarea.descripcion}")

        indice = self.vista.pedir_indice_tarea(
            completadas,
            "Ingrese el número de la tarea a marcar como pendiente: "
        )

        if indice is not None:
            completadas[indice].marcar_pendiente()
            print(f"Tarea '{completadas[indice].descripcion}' marcada como pendiente.")

    def mostrar_lista(self):
        """Muestra la lista de tareas"""
        self.vista.mostrar_lista(self.tareas)

    def ejecutar(self):
        """Ejecuta el programa principal"""
        print("¡Bienvenido al sistema de tareas!")
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == 1:
                self.crear_tarea()
            elif opcion == 2:
                self.completar_tarea()
            elif opcion == 3:
                self.eliminar_tarea()
            elif opcion == 4:
                self.marcar_pendiente()
            elif opcion == 5:
                self.mostrar_lista()
            elif opcion == 6:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

            input("\nPresione Enter para continuar...")
