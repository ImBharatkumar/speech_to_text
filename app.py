import requests
import os
from src.preprocess import record
import sounddevice as sd
from scipy.io.wavfile import write
from src.preprocess.record import record
from dotenv import load_dotenv
import streamlit as st


# Initialize the SpeechToText class
st.title('Speech To Text "openai/whisper-base" model')
st.write("Press the 'Record' button to start recording audio. Press 'Transcribe' to transcribe the audio to text.")



load_dotenv()
access_key = os.getenv('ACCESS_KEY')
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": access_key}


class  SpeechToText:
    def __init__(self,filename):
        self.filename= filename
        
    def query(self):
        with open(self.filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

audio_file= r'D:\\Projects\\sst\\src\\audio_files\\output.mp3'

# Create the recording button
if st.button('Record'):
    st.write("Recording...")
    with st.spinner("Recording..."):
        try:
            r = record(5)
            r.recording()
            st.write("Recording complete.")
        except Exception as e:
            print(e)


# Create the transcription button
if st.button('Transcribe'):
    st.write("Transcribing...")
    with st.spinner("Transcribing..."):
        try:
            rs = SpeechToText(audio_file)
            output = rs.query()
            st.write(output["text"])
        except Exception as e:
            print(e)



         
        