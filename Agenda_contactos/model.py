class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def __str__(self):
        return f"{self.nombre} | {self.telefono}  | {self.email}"
    
class AgendaModelo:
    def __init__(self):
        self.contactos = [] # lista donde se guardan los contactos

    def agregar(self, nombre, telefono, email):
        self.contactos.append(Contacto(nombre, telefono, email))

    def eliminar(self, nombre):
        antes = len(self.contactos)
        self.contactos = [C for C in self.contactos
                          if C.nombre.lower() != nombre.lower()]
        return len(self.contactos) < antes # true si se elimino algo
    def obtener_todos(self):
        return self.contactos
    