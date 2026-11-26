# Alumno: Axel Guzman | NC: 0070 | Lista: 26
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from funciones_frecuencia_0070 import cargar_imagen, obtener_espectro, aplicar_filtro_frecuencia, normalizar_visualizacion, guardar_grafica
img = cargar_imagen()
sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]], dtype=np.float32)
sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]], dtype=np.float32)
rx = aplicar_filtro_frecuencia(img, sx); ry = aplicar_filtro_frecuencia(img, sy)
mag = np.sqrt(rx**2 + ry**2)
fig, ax = plt.subplots(2, 3, figsize=(18, 10))
ax[0,0].imshow(img, cmap='gray'); ax[0,0].set_title('1. Original (#26)'); ax[0,0].axis('off')
ax[0,1].imshow(obtener_espectro(rx), cmap='gray'); ax[0,1].set_title('2. Espectro Sobel X'); ax[0,1].axis('off')
ax[0,2].imshow(obtener_espectro(ry), cmap='gray'); ax[0,2].set_title('3. Espectro Sobel Y'); ax[0,2].axis('off')
ax[1,0].imshow(normalizar_visualizacion(rx), cmap='gray'); ax[1,0].set_title('4. Respuesta Sobel X'); ax[1,0].axis('off')
ax[1,1].imshow(normalizar_visualizacion(ry), cmap='gray'); ax[1,1].set_title('5. Respuesta Sobel Y'); ax[1,1].axis('off')
ax[1,2].imshow(normalizar_visualizacion(mag), cmap='gray'); ax[1,2].set_title('6. Magnitud del Gradiente'); ax[1,2].axis('off')
plt.tight_layout(); guardar_grafica(fig, '04_comparacion_magnitud_gradiente.png'); plt.close(fig)