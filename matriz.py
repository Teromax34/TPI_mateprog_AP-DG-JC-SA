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
  
print("promedio por servidor es de:")
for i in range(len(m[0])):
    suma=0
    for j in range(len(m)):
        suma +=m[j][i]
    print(suma/ len(m))

print("\nmatriz transpuesta:")
mt=[]
for i in range (len(m[0])):
    fila= []
    for j in range (len(m)):
        fila.append(m[j][i])
    mt.append(fila)
for fila in mt:
    print(fila)