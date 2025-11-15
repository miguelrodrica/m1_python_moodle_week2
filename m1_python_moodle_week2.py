user_election = 0
inventory = []
product = {"nombre": None, "precio": None, "cantidad": None}

while True:
    print("")
    print("-- MENÚ INVENTARIO --")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("")
    try:
        user_election = int(input("Escriba el número de la opción seleccionada: "))
        if user_election <= 0 or user_election > 4:
            print("¡ERROR!. Número no contemplado en la lista.")
        elif user_election == 1:
            while True:
                try:
                    quantity = int(input("¿Cuántos productos desea ingresar?: "))
                    if quantity <= 0:
                        print("¡ERROR!. Ingrese un número positivo y diferente a 0.")
                    else:
                        for i in range(quantity):
                            print("")
                            print(f"Producto #{i+1}")
                            name_product = input("Nombre: ")
                            product["nombre"] = name_product
                            while True:
                                try:
                                    price_product = float(input("Precio: "))
                                    if price_product <= 0:
                                        print("¡ERROR!. El precio debe ser mayor a $0.")
                                        continue
                                    else:
                                        product["precio"] = price_product
                                    break
                                except ValueError:
                                    print("¡ERROR!. Debe ingresar un número.")
                            while True:
                                try:
                                    quantity_product = int(input("Cantidad: "))
                                    if quantity_product <= 0:
                                        print("¡ERROR!. La cantidad debe ser mayor a 0.")
                                        continue
                                    else:
                                        product["cantidad"] = quantity_product
                                    break
                                except ValueError:
                                    print("¡ERROR!. Debe ingresar un número.")
                            inventory.append(product)
                    break
                except ValueError:
                    print("¡ERROR!. Debe ingresar un número entero.")
        elif user_election == 2:
            if len(inventory) == 0:
                print("")
                print("¡ERROR! El inventario está vacío.")

        elif user_election == 3:
            print("Usted eligió 3. Calcular estadísticas")
        else:
            print("Usted eligió 4. Salir ¡CHAO!")
            repeat = False
    except ValueError:
        print("¡ERROR!. Debe ingresar un número entero.")