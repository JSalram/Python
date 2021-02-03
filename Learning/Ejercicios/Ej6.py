# Ejercicio 6

listaProductos = []


def identificaRepetido(nombre):
    existe = False
    for producto in listaProductos:
        if nombre in producto:
            existe = True
            break
    return existe


def insertaProducto(nombre, precio, iva):
    total = (precio * iva / 100) + precio
    producto = [nombre, precio, iva, total]
    listaProductos.append(producto)


def eliminaProducto(nombre):
    for producto in listaProductos:
        if producto[0] == nombre:
            listaProductos.remove(producto)


def modificaProducto(nombre, valor, nuevoValor):
    for producto in listaProductos:
        if producto[0] == nombre:
            producto[valor] = nuevoValor
            total = (producto[1] * producto[2] / 100) + producto[1]
            producto[3] = total


opcion = 1
while opcion < 4:
    print()
    print("Indica qué deseas hacer")
    print("0. Ver productos")
    print("1. Añadir")
    print("2. Eliminar")
    print("3. Modificar")
    print("4. Salir")

    opcion = input("Opción: ")
    try:
        opcion = int(opcion)
    except:
        print("La opción debe ser un numero entero")
        exit()
    print()

    if opcion == 0:
        if len(listaProductos) > 0:
            print("Lista de productos:")
            for producto in listaProductos:
                print(producto[0] + "; Precio: " + str(producto[1]) + "; IVA: " + str(producto[2]) + "%; Total: " + str(producto[3]))

    elif opcion == 1:
        print("Indica los detalles del producto")
        nombre = input("Nombre: ")
        if identificaRepetido(nombre):
            print("Este producto ya existe")
        else:
            precio = input("Precio: ")
            try:
                precio = float(precio)
            except:
                print("El precio debe ser un numero entero")
                exit()
            iva = input("Porcentaje de IVA (4 / 10 / 24): ")
            try:
                iva = int(iva)
            except:
                print("El IVA debe ser un numero entero")
                exit()
            while iva not in [4, 10, 24]:
                iva = input("IVA erróneo. Vuelve a introducirlo: ")
                try:
                    iva = int(iva)
                except:
                    print("El IVA debe ser un numero entero")
                    exit()
            insertaProducto(nombre, precio, iva)
            print("Producto insertado")

    elif opcion == 2:
        nombre = input("Nombre del producto a eliminar: ")
        if identificaRepetido(nombre):
            eliminaProducto(nombre)
            print("Producto eliminado")
        else:
            print("El producto no existe")

    elif opcion == 3:
        nombre = input("Nombre del producto a modificar: ")
        if identificaRepetido(nombre):
            print("Indica el valor a cambiar:")
            print("1. Precio")
            print("2. IVA")
            valor = input("Opción: ")
            try:
                valor = int(valor)
            except:
                print("El valor debe ser un numero entero")
                exit()
            if valor == 1:
                nuevoValor = input("Nuevo precio: ")
                try:
                    nuevoValor = float(nuevoValor)
                except:
                    print("El precio debe ser un numero entero")
                    exit()
                modificaProducto(nombre, valor, nuevoValor)
                print("Precio modificado")
            elif valor == 2:
                nuevoValor = input("Nuevo IVA (4 / 10 / 24): ")
                try:
                    nuevoValor = int(nuevoValor)
                except:
                    print("El IVA debe ser un numero entero")
                    exit()
                while nuevoValor not in [4, 10, 24]:
                    nuevoValor = input("IVA erróneo. Vuelve a introducirlo: ")
                    try:
                        nuevoValor = int(nuevoValor)
                    except:
                        print("El IVA debe ser un numero entero")
                        exit()
                modificaProducto(nombre, valor, nuevoValor)
                print("IVA modificado")
            else:
                print("Opción errónea")
        else:
            print("El nombre no coincide con ningún producto")

    elif opcion != 4:
        print("Opción incorrecta")
