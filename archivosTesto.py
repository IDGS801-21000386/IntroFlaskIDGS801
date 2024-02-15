from io import open


archivo1 = open("archivo.txt", "a") # Para poder escribir sobre el archivo
archivo1.write("\nHOLAAAAAAAAAAAAAAAAAAAA SALUDOS DE ERICK")
archivo1.close()



"""
archivo1 = open("archivo.txt", "r") # Para solo lectura
print(archivo1.read())
archivo1.seek(0) # Para que vuelva desde la posicion 0 del archivo
print(archivo1.read())

for datos in archivo1: # Imprime linea por linea los datos que se encuentren en el archivo
    #print(datos)
    print(datos.rstrip())
archivo1.close()

"""
# print(archivo1.readlines()) #Lo lee todo dentro de una sola linea mediante []
