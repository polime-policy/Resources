from nltk.tokenize import word_tokenize
from nltk.corpus import opinion_lexicon

# Function to perform emotion analysis
def analyze_emotion(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Initialize emotion scores
    emotion_scores = {
        'anger': 0,
        'anticipation': 0,
        'disgust': 0,
        'fear': 0,
        'joy': 0,
        'sadness': 0,
        'surprise': 0,
        'trust': 0
    }

    # Iterate through the tokens and calculate emotion scores
    for word in tokens:
        word = word.lower()

        if word in opinion_lexicon.positive():
            emotion_scores['joy'] += 1
            emotion_scores['trust'] += 1
            emotion_scores['anticipation'] += 1
        elif word in opinion_lexicon.negative():
            emotion_scores['anger'] += 1
            emotion_scores['disgust'] += 1
            emotion_scores['fear'] += 1
            emotion_scores['sadness'] += 1

    return emotion_scores

# Example usage
text = "As quantum technologies rise to the forefront of computing, the United States must proactively safeguard our citizens’ sensitive data and digital systems from the next generation of 'quantum cyber-attacks.' As stated by a 2021 McKinsey report, experts forecast quantum computers will be advanced enough to crack existing cryptography protocols by 2030, placing individuals, organizations, and national security at serious risk. Thus, if the quantum computing industry is left to grow unregulated, we are all threatened by widespread data breaches, intellectual property theft, financial losses, and even physical harm."

emotion_scores = analyze_emotion(text)
print("Emotion Scores:", emotion_scores)


