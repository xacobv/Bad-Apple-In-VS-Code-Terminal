from PIL import Image
import pygame
import time

# Reference
ASCII_CHARS =  [".", ":", ";", "+", "*", "?", "%", "$", "#", "@"]

# Resizes the image
def resize_image(image, new_width = 125):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Converts rgb average to ASCII character
def pixel_to_ascii(image):
    width, height = image.size
    ascii_image = []

    for y in range(height):
        
        row = ""
        
        for x in range(width):

            r, g, b = image.getpixel((x, y))
            mean = (r + g + b) // 3

            if mean in range(0, 25):
                row += "."
            elif mean in range(25, 50):
                row += ":"
            elif mean in range(50, 75):
                row += ";"
            elif mean in range(75, 100):
                row += "+"
            elif mean in range(100, 125):
                row += "*"
            elif mean in range(125, 150):
                row += "?"
            elif mean in range(150, 175):
                row += "%"
            elif mean in range(175, 200):
                row += "$"
            elif mean in range(200, 225):
                row += "#"
            elif mean in range(225, 256):
                row += "@"
            else:
                row += " "
        ascii_image.append(row)

    return "\n".join(ascii_image)

# Plays bad_apple audio
pygame.mixer.init()
pygame.mixer.music.load("bad_apple_audio.mp3")
pygame.mixer.music.play()

# Gets each frame from bad_apple_frames pathway
for i in range(6759):
    image_path = "bad_apple_frames/frame" + str(i) +".jpg"
    image = Image.open(image_path)

    # Resizes image, converts average rgb value to ASCII characters, and then assigns it to the ascii_art var
    resized_image = resize_image(image)
    ascii_art = pixel_to_ascii(resized_image)

    # Prints final product
    print(ascii_art)

    # Waits between each frame
    time.sleep(1/50)

    # Clears console in order to prevent it from breaking
    print("\033c", end="")

# Stops music once the frames stop
pygame.mixer.music.stop()
