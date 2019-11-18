from deeppavlov import build_model, configs


class Deeppavlov:
    def __init__(self):
        self.context_model = build_model(configs.squad.squad)

    def process(self, context, question):
        return self.context_model([context],[question])[0]


dp = Deeppavlov()
