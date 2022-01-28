import os
import time
import logging
import requests
from libs.functions import get_icon, indent, paste 
from datetime import datetime
from libs.waveshare_epd import epd2in7
from PIL import Image, ImageDraw, ImageFont
from settings import API_KEY

pic_dir = '/home/pi/eink-2in7/pics'

img_dir = '/home/pi/eink-2in7/images/jpg/'

FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

lat = "41.902756"
lon = "-88.337706"
exclude = "minutely,hourly"
units = "imperial"

openWeatherURL = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&exclude=" + exclude + "&units=" + units + "&appid=" + API_KEY


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

    response = requests.get(openWeatherURL)
    responseJson = response.json()
    responseCurr = responseJson['current']

    curTemp = str(round(responseCurr['temp']))
    curFeel = str(round(responseCurr['feels_like'])) + '°'
    curDesc = responseCurr['weather'][0]['description'].title().split(' ')

    curDesc1 = curDesc[0]
    curDesc2 = curDesc[1] 

 
    #time = dt.strftime('%a %m/%d %I:%M %p')

    logo = get_icon()
    image.paste(logo, (20, 30))

    draw.text((indent(curFeel,tempText,w)+20, 2), curFeel, font=tempText, fill=0, align='left')
    draw.text((indent(curDesc1,condText,w), 95), curDesc1, font=condText, fill=0, align='left')
    draw.text((indent(curDesc2,condText,w), 150), curDesc2, font=condText, fill=0, align='left')


    display.display(display.getbuffer(image))


except IOError as e:
    print(e)