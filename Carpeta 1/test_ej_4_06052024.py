def cuenta_palabras(texto):
    palabra_frecuencia = {}
    palabras = texto.split(" ")
    for palabra in palabras:
        if palabra in palabra_frecuencia:
            palabra_frecuencia[palabra] += 1
        else:
            palabra_frecuencia[palabra] = 1
    return palabra_frecuencia

texto = input("Ingrese un texto: ")

#print(cuenta_palabras(texto))

for palabra, frecuencia in cuenta_palabras(texto).items():
    print(f'{palabra}: {frecuencia}')