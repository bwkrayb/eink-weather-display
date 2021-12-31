import logging
import datetime
import subprocess
import os

from libs.weatherLib import Weather, get_weather, update_weather
from screens import AbstractScreen
from datetime import datetime

class Screen(AbstractScreen):
    weather: Weather = get_weather()

    def handle_btn_press(self, button_number: int = 1):
        if button_number == 0:
            pass
        elif button_number == 1:
            self.reload()
            self.show()
        elif button_number == 2:
            update_weather()
            self.reload()
            self.show()
        elif button_number == 3:
            pass
        else:
            logging.error("Unknown button pressed: KEY{}".format(button_number + 1))

    def reload(self):
        dt = datetime.now()

        self.blank()

        self.draw_titlebar("Weather")

        logo = self.weather.get_icon()
        self.image.paste(logo, (20, 40))

        text = os.popen('curl wttr.in/?format="%t"').read()
        self.centered_text(text.strip('+F'), 20, 60)

        text = dt.strftime('%a %m/%d %I:%M %p')
        self.centered_text(text, 85, 20)

        text = os.popen('curl -s wttr.in/?format="%C"').read()
        self.centered_text(text.title(), 110, 30)

        text = 'St Charles, IL'
        self.centered_text(text, 145, 20)
