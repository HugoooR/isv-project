from PIL import Image
import numpy as np

def fusionner_horizontalement(image1, image2):
    image2_redimensionnee = image2

    if (image1.size[1] != image2.size[1]):
        ratio = image2.height / image2.width
        new_width = int(image1.height * ratio)
        image2_redimensionnee = image2.resize((new_width, image1.height))

    result = Image.new('RGB', (image1.width + image2_redimensionnee.width, image1.height))
    result.paste(image1, (0, 0))
    result.paste(image2_redimensionnee, (image1.width, 0))

    return result
