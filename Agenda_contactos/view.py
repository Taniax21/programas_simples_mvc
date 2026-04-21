class AgendaVista:

    def mostrar_menu(self):
        print("\n===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Eliminar contacto")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Elige una opcion: ")
    
    def pedir_contacto(self):
        nombre   = input("Nombre: ")
        telefono = input("Teléfono: ")
        email    = input("Email: ")
        return nombre, telefono, email
    def pedir_nombre(self):
        return input("Nombre a eliminar: ")
    
    def mostrar_contactos(self, contactos):
        if contactos:
            print("\n--- Lista de contactos ---")
            for i, c in enumerate(contactos, 1):
                print(f"{i}. {c}")
        else:
            print("\nNo hay contactos guardados.")

    def mostrar_mensaje(self, msg):
        print(msg)