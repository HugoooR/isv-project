import imageio
import numpy as np

from PIL import Image
from .resize_image import redimensionner_image

def creer_gif(tableau_images, duree):
    gif = []

    for img in tableau_images:
        img_red = img
        
        img_red = img_red.convert("RGB") 
        
        if (tableau_images[0].size[1] != img.size[1]):
            nouvelle_largeur = int(img.size[0] * (tableau_images[0].size[1] / img.size[1]))
            nouvelle_hauteur = tableau_images[0].size[1]
            img_red = redimensionner_image(np.asarray(img), nouvelle_largeur, nouvelle_hauteur)

        gif.append(img_red)

    # Enregistrer le GIF // duree en ms
    imageio.mimsave('media/new_gif.gif', gif, duration=duree, loop=0)
