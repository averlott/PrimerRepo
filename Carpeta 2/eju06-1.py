#eju06-1

monedas = {
  'euro': '€'
  ,'dollar': '$'
  ,'yen': '¥'
}

#print(monedas)

moneda = input('Ingrese el nombre de una moneda para conocer su simbolo: ').lower()

if moneda in monedas:
    print(f'El simbolo de la moneda {moneda} es {monedas[moneda]}.')
else:
    print(f'El simbolo de la moneda {moneda} no se encuentra disponible.')
               




