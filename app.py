import tempfile
import ling

from flask import Flask, render_template, Response, request
import cv

app = Flask(__name__)


# Views
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/image_upload', methods=['POST'])
def file_upload():
    file = request.files
    path = '.imagepath'
    file.save()

    recognizer = cv.EmotionRecognizer()
    score = recognizer.get_emotion_from_image(path)
    return 'OK', 200

@app.route('/poem')
def generate_line():
    # TODO replace dummy val for sentiment
    return ling.get_next_line(1.0)

if __name__ == '__main__':
    app.run(debug=True)
