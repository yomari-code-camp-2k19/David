from datetime import datetime
from help import help
import logging

class Logger:
    def __init__(self):
        self.logname = '~/david/logs/' + 'log' + datetime.now().strftime("%d-%m-%y") + '.log'
        # self.messages = list()
        logging.basicConfig(filename=self.logname, 
                    format='%(asctime)s %(message)s', 
                    filemode='a')
        #Creating an object 
        self.logger=logging.getLogger() 
        
        #Setting the threshold of logger to DEBUG 
        self.logger.setLevel(logging.DEBUG) 

    # def log(self, message):
    #     self.messages.append(message + '\t' + str(datetime.now()))

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def debug(self, message):
        self.logger.debug(message)

    # def showlog(self):
    #     return [message for message in self.messages]

    # def shutdown(self):
    #     self.logs = open(help.get_project_path() + 'logs' + self.logname, "a+")
    #     self.logs.writelines( list( "%s\n" % item for item in self.messages ) )
    #     self.logs.close()


logger = Logger()
# logger.info("hello")
