def cuenta_palabras(texto):
    palabra_frecuencia = {}
    palabras = texto.split(" ")
    for palabra in palabras:
        if palabra in palabra_frecuencia:
            palabra_frecuencia[palabra] += 1
        else:
            palabra_frecuencia[palabra] = 1
    return palabra_frecuencia

def palabra_mas_repetida(diccionario):
    max_palabra = ''
    max_frecuencia = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

texto = input("Ingrese un texto: ")

#print(cuenta_palabras(texto))

for palabra, frecuencia in cuenta_palabras(texto).items():
    print(f'{palabra}: {frecuencia}')

max_palabra, max_frecuencia = palabra_mas_repetida(cuenta_palabras(texto))

print(f'La palabra mas repetida es "{max_palabra}" y su frecuencia es "{max_frecuencia}".')