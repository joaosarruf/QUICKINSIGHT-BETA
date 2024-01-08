import assemblyai as aai
import os
import requests
import json
import time


os.chdir('../..')

aai.settings.api_key = "66a8c7176b2c4dbc8e1ec4fd7931df63"

FILE_PATH = "backend/Routes/audio.mp3"

if os.path.exists(FILE_PATH):
    print("File exists!")
else:
    print("File does not exist.")

base_url = "https://api.assemblyai.com/v2"

headers = {
    "authorization": "66a8c7176b2c4dbc8e1ec4fd7931df63" 
}

with open(FILE_PATH , "rb") as f:
 response = requests.post(base_url + "/upload",
                          headers=headers,
                          data=f)

upload_url = response.json()["upload_url"]

data = {
    "audio_url": upload_url 
}

url = base_url + "/transcript"
response = requests.post(url, json=data, headers=headers)

transcript_id = response.json()['id']
polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"

while True:
 transcription_result = requests.get(polling_endpoint, headers=headers).json()

 if transcription_result['status'] == 'completed':
    break

 elif transcription_result['status'] == 'error':
    raise RuntimeError(f"Transcription failed: {transcription_result['error']}")

 else:
    time.sleep(3)

transcript = aai.Transcriber().transcribe(FILE_PATH)

random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=13))
output_file_name = f"{random_name}.mp3"

# Write the formatted strings to the file
with open(output_file_name, 'w') as file:
    for utterance in transcript.utterances:
        file.write(f"Speaker {utterance.speaker}: {utterance.text}\n")