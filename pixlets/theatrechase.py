from time import sleep
from math import sin

class TheatreChase:
    FX_NAME = "Theatre chase"
    FX_DESC = "Movie theatre light style chaser animation"

    def __init__(self, led_array):
        self.led_array = led_array
        self.position = 0
        self.iteration = 0

    def render(self, _):
        for i in range(0, len(self.led_array), 3):
            self.led_array[i + self.iteration] = [self.red, self.green, self.blue]
        
        # self.strip.show()
        
        # sleep(self.wait_ms/1000.0)
        
        # for i in range(0, self.strip.numPixels(), 3):
        #     self.strip.setPixelColor(i + self.iteration, 0)

        # self.iteration += 1

        # if self.iteration == 3:
        #     self.iteration = 0
