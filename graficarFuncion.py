import matplotlib.pyplot as plt

x = []
a = []
b = []
c = []

for i in range(0,51,5):
    x.append(i)

    a.append(40*i + 200)
    b.append(70*i + 50)
    c.append(-2*i**2 + 80*i + 100)

plt.plot(x,a,label="40x+200")
plt.plot(x,b,label="70x+50")
plt.plot(x,c,label="-2x^2+80x+100")
plt.grid(True)
plt.legend()
plt.show()
