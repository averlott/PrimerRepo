#eju06-5

asignaturas = {
  'Matemáticas': 6
  ,'Física': 4
  ,'Química': 5
}

#print(asignaturas)

totalCreditos = 0

for asignatura,creditos in asignaturas.items():
  print(f'{asignatura} tiene {creditos} créditos')
  totalCreditos += creditos

print(f'El número total de créditos del curso es {totalCreditos}.')      




