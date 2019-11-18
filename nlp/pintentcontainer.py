from padatious.intent_container import IntentContainer
from david.config import config


class PadatiousIntentContainer(IntentContainer):
    def __init__(self):
        IntentContainer.__init__(self, cache_dir=config.get_padatious_intent_cache())


container = PadatiousIntentContainer()
