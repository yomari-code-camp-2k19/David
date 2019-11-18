from david.nlp.pintentcontainer import container
from david.config import config


class PadatiousIntentTrainer:
    def __init__(self):
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
        self.train()

    # For intent list
    def add_intent(self, name, lines, reload_cache=True):
        container.add_intent(name, lines, reload_cache)

    # For Entity list
    def add_entity(self, name, lines, reload_cache=True):
        container.add_entity(name, lines, reload_cache)

    # For Intent File
    def load_intent(self, name, filename, reload_cache=True):
        container.load_intent(name, filename, reload_cache)

    # For Entity File
    def load_entity(self, name, filename, reload_cache=True):
        container.load_entity(name, filename, reload_cache)
    
    def train(self):
        container.train()

    def remove_intent(self, name):
        container.remove_intent(name)

    def remove_entity(self, name):
        container.remove_entity(name)

    def add_intent_to_file(self, name, value):
        intent = open(config.get_intent_and_entity_dir() + name + ".intent", 'a+')
        intent.write('\n' + value[0]) if len(value) == 1 else intent.writelines('\n' + v for v in value)
        intent.close()
        self.train()
        
    """
    Adds entity to file
    """
    def add_entity_to_file(self, name, value):
        entity = open(config.get_intent_and_entity_dir() + name + ".entity", 'a+')
        entity.write('\n' + value[0]) if len(value) == 1 else entity.writelines('\n' + v for v in value)
        entity.close()
        self.train()


trainer = PadatiousIntentTrainer()

# trainer.add_entity_to_file(name='city', value=['Berlin'])
