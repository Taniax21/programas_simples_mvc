from model import CalculadoraModelo
from view  import CalculadoraVista

class CalculadoraControlador:

    def __init__(self):
        self.modelo = CalculadoraModelo()
        self.vista  = CalculadoraVista()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion in ("1", "2", "3", "4"):
                a, b = self.vista.pedir_numeros()

                if opcion == "1":
                    r = self.modelo.sumar(a, b)
                elif opcion == "2":
                    r = self.modelo.restar(a, b)
                elif opcion == "3":
                    r = self.modelo.multiplicar(a, b)
                elif opcion == "4":
                    r = self.modelo.dividir(a, b)
                    if r is None:
                        self.vista.mostrar_mensaje("✗ Error: no se puede dividir entre 0.")
                        continue

                self.vista.mostrar_resultado(r)

            elif opcion == "5":
                self.vista.mostrar_mensaje("¡Hasta luego!")
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")

if __name__ == "__main__":
    CalculadoraControlador().ejecutar()