from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def redimensionner_image(image, nouvelle_largeur, nouvelle_hauteur):
    a0, b0, _ = image.shape

    ratio_lignes = a0 / nouvelle_largeur
    ratio_colonnes = b0 / nouvelle_hauteur

    image_sortie = np.zeros((nouvelle_largeur, nouvelle_hauteur, 3), dtype=np.uint8)
    for ligne in range(nouvelle_largeur):
        for col in range(nouvelle_hauteur):
            for i in range(3):
                image_sortie[ligne, col, i] = image[int(ligne * ratio_lignes), int(col * ratio_colonnes), i]

    return Image.fromarray(image_sortie)