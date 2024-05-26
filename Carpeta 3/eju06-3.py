#eju06-3

frutas = {
  'platano': 1.35
  ,'manzana': 0.8
  ,'pera': 0.85
  ,'naranja': 0.7
}

#print(frutas)

fruta = input('Ingrese el nombre de la fruta que desea comprar: ').lower()
kilos = float(input('Ingrese la cantidad de kilos de fruta que desea comprar: '))

if fruta in frutas:
    print(f'El precio de {kilos} kilos de {fruta} es {round(frutas[fruta]*kilos,2)}.')
else:
    print(f'{fruta} no se encuentra disponible.')

               




