# Alumno: Axel Guzman | NC: 0070 | Lista: 26
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from funciones_frecuencia_0070 import cargar_imagen, obtener_espectro, guardar_grafica
img = cargar_imagen(); esp = obtener_espectro(img)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img, cmap='gray'); ax[0].set_title('Imagen Original #26 (Onda Senoidal 2D)'); ax[0].axis('off')
ax[1].imshow(esp, cmap='gray'); ax[1].set_title('Espectro de Frecuencia (FFT)'); ax[1].axis('off')
plt.tight_layout(); guardar_grafica(fig, '01_imagen_y_espectro.png'); plt.close(fig)