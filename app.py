#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotMusical import BotMusical
from Bots.BotMinerin import BotMinerin
from Bots.BotMarombeiro import BotMarombeiro
from Bots.BotManezinho import BotManezinho
from Bots.BotJose import BotJose
from Bots.BotGamer import BotGamer
from Bots.BotEspelhado import BotEspelhado
from Bots.BotCansado import BotCansado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Universitário"), BotFeliz("Feliciano"), BotMusical("Mozart"), BotMinerin("João"), BotMarombeiro("Bambam"), BotManezinho("Guxtavo"), BotJose("José"), BotGamer("clebin_gamer23"), BotEspelhado("Espelho"), BotCansado("ZzZz")]
sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
