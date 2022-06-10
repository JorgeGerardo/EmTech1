#Productos
productos = [["1","Maiz",285,55],["2","Pepino",334.72],["3","Tomate verde",129]]

#Input's
cajassolicitadas = int(input('Numero de cajas a comprar: '))
id = input('seleccione el id del producto: ')

indice1 = 0
for i in range(3):
    if(productos[i][0].__contains__(id)):
        indice1 = i


#Salidas
print("\n\n-----------------------------------------------------\n\n")
print("Producto es: " + str(productos[indice1][1]))
print("Precio por caja es: " + str(productos[indice1][2]))

totalpagar = float(cajassolicitadas*productos[indice1][2])
if cajassolicitadas<=99:
    totalpagar +=1500

print("Total a pagar: " + str(totalpagar))
print("-----------------------------------------------------\n\n")



