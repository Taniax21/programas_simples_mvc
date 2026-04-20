from modelo import Producto


class Vista:
    def __init__(self):
        pass

    def mostrar_inventario(self, productos):
        """Muestra el inventario completo de forma organizada"""
        if not productos:
            print("El inventario está vacío.")
            return

        print("\n" + "="*80)
        print("                         INVENTARIO DE PRODUCTOS")
        print("="*80)
        print(f"{'Producto':<20} {'Stock':<10} {'Precio':<12} {'Total Inv.':<15}")
        print("-"*80)

        total_inventario = 0
        for producto in productos:
            valor = producto.get_valor_total()
            total_inventario += valor
            print(
                f"{producto.nombre:<20} {producto.stock:<10} ${producto.precio:<11.2f} ${valor:<14.2f}")

        print("-"*80)
        print(f"{'VALOR TOTAL DEL INVENTARIO':<42} ${total_inventario:.2f}")
        print("="*80)

    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("\n" + "="*50)
        print("        SISTEMA DE INVENTARIO")
        print("="*50)
        print("1. Ver inventario")
        print("2. Agregar producto")
        print("3. Realizar venta")
        print("4. Reponer stock")
        print("5. Eliminar producto")
        print("6. Ver producto específico")
        print("7. Salir")
        print("="*50)

    def pedir_opcion(self):
        """Pide al usuario que seleccione una opción"""
        try:
            opcion = int(input("Seleccione una opción (1-7): "))
            return opcion
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return None

    def pedir_datos_producto(self):
        """Pide datos para crear un nuevo producto"""
        nombre = input("Nombre del producto: ").strip()
        while not nombre:
            nombre = input(
                "El nombre no puede estar vacío. Nombre del producto: ").strip()

        try:
            stock = int(input("Stock inicial: "))
            while stock < 0:
                stock = int(
                    input("El stock no puede ser negativo. Stock inicial: "))

            precio = float(input("Precio unitario: "))
            while precio < 0:
                precio = float(
                    input("El precio no puede ser negativo. Precio unitario: "))

            return nombre, stock, precio
        except ValueError:
            print("Datos inválidos. Intente nuevamente.")
            return self.pedir_datos_producto()

    def pedir_indice_producto(self, productos, mensaje):
        """Pide el índice de un producto de la lista"""
        if not productos:
            print("No hay productos en el inventario.")
            return None

        try:
            indice = int(input(mensaje)) - 1
            if 0 <= indice < len(productos):
                return indice
            else:
                print("Índice fuera de rango.")
                return None
        except ValueError:
            print("Índice inválido.")
            return None

    def pedir_cantidad(self, mensaje):
        """Pide una cantidad válida"""
        try:
            cantidad = int(input(mensaje))
            while cantidad <= 0:
                cantidad = int(
                    input("La cantidad debe ser mayor a 0. Ingrese nuevamente: "))
            return cantidad
        except ValueError:
            print("Cantidad inválida.")
            return None

    def mostrar_producto(self, producto):
        """Muestra detalles de un producto"""
        print("\n" + "-"*60)
        print(f"Nombre: {producto.nombre}")
        print(f"Stock disponible: {producto.stock}")
        print(f"Precio unitario: ${producto.precio:.2f}")
        print(f"Valor total en inventario: ${producto.get_valor_total():.2f}")
        print("-"*60)
