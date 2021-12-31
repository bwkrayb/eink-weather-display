import importlib
import logging
import threading

from PIL import Image
from gpiozero import Button

from settings import DRIVER

try:
    driver = importlib.import_module("waveshare_epd." + DRIVER)
except ImportError:
    logging.error("Driver '{0}' couldn't be loaded".format(DRIVER))
    raise ImportError("Couldn't load driver")


class EPD(threading.Thread):
    epd: driver.EPD = driver.EPD()
    dirty: bool = False
    image: Image = Image.new("1", (driver.EPD_HEIGHT, driver.EPD_WIDTH), 255)
    thread_lock = threading.Lock()

    def __init__(self):
        super().__init__()
        self.image = Image.new("1", self.get_size(), 255)
        self.epd.init()  # initialize the display
        self.buttons = [Button(5), Button(6), Button(13), Button(19)]
        self.name = "EPD"

    def __del__(self):
        self.image = Image.new("1", get_size(), 255)
        red_image = Image.new("1", get_size(), 255)
        self.epd.display(self.epd.getbuffer(self.image), self.epd.getbuffer(red_image))

    def run(self):
        self.epd.Clear()
        thread_process = threading.Thread(target=self.process_epd)
        # run thread as a daemon so it gets cleaned up on exit.
        thread_process.daemon = True
        thread_process.start()

    def process_epd(self):
        while True:
            if self.dirty and self.image:
                self.dirty = False
                logging.debug("Writing image to display")
                red_image = Image.new("1", get_size(), 255)
                self.epd.display(self.epd.getbuffer(self.image), self.epd.getbuffer(red_image))

    def show(self, image: Image):
        logging.debug("Image sent to EPD")
        self.image = image
        self.dirty = True

    def get_size(self):
        return driver.EPD_HEIGHT, driver.EPD_WIDTH


epd = EPD()


def get_epd():
    return epd


def get_size():
    return driver.EPD_HEIGHT, driver.EPD_WIDTH


def get_buttons():
    return epd.buttons
