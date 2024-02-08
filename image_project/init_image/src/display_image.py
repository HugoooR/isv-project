import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def show_image(image):
    image = Image.open(image)
    plt.imshow(image)
    # plt.show()