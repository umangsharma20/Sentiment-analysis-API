from flask import Flask, request, jsonify
from sentiment_analysis import analyze_sentiment
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    # Start ngrok and expose the Flask app to the internet
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")
    
    # Start Flask app
    app.run(port=5000)
