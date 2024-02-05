from resize_image import redimensionner_image
from PIL import Image

def fusionner_horizontalement(image1, image2):
    nouvelle_largeur = int(image2.size[0] * (image1.size[1] / image2.size[1]))
    nouvelle_hauteur = image1.size[1]
    image2_redimensionnee = redimensionner_image(image2, nouvelle_largeur, nouvelle_hauteur)

    result = Image.new('RGB', (image1.width + image2_redimensionnee.width, image1.height))
    result.paste(image1, (0, 0))
    result.paste(image2_redimensionnee, (image1.width, 0))

    return result
