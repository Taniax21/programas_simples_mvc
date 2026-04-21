class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas  = notas  # lista de números

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return (f" {self.nombre} | "
                f"Notas: {self.notas} | "
                f"Promedio: {self.promedio():.2f}")


class EstudiantesModelo:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, nombre, notas):
        self.estudiantes.append(Estudiante(nombre, notas))

    def obtener_todos(self):
        return self.estudiantes

    def buscar(self, nombre):
        for e in self.estudiantes:
            if e.nombre.lower() == nombre.lower():
                return e
        return None  # si no lo encuentra