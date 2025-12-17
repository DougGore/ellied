from time import sleep
from random import randint, sample, random, choice

class Twinkle:
    FX_NAME = "Twinkle"
    FX_DESC = "Random flashes of white light"

    def __init__(self, led_array):
        self.led_array = led_array

        for index in range(len(self.led_array)):
            self.led_array[index] = [0, 0, 0]

        indices = sample(range(0, len(self.led_array)), 20)
        values = sample(range(127, 255), 20)

        self.twinkles = list(map(list, zip(indices, values)))

    def render(self, inputs):
        t = inputs["time_delta"] * 128

        for index, twinkle in enumerate(self.twinkles):
            led, value = twinkle

            self.led_array[led] = [value, value, value]

            if value <= 0:
                indices = [i[0] for i in self.twinkles]
                not_in_S = choice([x for x in range(len(self.led_array)) if x not in indices])
                self.twinkles[index] = [not_in_S, 255]
            else:
                twinkle[1] -= t
