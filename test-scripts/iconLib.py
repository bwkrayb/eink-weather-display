import datetime
import os
import PIL
import time
import logging
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def get_icon(weatherID):
    """
    Get the icon for the current weather
    :return: Image of the icon
    """
    dt = datetime.now()
    thunder = (200,201,202,210,211,212,221,230,231,232)
    drizzle = (300,301,301,310,311,312,313,314)
    lightRain = (500,520)
    heavyRain = (501,502,503,504,511,521,522,531)
    snow = (600,601,602,611,612,613,615,616,620,621,622)
    fogMist = (701,721,741)
    ptCloud = (801,802,803)
    clear = (800,999)
    cloudy = (804,998)
    if 5 <= int(dt.strftime('%H')) < 18:
        if weatherID in clear:
            return Image.open("images/jpg/day_clear.jpg")
        elif weatherID in ptCloud:
            return Image.open("images/jpg/day_partial_cloud.jpg")
        elif weatherID in cloudy:
            return Image.open("images/jpg/cloudy.jpg")
        elif weatherID in lightRain:
            return Image.open("images/jpg/rain.jpg")
        elif weatherID in fogMist:
            return Image.open("images/jpg/mist.jpg")
        elif weatherID in snow:
            return Image.open("images/jpg/day_snow.jpg")
        else:
            logging.info("No icon set for " + str(weatherID))
            return Image.open("images/jpg/day_clear.jpg")
    else:
        if weatherIcon == clear:
            return Image.open("images/jpg/night_clear.jpg")
        if weatherIcon in ptCloud:            
            return Image.open("images/jpg/night_partial_cloud.jpg")
        if weatherIcon in lightRain:
            return Image.open("images/jpg/night_rain.jpg")
        if weatherIcon in snow:
            return Image.open("images/jpg/night_snow.jpg")
        else:
            logging.info("No icon set for " + str(weatherID))
            return Image.open("images/jpg/night_clear.jpg")


