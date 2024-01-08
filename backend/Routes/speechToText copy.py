import assemblyai as aai
import os
import random
import string


os.chdir('../..')

aai.settings.api_key = "66a8c7176b2c4dbc8e1ec4fd7931df63"

# Specify the path to your local audio file using Unix-like path separators
FILE_PATH = "backend/Routes/audio.mp3"

if os.path.exists(FILE_PATH):
    print("File exists!")
else:
    print("File does not exist.")

config = aai.TranscriptionConfig(
 speaker_labels=True,
)

transcript = aai.Transcriber().transcribe(FILE_PATH, config)

# Open a file in write mode ('w') and write the summary
random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=13))

with open(f"backend/Routes/audios/{random_name}.txt", 'w') as file:
    for utterance in transcript.utterances:
        # Write the formatted string to the file
        file.write(f"Speaker {utterance.speaker}: {utterance.text}\n")