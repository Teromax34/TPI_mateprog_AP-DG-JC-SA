A = [101, 102, 103, 104, 105, 106]
B = [104, 105, 106, 107, 108]
C = [102, 105, 109]
criticos = []
noCriticos = []
for i in range(101,110):
    if ((i in A)or(i in B))and(i in C) == True:
        criticos.append(i)
    else:
        noCriticos.append(i)

print(criticos)
print(noCriticos)



