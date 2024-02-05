def convert_to_black_and_white(image):
    for x in range(image.width):
        for y in range(image.height):
            pixel_color = image.getpixel((x, y))

            if pixel_color != (255, 255, 255):
                image.putpixel((x, y), (0, 0, 0))