from model import EstudiantesModelo
from view  import EstudiantesVista

class EstudiantesControlador:

    def __init__(self):
        self.modelo = EstudiantesModelo()
        self.vista  = EstudiantesVista()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                nombre, notas = self.vista.pedir_estudiante()
                self.modelo.agregar(nombre, notas)
                self.vista.mostrar_mensaje(f"✓ Estudiante '{nombre}' registrado.")

            elif opcion == "2":
                estudiantes = self.modelo.obtener_todos()
                self.vista.mostrar_estudiantes(estudiantes)

            elif opcion == "3":
                nombre = self.vista.pedir_nombre()
                estudiante = self.modelo.buscar(nombre)
                self.vista.mostrar_estudiante(estudiante)

            elif opcion == "4":
                self.vista.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")

if __name__ == "__main__":
    EstudiantesControlador().ejecutar()