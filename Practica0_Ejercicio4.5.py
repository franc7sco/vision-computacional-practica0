
from matplotlib import pyplot as plt
import numpy as np


##### Imagen RAW

directorio = 'files/imagenes/'

# Hace un array con todos los datos del archivo en uint8
A = np.fromfile(directorio + 'rosa800x600.raw', dtype='uint8')

# Lo cambia de tamaño a 800x600
A = np.reshape(A, (800, 600))

# Lo muestra interpretándolo como una imagen en escala de grises
plt.imshow(A, cmap= 'gray')

# guardar imagen
plt.imsave('rosa.png', A, cmap = 'gray')