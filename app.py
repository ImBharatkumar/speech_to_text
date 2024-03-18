import requests
from src.preprocess import record
import sounddevice as sd
from scipy.io.wavfile import write
from src.preprocess.record import record


API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": "Bearer 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"}

class  SpeechToText:
    def __init__(self,filename):
        self.filename= filename
        
    def query(self):
        with open(self.filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()


if __name__  == '__main__':
    try:
        print("Recording...")
        r = record(10)
        r.recording()
        print('loading ...')
        print('Transcribing..')
        path= r'D:\\Projects\\sst\\src\\audio_files\\output.mp3'
        rs = SpeechToText(path)
        output = rs.query()
        print(output)
    except Exception as e:
        print(e)
