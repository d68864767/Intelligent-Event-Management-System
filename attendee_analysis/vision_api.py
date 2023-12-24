```python
# Import necessary libraries
from google.cloud import vision
from google.protobuf.json_format import MessageToDict

def analyze_image(image_path):
    """
    Function to analyze image using Google Cloud Vision API
    :param image_path: Path to the image file
    :return: Analyzed image data in dictionary format
    """
    # Initialize a client for Vision API
    client = vision.ImageAnnotatorClient()

    # Load image from path
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform face detection on the image file
    response = client.face_detection(image=image)

    # Convert the response to dictionary format
    analyzed_data = MessageToDict(response)

    return analyzed_data

def get_demographics(analyzed_data):
    """
    Function to extract demographic information from analyzed image data
    :param analyzed_data: Analyzed image data in dictionary format
    :return: Demographic information
    """
    demographics = {}

    # Extract demographic information
    for face_annotation in analyzed_data['faceAnnotations']:
        demographics['joy'] = face_annotation['joyLikelihood']
        demographics['sorrow'] = face_annotation['sorrowLikelihood']
        demographics['anger'] = face_annotation['angerLikelihood']
        demographics['surprise'] = face_annotation['surpriseLikelihood']

    return demographics
```
