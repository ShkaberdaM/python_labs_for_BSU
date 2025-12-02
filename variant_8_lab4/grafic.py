import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0, 5, 100)
z1 = 2 * np.sin(3*np.pi - 2*a)**2 * np.cos(5*np.pi + 2*a)**2
z2 = 0.25 - 0.25 * np.sin(2.5*np.pi - 8*a)

fig, ax1 = plt.subplots()

ax1.plot(a, z1, 'b-', label="z1")
ax1.set_xlabel("a")
ax1.set_ylabel("z1", color="b")

ax2 = ax1.twinx()
ax2.plot(a, z2, 'r--', label="z2")
ax2.set_ylabel("z2", color="r")

fig, ax1 = plt.subplots()

ax1.plot(a, z1, 'b-', label="z1")
ax2 = ax1.twinx()
ax2.plot(a, z2, 'r--', label="z2")

fig.legend(loc="upper right")

plt.title("Y")
plt.tight_layout()
plt.savefig("1.png")
plt.show()
