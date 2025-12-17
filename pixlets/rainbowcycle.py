import numpy as np

class RedGreenWave:
    FX_NAME = "Rainbow cycle"
    FX_DESC = "Rainbow cycle"

    def __init__(self, led_array):
        self.led_array = led_array

    @staticmethod
    def wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return [pos * 3, 255 - pos * 3, 0]
        elif pos < 170:
            pos -= 85
            return [255 - pos * 3, 0, pos * 3]
        else:
            pos -= 170
            return [0, pos * 3, 255 - pos * 3]

    def render(self, inputs):
        """Draw rainbow that uniformly distributes itself across all pixels."""

        t = inputs["time"]
        Fs = len(self.led_array)
        offset = t * 16 % 256
            
        for i in range(Fs):
            self.led_array[i] = self.wheel(int((i * 256 / Fs) + offset) & 255)
