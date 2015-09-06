from flask import Flask, render_template, Response, request
import numpy

import cv, tempfile, ling

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
    base_64 = request.get_data()
    temp_file = tempfile.NamedTemporaryFile(mode='w+b', suffix='.jpg')
    temp_file.write(base_64.decode('base64'))

    recognizer = cv.EmotionRecognizer()

    sentiment_val = recognizer.get_emotion_from_image(temp_file)
    global past_emotions
    past_emotions.append(sentiment_val)

    return 'OK', 200

@app.route('/poem')
def generate_line():
    # TODO replace dummy val for sentiment
    return ling.get_next_line(get_moving_average())

if __name__ == '__main__':
    app.run(debug=True)
