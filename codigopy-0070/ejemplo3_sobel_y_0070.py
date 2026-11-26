# Alumno: Axel Guzman | NC: 0070 | Lista: 26
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from funciones_frecuencia_0070 import cargar_imagen, obtener_espectro, aplicar_filtro_frecuencia, normalizar_visualizacion, guardar_grafica
img = cargar_imagen()
sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]], dtype=np.float32)
ry = aplicar_filtro_frecuencia(img, sy)
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(img, cmap='gray'); ax[0].set_title('Original (#26)'); ax[0].axis('off')
ax[1].imshow(obtener_espectro(ry), cmap='gray'); ax[1].set_title('Espectro Sobel Y'); ax[1].axis('off')
ax[2].imshow(normalizar_visualizacion(ry), cmap='gray'); ax[2].set_title('Respuesta Sobel Y'); ax[2].axis('off')
plt.tight_layout(); guardar_grafica(fig, '03_sobel_y.png'); plt.close(fig)