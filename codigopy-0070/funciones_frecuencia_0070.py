# Alumno: Axel Guzman | NC: 0070 | Lista: 26
import numpy as np, cv2, os
def cargar_imagen():
    x, y = np.ogrid[0:256, 0:256]
    return ((np.sin(x / 10) * np.cos(y / 10) + 1) * 127.5).astype(np.uint8)
def obtener_espectro(img):
    return 20 * np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))) + 1)
def aplicar_filtro_frecuencia(img, kernel):
    p = np.pad(img, 1, mode='reflect')
    kp = np.zeros(p.shape, dtype=np.float32)
    r, c = (p.shape[0] - 3) // 2, (p.shape[1] - 3) // 2
    kp[r:r+3, c:c+3] = kernel
    res = np.real(np.fft.ifft2(np.fft.fft2(p) * np.fft.fft2(np.fft.ifftshift(kp))))
    return res[1:-1, 1:-1]
def normalizar_visualizacion(img):
    return cv2.normalize(np.abs(img), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
def guardar_grafica(fig, nombre):
    os.makedirs('resultados-img-0070', exist_ok=True)
    fig.savefig(os.path.join('resultados-img-0070', nombre), dpi=150, bbox_inches='tight')
    print('Guardado:', nombre)