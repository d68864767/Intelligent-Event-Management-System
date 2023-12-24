```python
# Import the necessary libraries
from collections import defaultdict
from .natural_language_api import analyze_feedback

def process_feedback(feedbacks):
    """
    Process a list of feedbacks and return the analysis results

    Args:
    feedbacks: A list of feedback texts to analyze
    """
    # Initialize a dictionary to store the analysis results
    analysis_results = defaultdict(list)

    # Iterate over the feedbacks
    for feedback in feedbacks:
        # Analyze the feedback
        response = analyze_feedback(feedback)

        # Store the document sentiment score and magnitude
        analysis_results['document_sentiment_score'].append(response.document_sentiment.score)
        analysis_results['document_sentiment_magnitude'].append(response.document_sentiment.magnitude)

        # Store the sentence sentiment scores and magnitudes
        sentence_sentiment_scores = []
        sentence_sentiment_magnitudes = []
        for sentence in response.sentences:
            sentence_sentiment_scores.append(sentence.sentiment.score)
            sentence_sentiment_magnitudes.append(sentence.sentiment.magnitude)
        analysis_results['sentence_sentiment_scores'].append(sentence_sentiment_scores)
        analysis_results['sentence_sentiment_magnitudes'].append(sentence_sentiment_magnitudes)

        # Store the language of the text
        analysis_results['language'].append(response.language)

    return analysis_results
```
