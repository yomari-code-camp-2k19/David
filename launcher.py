from logger import logger
# from padatious.intent_container import IntentContainer
from david.nlp.pintentcontainer import container
import os
from david.config import config
from david.nlp.intenttrainer import trainer
from david.logger import logger
# from david.hotworddetection import hotword

path = config.get_intent_and_entity_dir()

# container = IntentContainer('test_cache')

class Launcher:
    def __init__(self):
        logger.info("System Starting ...")

    def load_intents(self):
        with os.scandir(path) as it:
            for entry in it:
                if entry.name.endswith(".entity") and entry.is_file():
                    # print(entry.name, entry.path)
                    # value = [line.strip('\n') for line in open(entry.path)]
                    name = entry.name.replace('.entity','')
                    trainer.load_entity(name, entry.path, True)
        with os.scandir(path) as it:            
            for entry in it:
                if entry.name.endswith(".intent") and entry.is_file():
                    # print(entry.name, entry.path)
                    # value = [line.strip('\n') for line in open(entry.path)]
                    name = entry.name.replace('.intent','')
                    trainer.load_intent(name, entry.path, True)
        trainer.train()
        while True:
            print(container.calc_intent(str(input("What do you wanna say?: "))))

    # def start_hotword(self):
    #     hotword.start()

launch = Launcher()
launch.load_intents()

