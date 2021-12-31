import os
import time

from libs.waveshare_epd import epd2in7

from PIL import Image, ImageDraw, ImageFont

pic_dir = '/home/pi/eink-2in7/pics'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

try:
    # Display init, clear
    display = epd2in7.EPD()
    display.init()
    display.Clear(0) # 0: Black, 255: White

    w = display.height
    h = display.width
    print('width:', w)
    print('height:', h)

    #### IMAGE CODE ####
    #body = ImageFont.truetype(os.path.join(pic_dir,'NotoMono-Regular.ttf'), 36, index=0)
    body = ImageFont.truetype(FONT, 36, index=0)

    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)

    draw.text((0, 0), 'Blah blah some words.', font=body, fill=0, align='left')

    display.display(display.getbuffer(image))


except IOError as e:
    print(e)
