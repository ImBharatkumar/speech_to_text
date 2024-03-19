<img width="960" alt="Screenshot 2024-03-19 154653" src="https://github.com/ImBharatkumar/speech_to_text/assets/118038590/54dd22c8-a2e7-4618-a9ae-ad65f6c91c1d">



# Speech-to-Text (SST)
This project is a simple speech-to-text application that transcribes audio files using the Whisper model from Hugging Face. The application consists of a single Python script that records audio, sends it to the Whisper model for transcription, and prints the transcription results.

## Requirements
* Python 3.6 or higher
* whisper-base model from Hugging Face
* requests library for making HTTP requests
* sounddevice library for recording audio
* scipy library for writing audio files
 
 ## Installation
 Clone the repository to your local machine:

* git clone https://github.com/your-username/speech-to-text.git
* Create a .env file in the root directory of the project and add your Hugging Face access key:
* ACCESS_KEY=your-hugging-face-access-key
* Install the required libraries using pip:


* pip install -r requirements.txt
## Usage
* Run the app.py script from the command line:
  
* python app.py
* The script will start recording audio for 30 seconds. Speak clearly into the microphone during this time.
* After recording, the script will send the audio to the Whisper model for transcription and print the results to the console.

## Code Structure
* app.py: The main script that records audio, sends it to the Whisper model for transcription, and prints the results.
* src: A directory containing the preprocess module.
* src/preprocess.py: A module containing the record function, which records audio and saves it to a file.
* .env: A file containing the Hugging Face access key.
* requirements.txt: A file containing the required libraries and their versions.
