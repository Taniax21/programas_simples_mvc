from modelo import Producto
from vista import Vista


class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.productos = []

    def agregar_producto(self):
        """Agrega un nuevo producto al inventario"""
        nombre, stock, precio = self.vista.pedir_datos_producto()
        # Verificar que el producto no exista
        if any(p.nombre.lower() == nombre.lower() for p in self.productos):
            print(f"El producto '{nombre}' ya existe en el inventario.")
            return

        producto = Producto(nombre, stock, precio)
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado exitosamente al inventario.")

    def realizar_venta(self):
        """Realiza una venta de un producto"""
        self.vista.mostrar_inventario(self.productos)
        if not self.productos:
            return

        indice = self.vista.pedir_indice_producto(
            self.productos,
            "Seleccione el número del producto a vender: "
        )

        if indice is not None:
            cantidad = self.vista.pedir_cantidad("Cantidad a vender: ")
            if cantidad is not None:
                exito, mensaje = self.productos[indice].vender(cantidad)
                print(mensaje)

    def reponer_stock(self):
        """Repone el stock de un producto"""
        self.vista.mostrar_inventario(self.productos)
        if not self.productos:
            return

        indice = self.vista.pedir_indice_producto(
            self.productos,
            "Seleccione el número del producto a reponer: "
        )

        if indice is not None:
            cantidad = self.vista.pedir_cantidad("Cantidad a reponer: ")
            if cantidad is not None:
                mensaje = self.productos[indice].reponer(cantidad)
                print(mensaje)

    def eliminar_producto(self):
        """Elimina un producto del inventario"""
        self.vista.mostrar_inventario(self.productos)
        if not self.productos:
            return

        indice = self.vista.pedir_indice_producto(
            self.productos,
            "Seleccione el número del producto a eliminar: "
        )

        if indice is not None:
            producto_eliminado = self.productos.pop(indice)
            print(
                f"Producto '{producto_eliminado.nombre}' eliminado del inventario.")

    def ver_producto(self):
        """Muestra detalles de un producto específico"""
        self.vista.mostrar_inventario(self.productos)
        if not self.productos:
            return

        indice = self.vista.pedir_indice_producto(
            self.productos,
            "Seleccione el número del producto a consultar: "
        )

        if indice is not None:
            self.vista.mostrar_producto(self.productos[indice])

    def ver_inventario(self):
        """Muestra el inventario completo"""
        self.vista.mostrar_inventario(self.productos)

    def ejecutar(self):
        """Ejecuta el programa principal"""
        print("¡Bienvenido al Sistema de Inventario!")
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            if opcion == 1:
                self.ver_inventario()
            elif opcion == 2:
                self.agregar_producto()
            elif opcion == 3:
                self.realizar_venta()
            elif opcion == 4:
                self.reponer_stock()
            elif opcion == 5:
                self.eliminar_producto()
            elif opcion == 6:
                self.ver_producto()
            elif opcion == 7:
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

            input("\nPresione Enter para continuar...")
