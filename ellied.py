#!/usr/bin/env python3

import importlib
import pkgutil
import inspect
import numpy as np
import argparse
from time import time, sleep
from ledstrip import LedStrip
from pixlet_manager import PixletManager

def get_pixlet(reference):
    pixlet_module = importlib.import_module(reference)

    pixlet_classlist = inspect.getmembers(pixlet_module, inspect.isclass)

    # Get first class
    return pixlet_classlist[0][1]

if __name__ == "__main__":
    multi_fx = True

    print("Ellie D - The girl with rainbows in her hair")

    parser = argparse.ArgumentParser()
    parser.add_argument("--fx")
    parser.add_argument("--time", type=int, default=5)
    args = parser.parse_args()

    led_strip = LedStrip()
    led_array = np.empty([150, 3], dtype=np.uint8)

    start_time = time()
    last_time = start_time

    inputs = {
        "time": 0,
        "time_delta": 0,
        "frames": 0
    }

    pixlet_manager = PixletManager("pixlets")

    if args.fx:
        multi_fx = False
        fx_class = pixlet_manager.get_pixlet(args.fx)
    else:
        fx_class = pixlet_manager.next_pixlet()
    
    if fx_class is None:
        print("Effect not found!")
        fx = None
    else:
        fx = fx_class(led_array)
        
    fx_timeout = args.time

    if fx:
        try:
            print(fx.FX_NAME)
            while True:
                fx.render(inputs)

                tick = time()

                inputs["time"] = tick - start_time
                inputs["time_delta"] = tick - last_time
                inputs["frames"] += 1

                last_time = tick

                led_strip.display(led_array)
                # sleep(50 / 1000.0)

                if multi_fx:
                    fx_timeout -= inputs["time_delta"]

                    if fx_timeout < 0:
                        fx_timeout += args.time
            
                        fx_class = pixlet_manager.next_pixlet()
                        fx = fx_class(led_array)
                        print(fx.FX_NAME)
        except KeyboardInterrupt:
            for i in range(len(led_array)):
                led_array[i] = [0, 0, 0]

            led_strip.display(led_array)

