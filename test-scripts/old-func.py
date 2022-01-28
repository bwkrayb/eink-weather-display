import datetime
import os
import PIL
import time
import logging
import requests
import re
from settings import API_KEY
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

data_dir='/home/pi/eink-2in7/data/'

logging.basicConfig(level=logging.INFO,filename='/home/pi/eink-2in7/logs/eink.log')

def get_icon():
    """
    Get the icon for the current weather
    :return: Image of the icon
    """
    # using wttr.in, just use a simple word search to decide which icon will be used. Needs more testing.
    dt = datetime.now()
    weatherIcon = os.popen('curl -s wttr.in/?format="%C"').read().lower()
    if 5 <= int(dt.strftime('%H')) < 18:
        if 'sunny' in weatherIcon or 'clear' in weatherIcon:
            return Image.open("images/jpg/day_clear.jpg")
        elif 'partly' in weatherIcon:
            return Image.open("images/jpg/day_partial_cloud.jpg")
        elif 'overcast' in weatherIcon:
            return Image.open("images/jpg/overcast.jpg")
        elif 'cloudy' in weatherIcon:
            return Image.open("images/jpg/cloudy.jpg")
        elif 'rain' in weatherIcon:
            return Image.open("images/jpg/rain.jpg")
        elif 'fog' in weatherIcon or 'haze' in weatherIcon or 'mist' in weatherIcon:
            return Image.open("images/jpg/mist.jpg")
        elif 'snow' in weatherIcon:
            return Image.open("images/jpg/day_snow.jpg")
        else:
            logging.info("No icon set for " + weatherIcon)
            return Image.open("images/jpg/day_clear.jpg")
    else:
        if 'clear' in weatherIcon:
            return Image.open("images/jpg/night_clear.jpg")
        elif 'cloudy' in weatherIcon:
            return Image.open("images/jpg/night_partial_cloud.jpg")
        elif 'rain' in weatherIcon:
            return Image.open("images/jpg/night_rain.jpg")
        elif 'snow' in weatherIcon:
            return Image.open("images/jpg/night_snow.jpg")
        else:
            logging.info("No icon set for " + weatherIcon)
            return Image.open("images/jpg/night_clear.jpg")

def paste(image: Image, position: tuple = (0, 0)) -> None:
    """
    Paste an image onto the buffer
    :param image: Image to paste
    :param position: tuple position to paste at
    :return: None
    """
    image.paste(image, position)


def indent(input,font,width):
    return int((width - font.getsize(input)[0]) / 2)



def write_weather():
    f = open(data_dir +'weather.json', 'w')
    lat = "41.902756"
    lon = "-88.337706"
    exclude = "minutely,hourly"
    units = "imperial"

    openWeatherURL = "https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + lon + "&exclude=" + exclude + "&units=" + units + "&appid=" + API_KEY

    response = requests.get(openWeatherURL)
    responseJson = response.json()
    responseStr = str(responseJson)

    p = re.compile('(?<!\\\\)\'')
    finalStr = p.sub('\"', responseStr)

    f.write(finalStr)
    f.close()
