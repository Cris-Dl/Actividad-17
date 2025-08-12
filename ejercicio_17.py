class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}  -   Precio: Q {self.precio}  -  Categoria: {self.categoria}")

    def eliminar_producto(self, producto_buscado):
        encontrado = False
        for i in lista_producto:
            if i.nombre.lower() == producto_buscado.lower():
                lista_producto.remove(i)
                print("Producto eliminado")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")

    def buscar_producto(self, producto_buscado2):
        encotrado = False
        for producto in lista_producto:
            if producto.nombre.lower() == producto_buscado2.lower():
                print(f"El producto {producto_buscado2} se encuentra en el carrito de compras")
                encotrado = True
                break
        if not encotrado:
            print("Producto no encontrado")

    def vaciar_lista(self, confirmacion):
        if confirmacion.lower() == "si":
            lista_producto.clear()
            print("Se ha vaciado el carrito de compras")
        else:
            print("Ha regresado al menú")

    def contar_producto(self, contar_producto):
        conteo = 0
        for producto in lista_producto:
            if producto.nombre.lower() == contar_producto.lower():
                conteo += 1
        print(f"El producto {contar_producto} ha sido ingresado {conteo} veces")

    def precio_total(self):
        total = 0
        for producto in lista_producto:
            total += producto.precio
        print(f"El total de las compras es de: Q{total}")

    def productos_por_categoria(self, categoria_buscar):
        encontrado = False
        print(f"Productos de la categoria {categoria_buscar}:")
        for producto in lista_producto:
            if producto.categoria.lower() == categoria_buscar.lower():
                producto.mostrar_info()
                encontrado = True
        if not encontrado:
            print("No se ha encontrado productos en esta categoría")

    def finalizar_compra(self):
        print("Productos agregados al carrito de compras: ")
        for producto in lista_producto:
            producto.mostrar_info()
        print()
        print("Total de la compra: ")
        total = 0
        for producto in lista_producto:
            total += producto.precio
        print("Gracias por su preferencia")

    def ordenar_productos(self):
        lista_producto.sort(key=lambda p: p.nombre)
        print("Productos agregados por nombre")
        for producto in lista_producto:
            producto.mostrar_info()

lista_producto = []

def agregar_producto():
    try:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: Q"))
        categoria = input("Ingrese la categoria del producto: ")
        productos = Producto(nombre, precio, categoria)
        lista_producto.append(productos)
        print("Producto agregado")
    except ValueError:
        print("Valor invalido, vuelva a intentar")
    except TypeError:
        print("Valor invalido, vuelva a intentar")
    except Exception as e:
        print("Ha ocurrido un error, vuelva a intentar.")

while True:
    print("---Menú---")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Buscar producto")
    print("4.- Ordenar productos")
    print("5.- Borrar carrito de compras")
    print("6.- Ver carrito de compras")
    print("7.- Contar producto")
    print("8.- Calcular total")
    print("9.- Productos por categoria")
    print("10.- Finalizar compra")
    menu_option = input("Ingrese el número de la opción a ingresar: ")
    print()
    match menu_option:
        case "1":
            print("Agregar producto")
            agregar_producto()
            print()
        case "2":
            print("Eliminar producto")
            producto_buscado = input("Ingrese el nombre del producto a eliminar: ")
            producto_temporal = Producto(None, None,None)
            producto_temporal.eliminar_producto(producto_buscado)
            print()
        case "3":
            print("Buscar producto")
            producto_buscado2 = input("Ingrese el nombre del producto ha buscar: ")
            producto_temporal2 = Producto(None, None, None)
            producto_temporal2.buscar_producto(producto_buscado2)
            print()
        case "4":
            print("Ordenar productos de la A a la Z")
            if not lista_producto:
                print("No hay productos agregados")
            else:
                ordenar_temporal = Producto(None, None, None)
                ordenar_temporal.ordenar_productos()
            print()
        case "5":
            print("Borrar carrito de compras")
            confirmacion = input("Realmente quiere vaciar el carrito de compras (si/no)?")
            confirmacion_temporal = Producto(None, None, None)
            confirmacion_temporal.vaciar_lista(confirmacion)
            print()
        case "6":
            print("Ver carrito de compras")
            if not lista_producto:
                print("La lista de productos esta vacía")
            else:
                print("--- Lista de productos ---")
                for producto in lista_producto:
                    producto.mostrar_info()
            print()
        case "7":
            print("Contar producto")
            if not lista_producto:
                print("No hay productos agregados")
            else:
                contar_producto = input("Ingrese el nombre del producto que desea contar: ")
                contar_producto_temporal = Producto(None, None, None)
                contar_producto_temporal.contar_producto(contar_producto)
            print()
        case "8":
            print("Total del carrito")
            if not lista_producto:
                print("No hay productos agregados")
            else:
                total_temporal = Producto(None, None, None)
                total_temporal.precio_total()
            print()
        case "9":
            print("Productos por categoría")
            if not lista_producto:
                print("No hay productos agregados")
            else:
                categoria_buscada = input("Ingrese el nombre de la categoria: ")
                categoria_temporal = Producto(None, None, None)
                categoria_temporal.productos_por_categoria(categoria_buscada)
            print()
        case "10":
            print("Finalizar compra")
            if not lista_producto:
                print("No hay productos agregados, de igual manera quieres salir?")
                validacion = input(": ")
                if validacion == "si":
                    print("Gracias, vuelva pronto")
                    break
                elif validacion == "no":
                    print("Voliendo al menú")
            else:
                finalizacion = Producto(None, None, None)
                finalizacion.finalizar_compra()
            print()