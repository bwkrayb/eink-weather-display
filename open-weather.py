import os
import time
import logging
import requests
import json
from libs.functions import get_icon, indent, paste, write_weather 
from datetime import datetime
from libs.waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont
from settings import API_KEY

pic_dir = '/home/pi/eink-2in7/pics'
data_dir = '/home/pi/eink-2in7/data/'
img_dir = '/home/pi/eink-2in7/images/jpg/'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

try:
    # Display init, clear
    display = epd2in7.EPD()
    display.init()
    display.Clear(0) # 0: Black, 255: White

    w = display.height
    h = display.width
    #print('width:', w) 264
    #print('height:', h) 176

    #### IMAGE CODE ####
    tempText = ImageFont.truetype(FONT, 90, index=0)
    bodyText = ImageFont.truetype(FONT, 30, index=0)
    timeText = ImageFont.truetype(FONT, 20, index=0)
    condText = ImageFont.truetype(FONT, 40, index=0)
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    dt = datetime.now()

    write_weather()
    time.sleep(5)
    f = open(data_dir + 'weather.json')
    responseStr = f.read()
    responseJson = json.loads(responseStr)
    responseCurr = responseJson['current']

    curTemp = str(round(responseCurr['temp'])) + '°'
    curFeel = str(round(responseCurr['feels_like'])) + '°'
    curDesc = responseCurr['weather'][0]['description'].title().split()
    curID = responseCurr['weather'][0]['id']

    if len(curDesc) > 2:
        custDesc = get_desc(curID).split()
        curDesc1 = custDesc[0]
        curDesc2 = custDesc[1]
    elif len(curDesc) == 2:
        curDesc1 = curDesc[0]
        curDesc2 = curDesc[1]
    else:
        curDesc1 = curDesc[0] 

    logo = get_icon(curID)
    image.paste(logo, (20, 30))

    draw.text((indent(curTemp,tempText,w)+20, 2), curTemp, font=tempText, fill=0, align='left')
    draw.text((indent(curDesc1,condText,w), 90), curDesc1, font=condText, fill=0, align='left')
    if len(curDesc) > 1:
        draw.text((indent(curDesc2,condText,w), 130), curDesc2, font=condText, fill=0, align='left')


    display.display(display.getbuffer(image))
    
    f.close()

except IOError as e:
    print(e)
    f.close()
