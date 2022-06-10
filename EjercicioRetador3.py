from ctypes.wintypes import INT


cementokg = 40
yesokg = 30
capacidadtotalcamion = 3254

cementoSolicitado = int(input("Numero de costales de cemento solicitados: "))
yesoSolicitado = int(input("Numero de costales de yeso solicitados: "))
total = cementoSolicitado+yesoSolicitado;
print("Total a enviar: " + str(total))
if total >= capacidadtotalcamion/2:
    print("La entrega se puede realizar")
else:
    print("La entrega no se puede realizar")






