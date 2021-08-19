# Holidays are Coming Pixlet

from time import sleep

light_cycle_colours = [
    [255,   0,   0],    # Red
    [  0, 255,   0],    # Green
    [  0,   0, 255],    # Blue
    [255, 255,   0]     # Yellow
]

class HolidaysComing:
    FX_NAME = "Holidays are Coming"
    FX_DESC = "Inspired by a vintage fizzy drink commercial"

    def __init__(self, led_array):
        self.led_array = led_array

    def render(self, inputs):
        t = inputs["time"]
        
        for i in range(len(self.led_array)):
            self.led_array[i] = light_cycle_colours[(int(t) + i) % len(light_cycle_colours)]
