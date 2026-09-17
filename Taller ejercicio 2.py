from os import system

l = []
v = []
p = []
mi = []

print('Programa de control de ventas :D\n')

c = int(input('Ingrese el código del producto: '))

while c != 0:

    
    co = int(input('Ingrese la cantidad comprada: '))
    u = int(input('Ingrese el valor unitario: '))

    va = co * u

    if va > 30000:
        mi.append(va)

    v.append(va)
    p.append(co)
    l.append(c)


    system('cls')
    h = len(p)
    if len(p) != 1:
        print(f'Llevas {h} registros')
    else: 
        print(f'Llevas {h} registro')

    c = int(input('Ingrese el código del producto: '))


i = len(v)
a = sum(p)
o = sum(v)
ma = max(v)
mi2 = len(mi)


system('cls')

print(f'La lista en la que se guardan los código es: {l}')
print(f'La lista de ventas es: {v}')
print(f'La lista de cantidades compradas es: {p}')
print(f'La lista de las compras superiores a $30.000 es: {mi}\n')

print(f'La cantidad de ventas realizadas fue de {i}')
print(f'El total de productos vendidos fueron {a}')
print(f'El total recuadado es de {o}')
print(f'EL valor de compra más alto fue {ma}')
print(f'La cantidad de compras superiores a $30.000 fueron {mi2}')
