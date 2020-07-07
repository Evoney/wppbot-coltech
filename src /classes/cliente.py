import datetime
import time
from datetime import date

class Cliente:
    def __init__(self, id):
        self.id = id
        self.hora_inicio_atendimento = int(datetime.datetime.now().hour)
        self.minuto_inicio_atendimento = int(datetime.datetime.now().minute)
        self.dia_inicio_atendimento = int(date.today().day)
        self.mes_inicio_atendimento = int(date.today().month)
        self.estado = 1