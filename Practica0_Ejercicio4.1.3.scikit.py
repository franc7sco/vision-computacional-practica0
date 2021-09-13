
import skimage as si # scikit-image 0.15.0
import matplotlib.pyplot as plt

directorio = 'files/imagenes/'



imagenes = ['lena_color_512.tif', 'peppers_color.tif']

for file in imagenes:
    
    rgb = si.io.imread(directorio + file, plugin = 'simpleitk')
    # grayscale
    grayscale = si.color.rgb2gray(rgb)
    # yuv
    yuv = si.color.rgb2yuv(rgb)
    # hsv
    hsv = si.color.rgb2hsv(rgb)
    
    # RGB como escala de grises
    r = rgb[:,:,0]
    g = rgb[:,:,1]
    b = rgb[:,:,2]
    rgb_array = []
    
    # HSV como escala de grises
    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]
    
    # Cambiar como rgb, para que se pueda "tintar" la imagen
    r_asrgb = [1,0,0] * si.color.gray2rgb(r)
    g_asrgb = [0,1,0] * si.color.gray2rgb(g)
    b_asrgb = [0,0,1] * si.color.gray2rgb(b)
    
    # Mostrar las 3 imagenes RGB
    fig, (ax_r, ax_g, ax_b) = plt.subplots(ncols=3, figsize=(24, 8),
                                   sharex=True, sharey=True)
    ax_r.set_title('Canal R')
    ax_r.imshow(r_asrgb)
    ax_g.set_title('Canal G')
    ax_g.imshow(g_asrgb)
    ax_b.set_title('Canal B')
    ax_b.imshow(b_asrgb)
    
    # Guardar la figura RGB
    fig.savefig(file + 'rgb_scikit.png')
    
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
    fig.savefig(file + 'hsv_scikit.png')