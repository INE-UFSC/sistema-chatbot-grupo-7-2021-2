from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste

class SistemaChatBot:
    lista_bots_ = []
    
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        for i in lista_bots:
            if type(i) == Bot:
                self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Olá, este é o sistema de de chatbots da empresa CrazyBots')
        
    def mostra_menu(self):
        print('''Os chat bots disponíveis no momento são:
              0 - Bot: Yoda - Mensagem de apresentação: Grrrrr. Meu nome é Yoda e eu te odeio!
              1 - Bot: Feliciano - Mensagem de apresentação: Hahaha. Meu nome é Feliciano e eu estou muito feliz!
              2 - Bot: Universitário - Mensagem de apresentação: snif snif. Meu nome é universitário e eu estou triste...''')
    
    def escolhe_bot(self):
        num_bot = int(input('Digite o número do chat bot desejado:'))
        
        if num_bot == 0:
            self.__bot = BotZangado('Yoda')
            SistemaChatBot.lista_bots_.append(self.__bot)
        elif num_bot == 1:
            self.__bot = BotFeliz('Feliciano')
        elif num_bot == 2: 
            self.__bot = BotTriste('Universitário')
        else:
            print('Bot inválido')

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        
    def le_envia_comando(self):
        comando = int(input('Digite o comando desejado (ou -1 para fechar o comando):'))
        if comando == -1:
            return 'sair'
        else: 
            print(self.__bot.executa_comando(comando))

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while True:
            self.mostra_comandos_bot()
            self.le_envia_comando()
            if self.le_envia_comando() == 'sair':
                break