import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
matrix = np.random.rand(10, 10)

plt.imshow(matrix, cmap='viridis')
plt.colorbar()
plt.title("Тепловая карта")
plt.savefig("4.png")
plt.show()
