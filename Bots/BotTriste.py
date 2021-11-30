from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return(self.__nome)

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f"Eu sou {self.nome}, me empresta dinheiro pra comprar café?")
 
    def mostra_comandos(self):
        return("1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus")
    
    def executa_comando(self,cmd):
        if cmd == 1:
            return(self.boas_vindas())
        if cmd == 2:
            return(f"Eu sou {self.nome}, perguntas repetidas me deixam triste e cansado")
        if cmd == 3:
            return(self.conselho())
        if cmd == 4:
            return(self.despedida())
        else:
            return ("Comando inválido")

    def boas_vindas(self):
        return("Bom dia? talvez para os outros bots...")

    def despedida(self):
        return("Mais um que se vai, eu já deveria ter percebido...")

    def conselho(self):
        return("Não confie em ninguém, principalmente em você mesmo.")