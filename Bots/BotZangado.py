from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return(self.__nome)

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f"Grrrrrr. Meu nome é {self.nome} e eu te odeio!")
 
    def mostra_comandos(self):
        return("1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus")
    
    def executa_comando(self,cmd):
        if cmd == 1:
            return(self.boas_vindas())
        if cmd == 2:
            return(f"{self.nome}, quantas tenho tenho que repetir?")
        if cmd == 3:
            return(self.conselho())
        if cmd == 4:
            return(self.despedida())
        else:
            return ("Comando inválido")

    def boas_vindas(self):
        return("Olá, como você vai me encher o saco hoje?")
    
    def conselho(self):
        return("Não tenho filho desse tamanho.")

    def despedida(self):
        return("Já vai tarde. Adeus.")