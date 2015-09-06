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
    base_64 = request.get_data()
    temp_file = tempfile.NamedTemporaryFile(mode='w+b', suffix='.jpg')
    temp_file.write(base_64.decode('base64'))

    recognizer = cv.EmotionRecognizer()
    recognizer.get_emotion_from_image(temp_file)
    return 'OK', 200

@app.route('/poem')
def generate_line():
    # TODO replace dummy val for sentiment
    return ling.get_next_line(1.0)

if __name__ == '__main__':
    app.run(debug=True)
