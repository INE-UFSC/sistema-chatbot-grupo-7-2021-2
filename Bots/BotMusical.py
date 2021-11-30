from Bots.Bot import Bot

class BotMusical(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {'1': 'Bom dia', '2': 'Quem é você?',
                           '3': 'Como vai ser o futuro?', '4': 'Adeus'}

    @property
    def comandos(self):
        return self.__comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f'Deixa eu me apresentar, que eu acabei de chegar! Meu nome é {self.__nome}!')
 
    def mostra_comandos(self):
        return('1 - Bom dia \n2 - Quem é você?\n3 - Como vai ser o futuro?')
    
    def executa_comando(self,cmd):
        if cmd == 1:
            return(self.boas_vindas())
        elif cmd ==2:
            return(self.quem_e())
        elif cmd == 3:
            return(self.futuro())
        else:
            return(self.despedida())

   
    def boas_vindas(self):
        return('Alguma coisa acontece no meu coração... Ah, oi! Bom dia!')

    def quem_e(self):
        return(f'EU SOU O SAMBAAA! Brincadeira, eu sou {self.__nome}!')

    def futuro(self):
        return('Eu vejo a vida melhor no futuro, eu vejo isso por cima de um muro\nde hipocrisia que insiste em nos rodear...')

    def despedida(self):
        return('Deixe-me ir, preciso andar, vou por aí a procurar... Rir pra não chorar! Tchaau!')