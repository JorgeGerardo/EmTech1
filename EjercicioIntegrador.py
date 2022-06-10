venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
#Productos
productos = [["1","Maiz",285,55],["2","Pepino",334.72],["3","Tomate verde",129]]

#Input's
cajassolicitadas = int(input('Numero de cajas a comprar: '))
id = input('seleccione el id del producto: ')

indice1 = 0
for i in range(3):
    if(productos[i][0].__contains__(id)):
        indice1 = i








#Total de ventas-----------------------------------------------------------------------------------------
totalVentas = [[1,0],[2,0],[3,0]]


for i in range(len(venta_productos)):
    if venta_productos[i][0] == 1:
        totalVentas[0][1] += venta_productos[i][1]
    elif venta_productos[i][0] == 2:
        totalVentas[1][1] += venta_productos[i][1]
    elif venta_productos[i][0] == 3:
        totalVentas[2][1] += venta_productos[i][1]

print(totalVentas)
#------------------------------------------------------------------------------------------------------







#Salidas------------------------------------------------------------------------------------------------------
descuento = False
if totalVentas[int(id)][1]<1500:
    descuento = True


print("\n\n-----------------------------------------------------\n\n")
print("Producto es: " + str(productos[indice1][1]))
print("Precio por caja es: " + str(productos[indice1][2]))

totalpagar = float(cajassolicitadas*productos[indice1][2])

if cajassolicitadas<=99:
    totalpagar +=1500

if descuento:
    totalpagar = totalpagar*0.8
    totalpagar -=1500
print("Aplica descuento del 20%: " + str(descuento))


print("Total a pagar: " + str(totalpagar))
print("-----------------------------------------------------\n\n")



