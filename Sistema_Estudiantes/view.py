class EstudiantesVista:

    def mostrar_menu(self):
        print("\n===== SISTEMA DE ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Buscar estudiante")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Elige una opción: ")

    def pedir_estudiante(self):
        nombre = input("Nombre del estudiante: ")
        cantidad = int(input("¿Cuántas notas vas a ingresar? "))
        notas = []
        for i in range(cantidad):
            nota = float(input(f"  Nota {i+1}: "))
            notas.append(nota)
        return nombre, notas

    def pedir_nombre(self):
        return input("Nombre a buscar: ")

    def mostrar_estudiantes(self, estudiantes):
        if estudiantes:
            print("\n--- Lista de estudiantes ---")
            for i, e in enumerate(estudiantes, 1):
                print(f"{i}. {e}")
        else:
            print("\nNo hay estudiantes registrados.")

    def mostrar_estudiante(self, estudiante):
        if estudiante:
            print(f"\nResultado: {estudiante}")
        else:
            print("\n✗ Estudiante no encontrado.")

    def mostrar_mensaje(self, msg):
        print(msg)