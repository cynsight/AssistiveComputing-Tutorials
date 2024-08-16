# Sentiment Analysis Neural Network Tutorial

This tutorial guides you through the process of designing and training a neural network for sentiment analysis using Python and TensorFlow. For a detailed explanation of this tutorial, see the post: [Designing and Training a Neural Network in Python](https://assistivecomputing.ai/posts/designing-and-training-neural-network-python/)

## Prerequisites

- Basic knowledge of Python programming
- Familiarity with neural network concepts (refer to our [What is a neural network?](https://assistivecomputing.ai/posts/what-is-a-neural-network/) article for a refresher)

## Setup

1. Ensure you have Python 3.7+ installed
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Files in this Tutorial

- `data_generation.py`: Script to generate synthetic movie review data
- `train_network.py`: Main script to prepare data, build, train, and evaluate the neural network
- `data/synthetic_movie_reviews.csv`: Sample synthetic data (1000 reviews)

## Running the Tutorial

1. Generate synthetic data (optional, as sample data is provided):
   ```
   python data_generation.py
   ```
   This will create a new `synthetic_movie_reviews.csv` file with 5000 reviews.

2. Train and evaluate the network:
   ```
   python train_network.py
   ```
   This script will load the data, train the model, and display the results.

## Modifying the Tutorial

Feel free to experiment with the code:
- Adjust the network architecture in `train_network.py`
- Modify data generation parameters in `data_generation.py`
- Try using real movie review data instead of synthetic data

## Additional Resources

For a detailed explanation of this tutorial, see the post: [Designing and Training a Neural Network in Python](https://assistivecomputing.ai/posts/designing-and-training-neural-network-python/)

