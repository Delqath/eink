import random
import os
import sys
from PIL import Image, ImageDraw

# Add the Waveshare e-Paper library to the system path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'e-Paper/RaspberryPi_JetsonNano/python'))
from lib.waveshare_epd import epd7in5_V2

# Generate a random abstract image
def generate_abstract_image(width, height):
    image = Image.new('1', (width, height), 255)  # 1-bit image, white background
    draw = ImageDraw.Draw(image)

    for _ in range(50):  # Number of shapes
        shape = random.choice(['ellipse', 'rectangle'])
        upper_left = (random.randint(0, width), random.randint(0, height))
        lower_right = (random.randint(upper_left[0], width), random.randint(upper_left[1], height))
        if shape == 'ellipse':
            draw.ellipse([upper_left, lower_right], outline=0)
        else:
            draw.rectangle([upper_left, lower_right], outline=0)

    return image

# Display the image on the e-ink display
def display_on_eink(image):
    epd = epd7in5_V2.EPD()  # Initialize the display
    epd.init()
    epd.display(epd.getbuffer(image))
    epd.sleep()

# Main function
def main():
    width, height = 800, 480  # Resolution for Waveshare 7.5 inch V2
    abstract_image = generate_abstract_image(width, height)
    display_on_eink(abstract_image)

if __name__ == "__main__":
    main()
