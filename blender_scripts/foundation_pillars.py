import matplotlib.pyplot as plt

length = 6
width = 5

cols = 5
rows = 4

col_spacing = length / (cols - 1)
row_spacing = width / (rows - 1)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, length + 1)
ax.set_ylim(-1, width + 1)

for i in range(cols):
    for j in range(rows):
        x = i * col_spacing
        y = j * row_spacing
        ax.plot(x, y, 'ko')
        ax.text(x + 0.1, y + 0.1, f"{x:.2f}m,{y:.2f}m", fontsize=8)

ax.set_title("Układ słupów fundamentowych - domek 6x5 m (siatka 5x4 = 20 słupków)")
ax.set_xlabel("Długość (m)")
ax.set_ylabel("Szerokość (m)")
ax.set_aspect('equal')
ax.grid(True)

plt.tight_layout()
plt.show()