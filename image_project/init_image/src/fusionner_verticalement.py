from .resize_image import redimensionner_image
from PIL import Image
import numpy as np

def fusionner_verticalement(image1, image2):
    image2_redimensionnee = image2
    
    if (image1.size[0] != image2.size[0]):
        nouvelle_largeur = image1.size[0]
        nouvelle_hauteur = int(image2.size[1] * (image1.size[0] / image2.size[0]))
        image2_redimensionnee = redimensionner_image(np.asarray(image2), nouvelle_largeur, nouvelle_hauteur)

    result = Image.new('RGB', (image1.width, image1.height + image2_redimensionnee.height))
    result.paste(image1, (0, 0))
    result.paste(image2_redimensionnee, (0, image1.height))
    
    return result
