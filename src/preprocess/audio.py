from pydub import AudioSegment

AudioSegment.converter = "rC:\\Program Files\\ffmpeg-2024-03-14-git-2129d66a66-essentials_build\\bin\\ffmpeg"

# Load the M4A file
m4a_audio = AudioSegment.from_file(r"D:\\Projects\\speech_to_text\\src\\data\\Recording.m4a", format="m4a")

# Export the M4A file as FLAC
m4a_audio.export("output.flac", format="flac")
