# Import necessary libraries
import pandas as pd
import spacy

# Import SpacyTextBlob
from spacytextblob.spacytextblob import SpacyTextBlob


# Load the spaCy model
nlp = spacy.load("en_core_web_sm")


# Initialize SpacyTextBlob
spacy_text_blob = SpacyTextBlob(nlp)

# Add SpacyTextBlob to the pipeline
nlp.add_pipe("spacytextblob")

# Enable the component in the pipeline
nlp.enable_pipe("spacytextblob")




# Load the dataset
# Note to user : because the dataset has 41000+ rows it can take time processing and might even lag your pc if it's not powerful
# so I set the number of rows to "nrow = 1000" to stop causing issues, but if you want to run it for the whole dataset at your own risk 
# just delete the rows setter and run the code
data = pd.read_csv("amazon_product_reviews.csv",delimiter="," , dtype={'reviews.text': str}, low_memory=False, nrows=1000)


# Fill NaN values with an empty string
data['reviews.text'] = data['reviews.text'].fillna('')



# Preprocess the text data
def preprocess_text(text):
    """Function to preprocess text by removing stopwords and performing basic text cleaning."""
    doc = nlp(text)  # Process the text with spaCy
    tokens = [token.text.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# Apply preprocessing to the 'review.text' column
data['cleaned_review'] = data['reviews.text'].apply(preprocess_text)

# Define a function for sentiment analysis
def analyze_sentiment(review):
    """Function to analyze the sentiment of a given review."""
    doc = nlp(review)  # Process the review with spaCy
    polarity = doc._.polarity  # Get polarity score
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Test the sentiment analysis function
sample_reviews = [
    "This product is amazing! I love it.",
    "The quality of this product is terrible."
]

print("Sample Reviews Sentiment Analysis:")
for review in sample_reviews:
    sentiment = analyze_sentiment(review)
    print(f"Review: {review} -- Sentiment: {sentiment}")

my_review_of_choice_1 = data['reviews.text'][945]

sentiment = analyze_sentiment(my_review_of_choice_1)
print(f"Review: {my_review_of_choice_1} -- Sentiment: {sentiment}")

my_review_of_choice_2 = data['reviews.text'][683]

sentiment = analyze_sentiment(my_review_of_choice_2)
print(f"Review: {my_review_of_choice_2} -- Sentiment: {sentiment}")
