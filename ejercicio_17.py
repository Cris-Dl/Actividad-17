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
            if producto.nombre.lower() == producto_buscado2:
                print(f"El producto {producto_buscado2} se encuentra en el carrito de compras")
                encotrado = True
                break
        if not encotrado:
            print("Producto no encontrado")


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
        case "3":
            print("Buscar producto")
            producto_buscado2 = input("Ingrese el nombre del producto ha buscar: ")
            producto_temporal2 = Producto(None, None, None)
            producto_temporal2.buscar_producto(producto_buscado2)
        case "4":
            print("Ordenar productos")
        case "5":
            print("Borrar carrito de compras")
        case "6":
            print("Ver carrito de compras")
            if not lista_producto:
                print("La lista de productos esta vacía")
            else:
                print("--- Lista de productos ---")
                for producto in lista_producto:
                    producto.mostrar_info()
        case "7":
            print("Contar producto")