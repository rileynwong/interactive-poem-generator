import os
import subprocess

assets_dir = '{}/cv/emotime-1.2-experimental/assets'.format(os.getcwd())
cmd_text = 'cd {} && ./emo_detector_cli svm ../resources/haarcascade_frontalface_cbcl1.xml ' \
           '../resources/haarcascade_eye.xml 52 52 1 5 8 ../svm_1vsallext_1_5_8_95c2eb0b58/*'\
           .format(assets_dir)

emotion_to_polarity = {
    'neutral': 0,
    'anger': -1,
    'contempt': -1,
    'disgust': -1,
    'fear': -1,
    'happy': 1,
    'sadness': -1,
    'surprise': 1,
    'others': 0,
    'unknown': 0,
}


class EmotionRecognizer:
    def __init__(self):
        self.cmd = new_command()
        self.cmd.stdout.readline()  # 'Insert the image file path:'

    def get_emotion_from_image(self, named_file):
        cmd = self.cmd
        filepath = file.name

        if cmd.poll() is not None:
            self.cmd = new_command()
            self.cmd.stdout.readline()

        cmd.stdin.write(filepath + '\n')
        cmd.stdout.readline()  # Processing <filepath>
        result = timeout(cmd.stdout.readline, timeout_duration=1)
        if result is not None:
            # map the raw result to a polarity score
            result = result.replace('\n', '')
            result = result[result.find(': ') + 2:]
            result = result[:result.find(' ')]
            result = emotion_to_polarity[result]
            cmd.stdout.readline()
        return result


def new_command():
    return subprocess.Popen(cmd_text,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()
    # set the timeout handler
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)

    return result

