# Stock inicial
gama_alta = 10
gama_media = 25
gama_baja = 40

# Registro de compras
comprados_alta = 0
comprados_media = 0
comprados_baja = 0

while True:
    print("\n=== MENU ===")
    print("1.- Ver tipos de PC")
    print("2.- Comprar PC")
    print("3.- Cantidad de PCs por gama")
    print("4.- Mostrar PCs comprados")
    print("5.- Salir")
    
    try:
        opc = int(input("Ingrese la opción deseada (1-5): "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    if opc == 1:
        print("Los PCs que hay a la venta son de gama alta, media y baja.")

    elif opc == 2:
        try:
            pcbajo = int(input("¿Cuántos PCs de gama baja desea comprar?: "))
            pcmedio = int(input("¿Cuántos PCs de gama media desea comprar?: "))
            pcalto = int(input("¿Cuántos PCs de gama alta desea comprar?: "))
        except ValueError:
            print("Por favor, ingrese solo números enteros.")
            continue

        # Gama baja
        if 1 <= pcbajo <= gama_baja:
            gama_baja -= pcbajo
            comprados_baja += pcbajo
            print(f"Compra de PCs gama baja exitosa. Quedan {gama_baja} en stock.")
        elif pcbajo > gama_baja:
            print("No hay suficiente stock para gama baja.")
        elif pcbajo < 0:
            print("Debe ingresar un número positivo para gama baja.")

        # Gama media
        if 1 <= pcmedio <= gama_media:
            gama_media -= pcmedio
            comprados_media += pcmedio
            print(f"Compra de PCs gama media exitosa. Quedan {gama_media} en stock.")
        elif pcmedio > gama_media:
            print("No hay suficiente stock para gama media.")
        elif pcmedio < 0:
            print("Debe ingresar un número positivo para gama media.")

        # Gama alta
        if 1 <= pcalto <= gama_alta:
            gama_alta -= pcalto
            comprados_alta += pcalto
            print(f"Compra de PCs gama alta exitosa. Quedan {gama_alta} en stock.")
        elif pcalto > gama_alta:
            print("No hay suficiente stock para gama alta.")
        elif pcalto < 0:
            print("Debe ingresar un número positivo para gama alta.")

    elif opc == 3:
        print(f"La cantidad de PCs de gama alta es: {gama_alta}")
        print(f"La cantidad de PCs de gama media es: {gama_media}")
        print(f"La cantidad de PCs de gama baja es: {gama_baja}")

    elif opc == 4:
        print("=== PCs comprados ===")
        print(f"Gama alta: {comprados_alta}")
        print(f"Gama media: {comprados_media}")
        print(f"Gama baja: {comprados_baja}")

    elif opc == 5:
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor ingrese un número entre 1 y 5.")
