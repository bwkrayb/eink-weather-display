import os
import time
import logging
from libs.functions import get_icon, indent, paste 
from datetime import datetime
from libs.waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont

pic_dir = '/home/pi/eink-2in7/pics'

img_dir = '/home/pi/eink-2in7/images/jpg/'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

#FONT = '/home/pi/eink-2in7/pics/PressStart2P-Regular.ttf'

#FONT = '/home/pi/eink-2in7/pics/Monoton-Regular.ttf'

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
    tempText = ImageFont.truetype(FONT, 90, index=0)
    bodyText = ImageFont.truetype(FONT, 30, index=0)
    timeText = ImageFont.truetype(FONT, 20, index=0)
    condText = ImageFont.truetype(FONT, 40, index=0)
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    dt = datetime.now()
    temp = os.popen('curl -s wttr.in/?format="%t"').read()
    time = dt.strftime('%a %m/%d %I:%M %p')
    cond = os.popen('curl -s wttr.in/?format="%C"').read()
    if w < condText.getsize(cond)[0]:
        logging.info("Condition " + cond + " is too wide for display. Font size reduced.")
        condText = ImageFont.truetype(FONT, 30, index=0)

    location = 'St Charles, IL'
    
    logo = get_icon()
    image.paste(logo, (20, 30))
    

    draw.text((indent(temp.strip('+F'),tempText,w)+20, 2), temp.strip('+F'), font=tempText, fill=0, align='left')
    draw.text((indent(cond,condText,w), 95), cond.title(), font=condText, fill=0, align='left')
    draw.text((indent(time,timeText,w), 150), time, font=timeText, fill=0, align='left')


    display.display(display.getbuffer(image))


except IOError as e:
    print(e)
