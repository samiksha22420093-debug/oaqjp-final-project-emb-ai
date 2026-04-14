import requests

def emotion_detector(text_to_analyze):
    if text_to_analyze == "":
        return None

    emotions = {
        "anger": 0.1,
        "disgust": 0.1,
        "fear": 0.1,
        "joy": 0.7,
        "sadness": 0.0
    }

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion
    }
