from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def blend_images(img1, img2, blend_ratio):

    img2 = img2.resize(img1.size)

    array1 = np.array(img1)
    array2 = np.array(img2)

    blended_array = np.round(array1 * blend_ratio + array2 * (1 - blend_ratio)).astype(np.uint8)

    if blended_array.ndim == 2:
        blended_array = np.expand_dims(blended_array, axis=2)

    blended_img = Image.fromarray(blended_array, 'RGB')

    return blended_img

