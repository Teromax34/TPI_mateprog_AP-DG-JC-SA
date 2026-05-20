m= [
  [120,150,100],
  [200,180,220],
  [90,110,95]
]
print("el calculo promedio por función es: ")
for fila in m:
  total= 0
  for numero in fila:
    total += numero
  promedio= total/ len(fila)
  print(promedio)
