import numpy as np
from skimage import io
from skimage import color
import os

directorio = 'imagenes/'
files = os.listdir(directorio)
imagen = io.imread(directorio + "lena_color_512.tif")
imagenSalida = []

imgGray = color.rgb2gray(imagen)

for x in range(1,len(imgGray)-2,2):
    temporal = []
    for y in range(1,len(imgGray)-2,2):
        suma = 0
        suma +=  imgGray[x - 1][y - 1]
        suma += imgGray[x][y - 1]
        suma += imgGray[x - 1][y]
        suma += imgGray[x][y]
        promedio = suma /4
        temporal.append(promedio)

    imagenSalida.append(temporal)

imagenSalida2 = []
for x in range(1,len(imgGray)-2,2):
    temporal = []
    for y in range(1,len(imgGray)-2,2):

        temporal.append(imgGray[x-1][y-1])

    imagenSalida2.append(temporal)


io.imshow(imgGray)
io.show()

io.imshow(np.array(imagenSalida))
io.show()

io.imshow(np.array(imagenSalida2))
io.show()







