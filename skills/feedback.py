from david.speechsynthesis import mouth
from david.speechrecognition import ear
from david.help import help


class Feedback:
    def __init__(self):
        with open(help.get_project_path() + 'data/positiveconfirmation.txt') as pc:
            self.pcs = [text.replace('\n','') for text in pc.readlines()]

    def prompt(self, whatfor):
        mouth.speak(whatfor)
        message = str(input(whatfor+ ': '))
        return message

    def confirm(self, summary):
        mouth.speak(summary)
        confirmcode = ear.recognize()
        print(confirmcode)
        if confirmcode in self.pcs:
            print("okay")
        else:
            print("try again")
f = Feedback()
print(f.pcs)
f.confirm("are you sure?")
# while 1:
#     print(f.prompt(str(input("test prompt: "))))