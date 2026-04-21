class CalculadoraVista:

    def mostrar_menu(self):
        print("\n===== CALCULADORA =====")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

    def pedir_opcion(self):
        return input("Elige una opción: ")

    def pedir_numeros(self):
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        return a, b

    def mostrar_resultado(self, resultado):
        print(f"\nResultado: {resultado:.2f}")

    def mostrar_mensaje(self, msg):
        print(msg)