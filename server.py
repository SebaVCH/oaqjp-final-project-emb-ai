from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renderiza la página principal de la aplicación."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "¡Texto inválido! Por favor, intenta de nuevo."

    return (
        f"Para la frase dada, el sistema de detección de emociones indica "
        f"los siguientes resultados:\n"
        f"Enfado (anger): {response['anger']}\n"
        f"Repugnancia (disgust): {response['disgust']}\n"
        f"Miedo (fear): {response['fear']}\n"
        f"Alegría (joy): {response['joy']}\n"
        f"Tristeza (sadness): {response['sadness']}\n"
        f"La emoción dominante es: {response['dominant_emotion']}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)