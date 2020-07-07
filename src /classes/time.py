import datetime
import time
from datetime import date

class Data:
    def __init__(self):
        self.hora = int(datetime.datetime.now().hour)
        self.minuto = int(datetime.datetime.now().minute)
        self.dia = int(date.today().day)
        self.mes = int(date.today().month)


