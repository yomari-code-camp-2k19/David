import os



class Help:
    def __init__(self):
        self.projectpath = os.getcwd()

    def get_project_path(self):
        return "~/david/"

help = Help()

