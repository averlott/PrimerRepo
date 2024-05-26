#eju06-2

nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
dir = input('Ingrese su dirección: ')
tel = input('Ingrese su teléfono: ')

datos = {
  'nombre': nombre
  ,'edad': edad
  ,'dir': dir
  ,'tel': tel
}

#print(datos)

print(f'{datos['nombre']} tiene {datos['edad']} años, vive en {datos['dir']} y su número de teléfono es {datos['tel']}.')

               




