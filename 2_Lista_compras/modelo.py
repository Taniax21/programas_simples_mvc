class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.comprado = False  # Para marcar si el producto ya fue comprado

    def marcar_comprado(self):
        self.comprado = True

    def __str__(self):
        estado = "[bien]" if self.comprado else "[ ]"
        return f"{estado} {self.nombre} - Cantidad: {self.cantidad}"
