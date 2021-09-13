
import cv2 as cv  # OpenCV 3.4.7.28
import numpy as np
from matplotlib import pyplot as plt

directorio = 'files/imagenes/'

imagenes = ['lena_color_512.tif', 'peppers_color.tif']

def cv2_imshow(windowName, img):
    cv.imshow(windowName, img)
    cv.waitKey(0)
    cv.destroyAllWindows() 

for file in imagenes:
    
    # imread abre las imagenes como bgr
    bgr = cv.imread(directorio + file)
    # para voltear el arreglo a rgb:
    rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
    # grayscale
    grayscale = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)
    # yuv
    yuv = cv.cvtColor(rgb, cv.COLOR_RGB2YUV)
    # hsv
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)
    
    # RGB como escala de grises
    r = rgb[:,:,0]
    g = rgb[:,:,1]
    b = rgb[:,:,2]
    
    # Mostrar los canales RGB
    rgb_array = np.concatenate((r,g,b), axis = 1)
    cv2_imshow('RGB', rgb_array)
    
    # Mostrar las 3 imagenes RGB
    fig, (ax_r, ax_g, ax_b) = plt.subplots(ncols=3, figsize=(24, 8),
                                   sharex=True, sharey=True)
    ax_r.set_title('Canal R')
    ax_r.imshow(r, cmap = 'gray')
    ax_g.set_title('Canal G')
    ax_g.imshow(g, cmap = 'gray')
    ax_b.set_title('Canal B')
    ax_b.imshow(b, cmap = 'gray')
    
    # Guardar la figura RGB
    fig.savefig(file + 'rgb_opencv.png')
    
    # HSV como escala de grises
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    
    # Mostrar los canales hsv
    hsv_array = np.concatenate((h, s, v), axis=1)
    cv2_imshow('HSV', hsv_array)
    
    # Mostrar las 3 imagenes HSV
    fig, (ax_h, ax_s, ax_v) = plt.subplots(ncols=3, figsize=(24, 8),
                                   sharex=True, sharey=True)
    ax_h.set_title('Canal H')
    ax_h.imshow(h, cmap = 'gray')
    ax_s.set_title('Canal S')
    ax_s.imshow(s, cmap = 'gray')
    ax_v.set_title('Canal V')
    ax_v.imshow(v, cmap = 'gray')
    
    # Guardar la figura HSV
    fig.savefig(file + 'hsv_opencv.png')