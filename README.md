# Sentiment Analysis API

This project is a Flask-based API that performs sentiment analysis on text input using the VADER Sentiment Analyzer. The API can be accessed externally using ngrok, making it available for public requests.

## Features
- **Sentiment Analysis**: Analyze text to return sentiment (positive, negative, neutral) and sentiment scores.
- **Public Access**: Uses ngrok to generate a publicly accessible URL for the local server.
- **JSON Response**: Sentiment results are returned in JSON format.

## Prerequisites
To run this project, you’ll need:
- Python 3.x
- pip for managing dependencies

## Installation
1. Clone or download the project files.
2. Install the required dependencies listed in `requirements.txt`.
3. Set up ngrok by creating an account, obtaining your authtoken, and authenticating ngrok in your terminal.

## Running the API
1. Start the Flask application to launch the local server.
2. ngrok will generate a public URL, allowing external access to the API.

## Usage
You can send POST requests to the API using tools such as:
- curl
- Postman
- Python’s requests library

Use the ngrok-generated URL to make requests to the API.

## Project Files
- **app.py**: Main file containing the Flask application logic.
- **sentiment_analysis.py**: Script with sentiment analysis functions.
- **requirements.txt**: Lists the necessary dependencies.
- **README.md**: Instructions for setup and usage.
