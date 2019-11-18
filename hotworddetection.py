import signal
import sys

from david.config import config
from david.hotword.snowboy import snowboydecoder
from david.speechrecognition import ear
from david.speechsynthesis import mouth
from david.nlp.intentprocess import intent


class SnowboyHotwordDetector:
    def __init__(self):
        self.models = config.get_hotword_model()
        self.interrupted = False
        self.sensitivity = [0.48]*len(self.models)
        signal.signal(signal.SIGINT, self.signal_handler)
        self.detector = snowboydecoder.HotwordDetector(self.models, sensitivity=self.sensitivity)
        self.callbacks = [lambda: self.recognize(),
             lambda: self.recognize(),
             lambda: self.recognize()]

    def signal_handler(self, signal, frame):
        self.interrupted = True

    def interrupt_callback(self):
        return self.interrupted

    def start(self):
        print('Listening... Press Ctrl+C to exit')
        self.detector.start(detected_callback=self.callbacks,
               interrupt_check=self.interrupt_callback,
               sleep_time=0.03)

    def recognize(self):
        print("Listening to your voice")
        snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING)
        ear.recognize()

    def stop(self):
        self.detector.terminate()


h = SnowboyHotwordDetector()
