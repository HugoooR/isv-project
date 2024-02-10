from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def blend_images(img1, img2, blend_ratio, position):
    new_img1 = img1
    new_img2 = img2

    if (np.asarray(img1).shape[-1] or np.asarray(img2).shape[-1] == 4):
        # On regarde si l'image 1 a le canal alpha, si oui on l'enlève
        if (np.asarray(img1).shape[-1] == 4):
            new_img1 = new_img1.convert("RGB")
        else:
            new_img2 = new_img2.convert("RGB")
        
    the_new_img2 = new_img2

    # Ajuster la position de l'image 2 en fonction de la position relative
    x, y = position
    x *= -1
    y *= -1
    
    the_new_img2 = the_new_img2.crop((x, y, x + new_img1.width, y + new_img1.height))

    array1 = np.array(new_img1)
    array2 = np.array(the_new_img2)

    blended_array = np.round(array1 * blend_ratio + array2 * (1 - blend_ratio)).astype(np.uint8)

    if blended_array.ndim == 2:
        blended_array = np.expand_dims(blended_array, axis=2)

    blended_img = Image.fromarray(blended_array, 'RGB')

    return blended_img


