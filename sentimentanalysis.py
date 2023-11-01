import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

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

current_memo = '''
This policy aims to improve access to healthcare services for underserved communities. It focuses on expanding healthcare facilities, recruiting more healthcare professionals, and providing affordable healthcare options for low-income individuals. The policy aims to address the existing healthcare disparities and ensure that everyone has equal access to quality healthcare services.
'''

comparative_memos = [
    '''
    This policy proposes tax incentives for private companies to invest in renewable energy sources such as solar and wind power. It aims to reduce carbon emissions and promote a sustainable environment.
    ''',
    '''
    The proposed policy focuses on improving education quality by implementing new teaching methods and providing additional resources for schools. It aims to enhance students' learning outcomes and prepare them for future success.
    '''
]

sentiment_scores = {}

sentiment, compound_score = analyze_sentiment(current_memo)
sentiment_scores['Current Memo'] = {
    'sentiment': sentiment,
    'compound_score': compound_score
}

for i, memo in enumerate(comparative_memos):
    sentiment, compound_score = analyze_sentiment(memo)
    sentiment_scores[f'Comparative Memo {i+1}'] = {
        'sentiment': sentiment,
        'compound_score': compound_score
}

print("Sentiment Analysis:")
for memo, scores in sentiment_scores.items():
    print(f"Memo: {memo}")
    print(f"Sentiment: {scores['sentiment']}")
    print(f"Compound Score: {scores['compound_score']}")
    print()
