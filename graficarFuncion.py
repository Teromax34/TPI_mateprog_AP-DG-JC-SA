import matplotlib.pyplot as plt

x = []
a = []
b = []
c = []

for i in range(0,50):
    x.append(i)

    a.append(40*i + 200)
    b.append(70*i + 50)
    c.append(-2*i**2 + 80*i + 100)

plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)

plt.show()
