import numpy as np
import pyaudio
from time import time, sleep
from ledstrip import LedStrip
from pixlet_manager import PixletManager

from aubio import tempo, onset, source


if __name__ == "__main__":
    print("Ellie D - The girl with rainbows in her hair")

    led_strip = LedStrip()
    led_array = np.empty([150, 3], dtype=np.uint8)

    start_time = time()
    last_time = start_time

    inputs = {
        "time": 0,
        "time_delta": 0,
        "frames": 0,
        "is_beat": False,
        "is_onset": False
    }

    pixlet_manager = PixletManager("pixlets/audio")

    fx_class = pixlet_manager.next_pixlet()
    fx = fx_class(led_array)

    fx_timeout = 5

    win_s = 512                 # fft size
    hop_s = win_s // 2          # hop size

    # win_s = 1024                # fft size
    # hop_s = win_s // 2          # hop size

    s = source("perspective.wav", 0, hop_s)
    samplerate = s.samplerate
    tempo_detect = tempo("default", win_s, hop_s, samplerate)
    onset_detect = onset("default", win_s, hop_s, samplerate)

    py_audio = pyaudio.PyAudio()
    # audio_out = Stream(samplerate = samplerate, blocksize = hop_s)

    pyaudio_format = pyaudio.paFloat32
    frames_per_buffer = hop_s
    n_channels = 1

    audio_out = py_audio.open(format=pyaudio_format,
                channels=1,
                rate=s.samplerate,
                frames_per_buffer=frames_per_buffer,
                output=True)

    # start pyaudio stream
    audio_out.start_stream()


    # print(py_audio.get_format_from_width(2))
    # audio_out.start()

    # tempo detection delay, in samples
    # default to 4 blocks delay to catch up with
    delay = 4. * hop_s

    # list of beats, in samples
    # beats = []

    # total number of frames read
    total_frames = 0

    print ('Press Ctrl-C to quit.')

    try:
        while True:
            samples, read = s()
            is_beat = tempo_detect(samples)
            is_onset = onset_detect(samples)

            if is_beat:
                this_beat = int(total_frames - delay + is_beat[0] * hop_s)
                print("Beat {} - {}".format((this_beat / float(samplerate)), is_beat[0]))
                # beats.append(this_beat)

            # if is_onset:
            #     print("IS ONSET")
            # else:
            #     print("NOT ONSET")

            total_frames += read
            if read < hop_s: break

            tick = time()

            inputs["time"] = tick - start_time
            inputs["time_delta"] = tick - last_time
            inputs["frames"] += 1
            inputs["is_beat"] = is_beat[0] > 0.5
            inputs["is_onset"] = is_onset[0] > 0

            fx.render(inputs)
            led_strip.display(led_array)

            last_time = tick

            fx_timeout -= inputs["time_delta"]

            if fx_timeout < 0:
                fx_timeout += 5
                fx_class = pixlet_manager.next_pixlet()
    
                fx = fx_class(led_array)

            audio_out.write(samples.tobytes())

    except KeyboardInterrupt:
        audio_out.stop_stream()
        audio_out.close()

        py_audio.terminate()