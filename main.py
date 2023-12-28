import random
from PIL import Image, ImageDraw
import epd7in5_V2  # Importing the Waveshare 7.5 inch V2 library
import os
import time
import logging

# Generate a random abstract image
def generate_abstract_image(width, height):
    image = Image.new('1', (width, height), 1)  # '1' for black and white
    draw = ImageDraw.Draw(image)

    for _ in range(100):  # Number of shapes
        x0 = random.randint(0, width)
        y0 = random.randint(0, height)
        x1 = random.randint(x0, width)
        y1 = random.randint(y0, height)
        color = 0 if random.choice([True, False]) else 1  # 0 for black, 1 for white
        draw.ellipse([(x0, y0), (x1, y1)], fill=color)

    return image

# Display the image on the e-ink display
def display_on_eink(image):
    logging.basicConfig(level=logging.DEBUG)
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.display(epd.getbuffer(image))
    time.sleep(2)  # Time for the display to refresh
    epd.sleep()

# Shut down the Raspberry Pi
def shutdown_pi():
    os.system("sudo shutdown now")

# Main function
def main():
    width, height = 800, 480  # Resolution for Waveshare 7.5 inch V2 display
    abstract_image = generate_abstract_image(width, height)
    display_on_eink(abstract_image)

    # Wait a few seconds before shutting down
    time.sleep(10)
    shutdown_pi()

if __name__ == "__main__":
    main()
