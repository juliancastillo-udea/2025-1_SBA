import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Parámetros del autómata
tablero_tamanio = 50            # Número de filas
ancho_tablero = tablero_tamanio * 2  # Número de columnas

# Inicializar el tablero como un array de NumPy lleno de ceros
tablero = np.zeros((tablero_tamanio, ancho_tablero), dtype=int)

# Condición inicial: colocar un '1' en el centro de la primera fila
tablero[0, ancho_tablero // 2] = 1

# Configuración de la visualización (una única figura)
plt.ion()  # Activar modo interactivo
fig, ax = plt.subplots(figsize=(10, 10))
im = ax.imshow(tablero, cmap='gray_r')
ax.set_title("Progreso: fila 0", fontsize=16)
ax.axis('off')
plt.show()

# Evolución del autómata aplicando la Regla 90
for i in tqdm(range(1, tablero_tamanio), desc="Calculando..."):
    for j in range(ancho_tablero):
        # Obtener los vecinos de la fila anterior con control de bordes
        if j == 0:
            izq = 0
            cen = tablero[i - 1, j]
            der = tablero[i - 1, j + 1]
        elif j == ancho_tablero - 1:
            izq = tablero[i - 1, j - 1]
            cen = tablero[i - 1, j]
            der = 0
        else:
            izq = tablero[i - 1, j - 1]
            cen = tablero[i - 1, j]
            der = tablero[i - 1, j + 1]
        
        # Aplicar la Regla 90:
        # 000 -> 0, 001 -> 1, 010 -> 0, 011 -> 1, 100 -> 1, 101 -> 0, 110 -> 1, 111 -> 0
        if izq == 0 and cen == 0 and der == 0:
            tablero[i, j] = 0
        elif izq == 0 and cen == 0 and der == 1:
            tablero[i, j] = 1
        elif izq == 0 and cen == 1 and der == 0:
            tablero[i, j] = 0
        elif izq == 0 and cen == 1 and der == 1:
            tablero[i, j] = 1
        elif izq == 1 and cen == 0 and der == 0:
            tablero[i, j] = 1
        elif izq == 1 and cen == 0 and der == 1:
            tablero[i, j] = 0
        elif izq == 1 and cen == 1 and der == 0:
            tablero[i, j] = 1
        elif izq == 1 and cen == 1 and der == 1:
            tablero[i, j] = 0

    # Actualizar la misma imagen con los nuevos datos del tablero
    im.set_data(tablero)
    ax.set_title(f"Progreso: fila {i}", fontsize=16)
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.ioff()
plt.show()
