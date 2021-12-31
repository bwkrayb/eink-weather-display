import threading
import time
import logging
import settings
import datetime
import os
from PIL import Image
from datetime import datetime



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
        elif 'fog' in weatherIcon:
            return Image.open("images/jpg/fog.jpg")
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

