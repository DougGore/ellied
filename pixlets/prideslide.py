# Pride Slide

from time import sleep

light_cycle_colours = [
    [255,   0,  24],    # Vivid Red
    [246, 138,  30],    # Deep Saffron
    [255, 255,  65],    # Maximum Yellow
    [  0, 128,  24],    # Ao
    [  0,   0, 249],    # Blue
    [134,   0, 125],    # Philippine Violet
    [  0,   0,   0],    # Gap
    [  0,   0,   0],    # Gap
    [  0,   0,   0]     # Gap
]

class PrideSlide:
    FX_NAME = "Pride Slide"
    FX_DESC = "Show your pride"

    def __init__(self, led_array):
        self.led_array = led_array

    def render(self, inputs):
        t = inputs["time"]
        
        for i in range(len(self.led_array)):
            self.led_array[i] = light_cycle_colours[(int(t / 0.1) + i) % len(light_cycle_colours)]
