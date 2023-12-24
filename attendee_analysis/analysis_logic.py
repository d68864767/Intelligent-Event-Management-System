```python
# Import necessary libraries
from .vision_api import analyze_image, get_demographics
from .speech_to_text_api import transcribe_speech, get_speech_content

def analyze_attendee(image_path, speech_file_path):
    """
    Function to analyze attendee based on image and speech data
    :param image_path: Path to the image file
    :param speech_file_path: Path to the audio file
    :return: Analysis result
    """
    # Analyze image and extract demographic information
    analyzed_image_data = analyze_image(image_path)
    demographics = get_demographics(analyzed_image_data)

    # Transcribe speech and extract content
    transcribed_speech_data = transcribe_speech(speech_file_path)
    speech_content = get_speech_content(transcribed_speech_data)

    # Combine results
    analysis_result = {
        'demographics': demographics,
        'speech_content': speech_content
    }

    return analysis_result
```
