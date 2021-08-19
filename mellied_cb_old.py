import numpy as np
import pyaudio
from time import time, sleep
from ledstrip import LedStrip
from pixlet_manager import PixletManager

from aubio import tempo, source

# win_s = 512                 # fft size
# hop_s = win_s // 2          # hop size

win_s = 1024                # fft size
hop_s = win_s // 2          # hop size


def pyaudio_callback(_in_data, _frame_count, _time_info, _status):
    print("Callback")
    samples, read = s()
#     is_beat = o(samples)
#     if is_beat:
#         this_beat = int(total_frames - delay + is_beat[0] * hop_s)
#         print("%f" % (this_beat / float(samplerate)))
#         # beats.append(this_beat)
#     total_frames += read
#     # if read < hop_s: break

# # read = 0
# # while 1:
# #     vec, read = f()
# #     s.write(vec)
# #     if read < hop_size: break
#     audio_out.write(samples)

#     fx.render(inputs)

#     tick = time()

#     inputs["time"] = tick - start_time
#     inputs["time_delta"] = tick - last_time
#     inputs["frames"] += 1
#     inputs["is_beat"] = is_beat

#     last_time = tick

#     led_strip.display(led_array)
#     # sleep(50 / 1000.0)

#     fx_timeout -= inputs["time_delta"]

#     if fx_timeout < 0:
#         fx_timeout += 5
#         fx_class = pixlet_manager.next_pixlet()

#         fx = fx_class(led_array)

    audiobuf = samples.tobytes()
    if read < hop_s:
        print("Complete")
        return (audiobuf, pyaudio.paComplete)
    return (audiobuf, pyaudio.paContinue)

if __name__ == "__main__":
    print("Ellie D - The girl with rainbows in her hair")

    led_strip = LedStrip()
    led_array = np.empty([150, 3], dtype=np.uint8)

    start_time = time()
    last_time = start_time

    inputs = {
        "time": 0,
        "time_delta": 0,
        "frames": 0
    }

    pixlet_manager = PixletManager("pixlets/audio")

    fx_class = pixlet_manager.next_pixlet()
    fx = fx_class(led_array)

    fx_timeout = 5

    s = source("perspective.wav", 0, hop_s)
    samplerate = s.samplerate
    o = tempo("default", win_s, hop_s, samplerate)

    py_audio = pyaudio.PyAudio()
    # audio_out = Stream(samplerate = samplerate, blocksize = hop_s)

    pyaudio_format = pyaudio.paFloat32
    frames_per_buffer = hop_s
    n_channels = 1

    audio_out = py_audio.open(format=pyaudio_format,
                channels=2,
                rate=s.samplerate,
                frames_per_buffer=frames_per_buffer,
                output=True,
                stream_callback=pyaudio_callback)

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

    # start pyaudio stream
    audio_out.start_stream()

    # try:
    # wait for stream to finish
    while audio_out.is_active():
        sleep(0.1)

    # except KeyboardInterrupt:
    audio_out.stop_stream()
    audio_out.close()

    py_audio.terminate()