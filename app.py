import tempfile
import ling

from flask import Flask, render_template, Response, request
import cv
import os

app = Flask(__name__)


# Views
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/image_upload', methods=['POST'])
def file_upload():
    file = request.files['webcam']
    path = os.getcwd() + '/imagepath.jpg'
    file.save(path)

    recognizer = cv.EmotionRecognizer()
    score = recognizer.get_emotion_from_image(path)
    # update moving avg
    next_line = ling.get_next_line(score)
    return next_line, 200


if __name__ == '__main__':
    app.run(debug=True)
