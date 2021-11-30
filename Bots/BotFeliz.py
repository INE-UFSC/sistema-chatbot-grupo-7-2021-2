from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)

    def apresentacao(self):
        return(f"Meu nome é {self.nome}! Fico muito feliz de conversar com você :) !!!")
 
    def mostra_comandos(self):
        return("1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus")
    
    def executa_comando(self,cmd):
        if cmd == 1:
            return(self.boas_vindas())
        if cmd == 2:
            return(f"{self.nome} :D")
        if cmd == 3:
            return(self.conselho())
        if cmd == 4:
            return(self.despedida())
        else:
            return ("Comando inválido")

    def boas_vindas(self):
        return("Olá, como você está? Obrigado por me chamar!")
    
    def conselho(self):
        return("Sorria, a vida é uma só!")

    def despedida(self):
        return("Tenha um bom dia!")