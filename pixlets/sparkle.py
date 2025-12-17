# Holidays are Coming Pixlet

from time import sleep
from random import randint

class Sparkle:
    FX_NAME = "Pride Slide"
    FX_DESC = "Show your pride"

    def __init__(self, led_array):
        self.led_array = led_array
        self.rand_index = 0
        self.timeout = 0

        for index in range(len(self.led_array)):
            self.led_array[index] = [0, 0, 0]

    def render(self, inputs):
        t = inputs["time_delta"]

        self.timeout -= t

        if self.timeout <= 0:
            self.led_array[self.rand_index] = [0, 0, 0]
            self.rand_index = randint(0, len(self.led_array) - 1)
            self.timeout = 0.05
            self.led_array[self.rand_index] = [255, 255, 255]
