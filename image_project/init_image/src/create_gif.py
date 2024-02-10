import imageio
import numpy as np

from PIL import Image
from .resize_image import redimensionner_image

def creer_gif(tableau_images, duree):
    gif = []

    for img in tableau_images:
        img_red = img
    
        img_red = img_red.convert("RGB") 
        if (tableau_images[0].size != img.size):
            img_red = img_red.resize(tableau_images[0].size)
            
        gif.append(img_red)

    # Enregistrer le GIF
    imageio.mimsave('media/new_gif.gif', gif, duration=duree, loop=0)
