from matplotlib import pyplot as plt
import numpy as np


def f(x,a,b,c):
    return a*x**2+b*x+c

xlist = np.arange(-10,10.1,0.1)
ylist = f(xlist, 3, 1, 4)

plt.figure(num=0, dpi=120)
plt.title("Parabola")
plt.xlabel("x-osa")
plt.ylabel("y-osa")
plt.plot(xlist, ylist, label="f(x)")
plt.plot(xlist, ylist**(1/2),"--g" ,label=r"f(x)$*(0.5)$")
plt.legend()
