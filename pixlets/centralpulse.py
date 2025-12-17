import numpy as np

class CentralPulse:
    FX_NAME = "Central pulse"
    FX_DESC = "To be written"

    def __init__(self, led_array):
        self.led_array = led_array

    def render(self, inputs):
        """Wipe color across display a pixel at a time."""

        t = inputs["time"]
        mid_point = len(self.led_array) // 2
        end_point = len(self.led_array) - 1
        f = 2

        for i in range(mid_point):
            # y = int(np.sin(2 * np.pi * f * i))
            y = int(np.sin(((2 * np.pi * f * i) + t * 200) / mid_point) * 255)
            # if y < 0: y = 0

            # y2 = int((np.cos(((2 * np.pi * f * (Fs - i)) + t * 1000) / Fs)) * 255)
            # if y2 < 0: y2 = 0
            
            self.led_array[i] = [y, y, 0]
            self.led_array[end_point - i] = [y, y, 0]

