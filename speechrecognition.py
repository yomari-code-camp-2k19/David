import json
from logger import logger
import azure.cognitiveservices.speech as speechsdk
from david.help import help
# from david.hotworddetection import h
# from nlp.

# with open(help.get_project_path() + 'config.json') as data:
#     config = json.load(data)


class SpeechRecognizer:
    def __init__(self):
        logger.info('loading configuration')
        with open(help.get_project_path() + 'config.json') as data:
            self.config = json.load(data)
        self.speech_key, self.service_region = self.config["speech"]["azure"]["key1"], self.config["speech"]["azure"]["region"]
        self.speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        logger.info('configuration loaded')
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def recognize(self):
        # h.stop()
        logger.info("Listening..")
        result = self.speech_recognizer.recognize_once()
        print('listening..')

        # Checks result.
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            logger.info("Recognized: {}".format(result.text))
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            logger.warning("No speech could be recognized: {}".format(result.no_match_details))
            return False
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            logger.warning("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                logger.error("Error details: {}".format(cancellation_details.error_details))
            return False


ear = SpeechRecognizer()
# import time
# while True:
#     print('starting in 2 seconds')
#     time.sleep(2)
#     print('listening..')
#     print(ear.recognize())
#     print('stopped')