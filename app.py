#!/usr/bin/env python
from flask import Flask, render_template, Response

# emulated camera
from camera import Camera
from flask import render_template

app = Flask(__name__)



# Views
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)



def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
