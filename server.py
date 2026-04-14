from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result is None:
        return "Invalid input"

    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
