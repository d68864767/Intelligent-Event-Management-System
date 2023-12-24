```python
# Import necessary libraries
from google.cloud import speech_v1p1beta1 as speech
from google.protobuf.json_format import MessageToDict

def transcribe_speech(speech_file_path):
    """
    Function to transcribe speech using Google Cloud Speech-to-Text API
    :param speech_file_path: Path to the audio file
    :return: Transcribed text data in dictionary format
    """
    # Initialize a client for Speech-to-Text API
    client = speech.SpeechClient()

    # Load audio from path
    with open(speech_file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    # Configure the recognition process
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Perform speech-to-text on the audio file
    response = client.recognize(config=config, audio=audio)

    # Convert the response to dictionary format
    transcribed_data = MessageToDict(response)

    return transcribed_data

def get_speech_content(transcribed_data):
    """
    Function to extract speech content from transcribed data
    :param transcribed_data: Transcribed text data in dictionary format
    :return: Speech content
    """
    speech_content = ""

    # Extract speech content
    for result in transcribed_data['results']:
        speech_content += result['alternatives'][0]['transcript']

    return speech_content
```
