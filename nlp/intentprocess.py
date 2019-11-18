from david.nlp.pintentcontainer import container


class IntentProcess:
    def __init__(self):
        pass

    def process(self, query):
        return container.calc_intent(query).name


intent = IntentProcess()