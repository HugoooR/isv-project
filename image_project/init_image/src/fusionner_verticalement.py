from PIL import Image
import numpy as np

def fusionner_verticalement(image1, image2):
    image2_redimensionnee = image2
    
    if (image1.size[0] != image2.size[0]):
        ratio = image2.width / image2.height
        
        new_height = int(image1.width / ratio)
        image2_redimensionnee = image2.resize((image1.width, new_height))

    result = Image.new('RGB', (image1.width, image1.height + image2_redimensionnee.height))
    result.paste(image1, (0, 0))
    result.paste(image2_redimensionnee, (0, image1.height))
    
    return result

