import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Wymiary domku
length = 6  # metry (dłuższy bok)
width = 5   # metry (krótszy bok)

# Liczba słupków
cols = 5  # wzdłuż długości (6 m)
rows = 4  # wzdłuż szerokości (5 m)

# Oblicz rozstawy
col_spacing = length / (cols - 1)
row_spacing = width / (rows - 1)

# Rozmiar wykresu
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, length + 1)
ax.set_ylim(-1, width + 1)

# Dodaj słupki
for i in range(cols):
    for j in range(rows):
        x = i * col_spacing
        y = j * row_spacing
        ax.plot(x, y, 'ko')  # czarne kropki jako słupki
        ax.text(x + 0.1, y + 0.1, f"{x:.2f}m,{y:.2f}m", fontsize=8)

# Opis
ax.set_title("Układ słupów fundamentowych - domek 6x5 m (siatka 5x4 = 20 słupków)")
ax.set_xlabel("Długość (m)")
ax.set_ylabel("Szerokość (m)")
ax.set_aspect('equal')
ax.grid(True)

plt.tight_layout()
plt.show()
