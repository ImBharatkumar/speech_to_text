import sounddevice as sd
import os , sys
from scipy.io.wavfile import write


class record:
    def __init__(self,sec):
        self.sec = sec
        
    def recording(self):
        #Record audio and save to a file.
        fs = 44100  # Sample rate
        seconds = self.sec  # Duration of recording
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        print("Done!")
        path = r'D:\\Projects\\sst\\src\\audio_files\\output.mp3'
        return write(path, fs, myrecording)  

if __name__ == '__main__':
    try:
        print("Recording...")
        r = record(10)
        r.recording()

    except Exception as e:
        print(e)