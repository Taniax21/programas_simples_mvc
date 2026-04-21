from model import AgendaModelo
from view  import AgendaVista

class AgendaControlador:

    def __init__(self):
        self.modelo = AgendaModelo()
        self.vista  = AgendaVista()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == "1":
                n, t, e = self.vista.pedir_contacto()
                self.modelo.agregar(n, t, e)
                self.vista.mostrar_mensaje(f"✓ Contacto '{n}' agregado.")

            elif opcion == "2":
                contactos = self.modelo.obtener_todos()
                self.vista.mostrar_contactos(contactos)

            elif opcion == "3":
                nombre = self.vista.pedir_nombre()
                if self.modelo.eliminar(nombre):
                    self.vista.mostrar_mensaje(f"✓ Contacto '{nombre}' eliminado.")
                else:
                    self.vista.mostrar_mensaje(f"✗ No se encontró '{nombre}'.")

            elif opcion == "4":
                self.vista.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")

if __name__ == "__main__":
    AgendaControlador().ejecutar()