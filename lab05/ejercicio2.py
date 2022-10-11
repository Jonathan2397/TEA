#Tendencias e Innovacion en Tecnologia Agricola
try:
    entrada = input("Ingrese el nombre del archivo: ")
    archivo = open(entrada)
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, archivo no existe")

#print(archivo.read())