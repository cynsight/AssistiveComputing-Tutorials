import random
import numpy as np
import pandas as pd

positive_words = ["good", "great", "fantastic", "amazing", "excellent", "wonderful", "positive", "enjoyable", "pleasant", "satisfying"]
negative_words = ["bad", "terrible", "awful", "horrible", "negative", "poor", "disappointing", "unpleasant", "dismal", "unsatisfactory"]

def generate_review():
    word_count = random.randint(50, 200)
    review_words = []
    positive_word_count = 0
    negative_word_count = 0
    contains_excellent = 0
    contains_terrible = 0

    for _ in range(word_count):
        if random.random() > 0.5:
            word = random.choice(positive_words)
            positive_word_count += 1
            if word == "excellent":
                contains_excellent = 1
        else:
            word = random.choice(negative_words)
            negative_word_count += 1
            if word == "terrible":
                contains_terrible = 1
        review_words.append(word)

    review_text = " ".join(review_words)
    avg_word_length = np.mean([len(word) for word in review_words])
    positive_review = 1 if positive_word_count > negative_word_count else 0

    return {
        "Review Text": review_text,
        "Word Count": word_count,
        "Average Word Length": avg_word_length,
        "Positive Words": positive_word_count,
        "Negative Words": negative_word_count,
        "Contains 'excellent'": contains_excellent,
        "Contains 'terrible'": contains_terrible,
        "Positive Review": positive_review
    }

# Generate dataset
number_reviews = 5000
reviews = [generate_review() for _ in range(number_reviews)]
df = pd.DataFrame(reviews)

# Save to CSV
df.to_csv('synthetic_movie_reviews.csv', index=False)

