from fer import FER

emotion_detector = FER(mtcnn=True)

stress_weights = {
    "happy": 5,
    "neutral": 12,
    "surprise": 18,
    "sad": 22,
    "disgust": 26,
    "angry": 35,
    "fear": 40
}

HIGH_STRESS_RECS = [
    {"text": "Take slow deep breaths", "link": "https://www.youtube.com/watch?v=odADwWzHR24"},
    {"text": "Stop work for a few minutes", "link": "https://www.youtube.com/watch?v=inpok4MKVLM"},
    {"text": "Drink cold water", "link": "https://www.youtube.com/watch?v=9iMGFqMmUFs"},
    {"text": "Sit quietly and calm down", "link": "https://www.youtube.com/watch?v=ZToicYcHIOU"},
    {"text": "Listen to calm music", "link": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"}
]

MEDIUM_STRESS_RECS = [
    {"text": "Stretch your body", "link": "https://www.youtube.com/watch?v=v7AYKMP6rOE"},
    {"text": "Try light breathing exercise", "link": "https://www.youtube.com/watch?v=odADwWzHR24"},
    {"text": "Take a short work break", "link": "https://www.youtube.com/watch?v=hnpQrMqDoqE"},
    {"text": "Drink water or tea", "link": "https://www.youtube.com/watch?v=9iMGFqMmUFs"}
]

LOW_STRESS_RECS = [
    {"text": "Maintain daily routine", "link": "https://www.youtube.com/watch?v=ZToicYcHIOU"},
    {"text": "Sleep on time", "link": "https://www.youtube.com/watch?v=nm1TxQj9IsQ"},
    {"text": "Do light exercise", "link": "https://www.youtube.com/watch?v=ml6cT4AZdqI"},
    {"text": "Spend time with family or friends", "link": "https://www.youtube.com/watch?v=9iMGFqMmUFs"},
    {"text": "Do your favorite hobby", "link": "https://www.youtube.com/watch?v=VYOjWnS4cMY"}
]

def analyze_frame(frame):
    emotions = emotion_detector.detect_emotions(frame)

    if not emotions:
        return None

    emotion, confidence = max(
        emotions[0]["emotions"].items(),
        key=lambda x: x[1]
    )

    if confidence < 0.40:
        return None

    base_stress = stress_weights.get(emotion, 10)
    stress_score = int(base_stress * confidence)
    stress_score = min(stress_score, 40)

    if emotion in ["angry", "fear"]:
        stress_level = "High Stress"
        recommendations = HIGH_STRESS_RECS
    else:
        if stress_score <= 15:
            stress_level = "Low Stress"
            recommendations = LOW_STRESS_RECS
        elif stress_score <= 25:
            stress_level = "Medium Stress"
            recommendations = MEDIUM_STRESS_RECS
        else:
            stress_level = "High Stress"
            recommendations = HIGH_STRESS_RECS

    warning = True if stress_level == "High Stress" else False

    return {
        "emotion": emotion,
        "stress_level": stress_level,
        "stress_percentage": stress_score,
        "recommendations": recommendations,
        "warning": warning
    }