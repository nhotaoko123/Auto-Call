# sudo i2cdetect -y 1
import time
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

#                                                               +----------------------+       +-------------------------+
#                                                               |                   Vcc| <---> | 1 *                3.3V |
#                                                               |                      |       |                         |
#                                                               |                   Gnd| <---> | 9  **            Ground |
#                                                               |    OLED              |       |         Pi GPIO         |
#                                                               |                   SCL| <---> | 5               I2C SCL |
#                                                               |                      |       |                         |
#                                                               |                   SDA| <---> | 3               I2C SCA |
#                                                               +----------------------+       +-------------------------+

#                                                                               +----------------------+
#                                                                               | Mail:                |
#                                                                               |                      |
#                                                                               | Send:                |
#                                                                               |                      |
#                                                                               | IP:                  |
#                                                                               |                      |
#                                                                               | File:                |
#                                                                               +----------------------+
# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.
font = ImageFont.load_default()

# font = ImageFont.truetype('Minecraftia.ttf', 8)
class display():
    def display_to_LCD(email, send_email, file_name):

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        cmd = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )

        # Write two lines of text.
        draw.text((x, top),       "MAIL: " + str(email),  font=font, fill=255)
        draw.text((x, top+16),     "SEND: "+ str(send_email), font=font, fill=255)
        draw.text((x, top+32),    "IP: " + str(IP,'utf-8'),  font=font, fill=255)
        draw.text((x, top+48),       "FILE: " + str(file_name),  font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()
        time.sleep(.1)