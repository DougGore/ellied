# Holidays are Coming Pixlet

from time import sleep

light_cycle_colours = [
    [255,   0,   0],    # Red
    [  0, 255,   0],    # Green
    [  0,   0, 255],    # Blue
    [255, 255,   0]     # Yellow
]

class AudioTest:
    FX_NAME = "Holidays are Coming"
    FX_DESC = "Inspired by a vintage fizzy drink commercial"

    def __init__(self, led_array):
        self.led_array = led_array
        self.beat_level = 0
        self.onset_level = 0
        self.decay = 1
        self.beat_main = True

    def render(self, inputs):
        t = inputs["time"]
        is_beat = inputs["is_beat"]
        is_onset = inputs["is_onset"]
        led_count = len(self.led_array)

        led_on = self.beat_main

        for i in range(led_count):
            if led_on:
                self.led_array[i] = [128, 0, 128]
            else:
                self.led_array[i] = [0, 0, 0]
            
            led_on = not led_on

        if is_beat == True:
            self.beat_main = not self.beat_main

            # self.beat_level = 255
        
        # if is_onset == True:
        #     self.onset_level = 255

        # print(self.beat_level, self.onset_level, is_onset)

        # for i in range(led_count // 2):
        #     self.led_array[i] = [self.beat_level, self.beat_level, self.beat_level]

        # for i in range(led_count // 2, led_count):
        #     self.led_array[i] = [self.onset_level, self.onset_level, self.onset_level]

        # if self.beat_level > 0:
        #     self.beat_level -= 4
        #     # self.beat_level = 0

        # if self.onset_level > 0:
        #     self.onset_level -= 4
        #     # self.onset_level = 0
