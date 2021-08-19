try:
    from rpi_ws281x import *
    REAL_HARDWARE = True
except:
    from vrtneopixel import *
    REAL_HARDWARE = False

# LED strip configuration:
# LED_COUNT      = 50      # Number of LED pixels.
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 64     # Set to 0 for darkest and 255 for brightest
# LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class LedStrip:
    def __init__(self):
        if REAL_HARDWARE:
            self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, ws.WS2811_STRIP_GRB)
        else:
            self.strip = Adafruit_NeoPixel([1, LED_COUNT], LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, led_size=7)
        
        self.strip.begin()

    def display(self, led_array):
        # print(led_array)
        for i in range(0, self.strip.numPixels()):
            led = led_array[i]
            self.strip.setPixelColorRGB(i, int(led[0]), int(led[1]), int(led[2]))

        self.strip.show()
