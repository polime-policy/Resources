import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, compound_score

# Function to perform sentiment analysis for different sections
def analyze_sentiment_sections(sections):
    sentiment_scores = {}

    for section_name, section_text in sections.items():
        sentiment, compound_score = analyze_sentiment(section_text)

        sentiment_scores[section_name] = {
            'sentiment': sentiment,
            'compound_score': compound_score
        }

    return sentiment_scores

# Example usage
sections = {
    'Introduction': 'This policy aims to improve access to healthcare services for underserved communities.',
    'Analysis': 'The data shows a significant increase in crime rates following the implementation of the current policy.',
    'Recommendations': 'To address the issue, we propose allocating additional funding to community policing programs.',
    'Conclusion': 'In conclusion, the proposed policy changes have the potential to bring about positive outcomes.'
}

sentiment_scores = analyze_sentiment_sections(sections)

# Print sentiment scores for each section
for section_name, scores in sentiment_scores.items():
    print(f"Section: {section_name}")
    print(f"Sentiment: {scores['sentiment']}")
    print(f"Compound Score: {scores['compound_score']}")
    print()
