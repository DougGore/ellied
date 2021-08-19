from time import sleep
from random import randint
import numpy as np

class TwinkleFairy:
    FX_NAME = "Twinkle Fairy"
    FX_DESC = "RGB twinkling effect with a fairy sweeping by periodically to change effect colour"

    def __init__(self, led_array):
        self.led_array = led_array
        self.fx_time = 10
        self.whoosh = False
        
        self.colour_mix = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255)
        ]
        self.colour_index = 0

    def drawSparkle(self, t, pixel_range, r, g, b):
        Fs = len(self.led_array)
        f = 64

        for i in pixel_range:
            y = (np.sin(((2 * np.pi * f * i) + t * 500) / Fs) * 0.5) + 0.5
            self.led_array[i] = [
                int(r * y),
                int(g * y),
                int(b * y)
            ]


    def render(self, inputs):
        t = inputs["time"]

        self.colour_index = int(t // self.fx_time) % len(self.colour_mix)
        r, g, b = self.colour_mix[self.colour_index]

        if int(t) % self.fx_time == 0:
            colour_alt = (int(t // self.fx_time) - 1) % len(self.colour_mix)
            r, g, b = self.colour_mix[colour_alt]
            ra, ga, ba = self.colour_mix[self.colour_index]
        #     # =B1-((B1-A1)*(1-C1))
            frac = t % 1
            # print("R: {} G: {} B: {}".format(r, g, b))
            # print("Ra: {} Ga: {} Ba: {}".format(ra, ga, ba))
            rn = int(ra - ((ra - r) * (1 - frac)))
            gn = int(ga - ((ga - g) * (1 - frac)))
            bn = int(ba - ((ba - b) * (1 - frac)))

            mid = int(frac * len(self.led_array))

            self.drawSparkle(t, range(mid), rn, gn, bn)
            self.drawSparkle(t, range(mid, len(self.led_array)), r, g, b)

            # self.strip.setPixelColor(mid, Color(255, 255, 0))
            self.led_array[mid] = [255, 255, 0]

            # self.strip.show()
            # sleep(1 / 1000.0)

        else:
            self.drawSparkle(t, range(len(self.led_array)), r, g, b)
            # self.strip.show()
            # sleep(self.wait_ms / 1000.0)
