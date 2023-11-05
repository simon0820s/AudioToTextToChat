from flask import Flask, request, jsonify
from model import useModels
from prepareAudio import useConverter

app = Flask(__name__)


@app.route("/", methods=["POST"])
def upload():
    data = request.get_json()

    audio_b64 = data.get("audio")

    audioWav = useConverter(audio_b64)

    response = useModels(audioWav)


if __name__ == "__main__":
    app.run(debug=True, port=2809, host="0.0.0.0")
