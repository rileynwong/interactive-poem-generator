import tempfile
import ling

from flask import Flask, render_template, Response, request
import numpy

import cv, tempfile, ling
import os

app = Flask(__name__)

past_emotions = []


## Functions
def get_moving_average():
    if len(past_emotions) > 4:
        return numpy.mean(past_emotions)
    elif past_emotions:
        return past_emotions[0]
    else:
        return 1.0


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
    if score is None:
        score = 0
    past_emotions.append(score)
    if len(past_emotions) == 5:
        past_emotions.pop(0)
    next_line = ling.get_next_line(get_moving_average())
    return next_line, 200


if __name__ == '__main__':
    app.run(debug=True)
