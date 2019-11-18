from deeppavlov import build_model, configs

model = build_model(configs.classifiers.insults_kaggle_bert , download=False)
while True:
    print(model([str(input('Test Insult: '))]))