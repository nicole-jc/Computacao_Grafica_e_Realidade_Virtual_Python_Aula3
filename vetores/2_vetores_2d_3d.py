import matplotlib.pyplot as plt
# 2. Vetores no espaço vetorial 2D e 3D

# Vetor 2D
x = [0, 3]
y = [0, 2]

plt.quiver(
    x[0], y[0],
    x[1] - x[0], y[1] - y[0],
    angles='xy',
    scale_units='xy',
    scale=1
)

plt.xlim(0, 4)
plt.ylim(0, 3)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Vetor no espaço 2D")
plt.grid()
plt.show()

# Vetor 3D
x, y, z = 3, 2, 4

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, x, y, z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Vetor no espaço 3D")

plt.show()