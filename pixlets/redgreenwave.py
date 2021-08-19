import numpy as np

class RedGreenWave:
    FX_NAME = "Red and green wave"
    FX_DESC = "Red and green wave pattern travelling in alternate directions"

    def __init__(self, led_array):
        self.led_array = led_array

    def render(self, inputs):
        """Wipe color across display a pixel at a time."""

        t = inputs["time"]
        Fs = len(self.led_array)
        f = 16

        for i in range(Fs):
            y = int(np.sin(((2 * np.pi * f * i) + t * 1000) / Fs) * 255)
            if y < 0: y = 0

            y2 = int((np.cos(((2 * np.pi * f * (Fs - i)) + t * 1000) / Fs)) * 255)
            if y2 < 0: y2 = 0
            
            self.led_array[i] = [y, y2, 0]

