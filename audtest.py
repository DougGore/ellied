import pyaudio

print("Init PyAudio...")
po = pyaudio.PyAudio()

print("Iterating...")
for index in range(po.get_device_count()): 
    desc = po.get_device_info_by_index(index)
    print(desc)
    print ("DEVICE: {0} \t INDEX: {1} \t RATE: {2}".format(desc["name"],index,int(desc["defaultSampleRate"])))