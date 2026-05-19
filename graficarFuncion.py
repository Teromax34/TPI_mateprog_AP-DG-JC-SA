import matplotlib.pyplot as plt

x = []
a = []
b = []
c = []
masBarato = []
n = 0

for i in range(0,51,5):
    x.append(i)

    a.append(40*i + 200)
    b.append(70*i + 50)
    c.append(-2*i**2 + 80*i + 100)

    if a[n] <= b[n] and a[n] <= c[n]:
        masBarato.append(a[n])
    elif b[n] < a[n] and b[n] < c[n]:
        masBarato.append(b[n])
    else:
        masBarato.append(c[n])
    
    n += 1

plt.plot(x,a,label="40x+200")
plt.plot(x,b,label="70x+50")
plt.plot(x,c,label="-2x^2+80x+100")
plt.plot(x,masBarato,label="plan mas economico")
plt.grid(True)
plt.legend()
plt.show()
