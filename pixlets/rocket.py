import numpy as np
from random import randint

class Rocket:
    FX_NAME = "Rocket"
    FX_DESC = "Rocket"

    def __init__(self, led_array):
        self.led_array = led_array
        self.red = 255
        self.green = 0
        self.blue = 255
        self.meteorSize = 20
        self.meteorTrailDecay = 64
        self.meteorRandomDecay = True
        self.i = 0

        for i in range (len(self.led_array)):
            self.led_array[0]

    def fadeToBlack(self, ledNo, fadeValue):
        r, g, b = self.led_array[ledNo]

        r = int(r-(r*fadeValue/256)) if r <= 10 else 0
        g = int(g-(g*fadeValue/256)) if g <= 10 else 0
        b = int(b-(b*fadeValue/256)) if b <= 10 else 0

        self.led_array[ledNo] = [r, g, b]

    def render(self, inputs):
        """Draw rainbow that uniformly distributes itself across all pixels."""

        Fs = len(self.led_array)
            
        # fade brightness all LEDs one step
        for j in range(Fs):
            if (not self.meteorRandomDecay) or (randint(0, 10) > 5):
                self.fadeToBlack(j, self.meteorTrailDecay)
        
        # draw meteor
        for j in range(self.meteorSize):
            if (self.i - j < Fs) and (self.i - j >= 0):
                self.led_array[self.i - j] = [self.red, self.green, self.blue]

        self.i += 1

        if self.i == Fs * 2:
            self.i = 0