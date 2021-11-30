from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste

class SistemaChatBot:    
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        self.__bot = None
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
    
    def boas_vindas(self):
        print('Olá, este é o sistema de de chatbots da empresa CrazyBots')
        
    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são:")
        for index, bot in enumerate(self.__lista_bots):
            print(f'{index + 1} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()}')
    
    def escolhe_bot(self):
        while True:
            num_bot = input('Digite o número do chat bot desejado:')
            if not num_bot.isnumeric():
                print("Erro. Escolha um número")
            elif int(num_bot) > len(self.__lista_bots) or int(num_bot) < 1:
                print(f"Escolha um bot entre 1 e {len(self.__lista_bots)}")
            else:
                break
        
        num_bot = int(num_bot)
        self.__bot = self.__lista_bots[num_bot - 1]

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        
    def le_envia_comando(self):
        comando = int(input('Digite o comando desejado (ou -1 para fechar o comando):'))
        if comando == -1:
            return True
        else: 
            print(self.__bot.executa_comando(comando))

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            if self.le_envia_comando(): break