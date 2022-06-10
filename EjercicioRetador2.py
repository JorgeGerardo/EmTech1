municipios = []

for i in range(3):
    municipio = input("Escriba el nombre del municipio # " + str(i+1)+" ")
    habitantes = int(input("Escriba el numero de habitantes de " + municipio +" "))
    municipios.append([municipio,habitantes])
    nuevalista = [municipio,habitantes]
    municipios.append(nuevalista)

totalhabitantes = municipios[0][1]+municipios[1][1]+municipios[1][1];
promediohabitantes = totalhabitantes/3;
print("Total de habitantes: "+ str(totalhabitantes))
print("Promedio habitantes: " +str(promediohabitantes))