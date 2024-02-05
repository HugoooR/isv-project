import imageio
from PIL import Image

def creer_gif(tableau_images, output_path, duree=0.5):
    gif = []

    for img in tableau_images:
        gif.append(Image.fromarray(img))

    # Enregistrer le GIF
    imageio.mimsave(output_path, gif, duration=duree)
