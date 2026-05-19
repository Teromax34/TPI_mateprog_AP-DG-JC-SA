import matplotlib.pyplot as plt

x = []
a = []

for i in range(0,50):
    x.append(i)

    a.append(40*i + 200)

plt.plot(x,a)

plt.show()
