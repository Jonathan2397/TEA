#Tendencias e Innovacion en Tecnologia Agricola
cadena = "X-DSPAM-Confidence:0.8475"
inicio = cadena.find(":") + 1
final = len(cadena)
numero = float(cadena[inicio:final])
print(numero)
print(inicio, final)
print(type(numero))
