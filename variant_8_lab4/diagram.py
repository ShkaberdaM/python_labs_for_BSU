import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(5, 0.5, 50)
y2 = np.random.normal(5, 0.5, 50)

x3 = np.random.normal(8, 0.5, 50)
y3 = np.random.normal(2, 0.5, 50)

plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, color='red', label='Кластер 1')
plt.scatter(x2, y2, color='blue', label='Кластер 2')
plt.scatter(x3, y3, color='green', label='Кластер 3')

plt.title("Точечная диаграмма трёх кластеров")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.savefig("2.png")
plt.show()
