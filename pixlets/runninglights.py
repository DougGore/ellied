from time import sleep
from math import sin

class RunningLights:
    FX_NAME = "Running lights"
    FX_DESC = ""

    def __init__(self, led_array):
        self.led_array = led_array
        self.red = 255
        self.green = 255
        self.blue = 255

    def render(self, inputs):
        t = inputs["time"] * 16
        Fs = len(self.led_array)

        for i in range(Fs):
            level = (sin(i + t) * 127 + 128) / 255
            self.led_array[i] = [int(level * self.red),
                                 int(level * self.green),
                                 int(level * self.blue)]
