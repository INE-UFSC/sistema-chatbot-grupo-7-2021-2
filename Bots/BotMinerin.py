from Bots.Bot import Bot

class BotMinerin(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {"1 - Você queria ter praia?":"Sô, não é Minas que não tem mar, é o mar que não têm Minas!",
            "2 - Pão de Queijo ou Queijo Canastra?":"Pão de Queijo com Queijo Canastra",
            "3 - O que significa a sigla GO?":"GOnorante! Mas nós aqui de Minas somo Mai Gonorante ainda!",
        "4 - Onde você mora?":"Eu moro logo ali, na rua de cima do açouque do Valtin, debaixo da rua da Vânia mãe do Zé",
        "5 - Qual o verdadeiro truco?":"O truco de verdade é o trucão com manilha fixa! Esses paulistas que inventam esse trem de manilha alta",
        "6 - Você é atleticano ou cruzeirense?":"GALOOOOOO!"}
    
    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Aoba, bão ô não?! Prazer, sou o {self.__nome}. E ocê, cê é fí de quem?"
    
    def mostra_comandos(self):
        retorno = ""
        for key in list(self.comandos.keys()):
            retorno += "\n"+key
        return retorno

    def executa_comando(self, cmd):
        try:
            if cmd == 1:
                return(self.comandos["1 - Você queria ter praia?"])
            elif cmd == 2:
                return(self.comandos["2 - Pão de Queijo ou Queijo Canastra?"])
            elif cmd == 3:
                return(self.comandos["3 - O que significa a sigla GO?"])
            elif cmd == 4:
                return(self.comandos["4 - Onde você mora?"])
            elif cmd == 5:
                return(self.comandos["5 - Qual o verdadeiro truco?"])
            elif cmd == 6:
                return(self.comandos["6 - Você é atleticano ou cruzeirense?"])
        except:
            return('Atrapaiô o trem tudo!')

    def boas_vindas(self):
        return(f"Prazer, {self.nome}! Eu tenho um primo em Uberlândia com esse mesmo nome.")

    def despedida(self):
        return("Vai não sô, tá cedo!! Fica só mais um cadin, vou passar um cafezin nesse instante.")