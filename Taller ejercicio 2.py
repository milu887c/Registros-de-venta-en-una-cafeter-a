from os import system

codigos = []
ventas = []
cantidades = []
unidades = []
mayor = []

contador = 0

print('====PROGRAMA DE CONTROL DE VENTAS====\n')

while True:
    try:
        print('Para terminar el registro ingrese el código \'0\'')
        codigo = int(input('Ingrese el código del producto: '))
        break
    except ValueError:
        system('cls')
        print('Valor inválido. Debes ingresar un número')

while codigo != 0:

    while True:
        try:
            cantidad = int(input('Ingrese la cantidad comprada: '))
            unidad = int(input('Ingrese el valor unitario: '))
            break
        except ValueError:
            system('cls')
            print('Valor inválido. Debes ingresar un número')


    total = cantidad * unidad

    if total > 30000:
        mayor.append(total)
    
    unidades.append(unidad)
    ventas.append(total)
    cantidades.append(cantidad)
    codigos.append(codigo)


    system('cls')
    contador += 1
    if contador != 1:
        print(f'Llevas {contador} registros')
    else: 
        print(f'Llevas {contador} registro')

    while True:
            try:
                print('Para terminar el registro ingrese el código \'0\'')
                codigo = int(input('Ingrese el código del producto: '))
                break
            except ValueError:
                system('cls')
                print('Valor inválido. Debes ingresar un número')


if ventas:
    suma_cant = sum(cantidades)
    suma_ventas = sum(ventas)
    maxima = max(ventas)
    cant_mayores = len(mayor)

    system('cls')
    print(f'Los códigos ingresados fueron {codigos}')
    print(f'La lista de las ventas fueron {ventas}')
    print(f'Las cantidades compradas fueron {cantidades}')
    print(f'Los valores unitarios fueron {unidades}')
    print(f'Las ventas mayores a $30.000 pesos fueron {mayor}\n')

    print(f'La cantidad de ventas realizadas fue de {contador}')
    print(f'El total de productos vendidos fueron {suma_cant}')
    print(f'El total recuadado es de {suma_ventas}')
    print(f'EL valor de compra más alto fue {maxima}')
    print(f'La cantidad de compras superiores a $30.000 fueron {cant_mayores}')

    print('\nDetalles de cada venta:')

    for i in range(len(ventas)):
        print(f'\nVenta {i + 1}:\nEl código de la venta es: {codigos[i]}\nCantidad comprada: {cantidades[i]}\nEl valor unitario es: {unidades[i]}\nEl total de la venta es: {ventas[i]}')
        

else:
    print('\nNo se registraron ventas')