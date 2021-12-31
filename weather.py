import os
import time
import logging
from libs.functions import get_icon, indent, paste 
from datetime import datetime
from libs.waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont

pic_dir = '/home/pi/eink-2in7/pics'

img_dir = '/home/pi/eink-2in7/images/jpg/'

#FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

FONT = '/home/pi/eink-2in7/pics/PressStart2P-Regular.ttf'

#FONT = '/home/pi/eink-2in7/pics/Monoton-Regular.ttf'

weatherTemp = os.popen('curl -s wttr.in/?format="%f"').read()
weatherTempShort = weatherTemp.lstrip('+F')

try:
    # Display init, clear
    display = epd2in7.EPD()
    display.init()
    display.Clear(0) # 0: Black, 255: White

    w = display.height
    h = display.width
    #print('width:', w)
    #print('height:', h)

    #### IMAGE CODE ####
    tempText = ImageFont.truetype(FONT, 72, index=0)
    bodyText = ImageFont.truetype(FONT, 30, index=0)
    timeText = ImageFont.truetype(FONT, 13, index=0)
    condText = ImageFont.truetype(FONT, 30, index=0)
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    dt = datetime.now()
    temp = os.popen('curl -s wttr.in/?format="%t"').read()
    time = dt.strftime('%a %m/%d %I:%M %p')
    cond = os.popen('curl -s wttr.in/?format="%C"').read()
    location = 'St Charles, IL'
    
    logo = get_icon()
    image.paste(logo, (20, 30))
    

    draw.text((68, 15), temp.strip('+F'), font=tempText, fill=0, align='left')
    draw.text((indent(cond,condText,w), 105), cond.upper(), font=condText, fill=0, align='left')
    draw.text((indent(time,timeText,w), 150), time, font=timeText, fill=0, align='left')


    display.display(display.getbuffer(image))


except IOError as e:
    print(e)
