from matplotlib import pyplot as plt

plt.xkcd()


dev_x =[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] 


py_devx = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_devy = [27, 28, 29, 30, 31, 32, 33, 34, 36, 38, 39]
plt.plot(py_devx, py_devy, label="Python")

js_devy = [24, 25, 27, 28, 30, 30, 31, 32, 32, 34, 35]
plt.plot(py_devx, js_devy, label="JavaScript")

dev_y = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36]
plt.plot(dev_x, dev_y, color="#444444", linestyle="--", label="All Devs")

plt.xlabel("ages")
plt.ylabel("Median Salary")
plt.title("Median salary")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plot.png")

plt.show()
