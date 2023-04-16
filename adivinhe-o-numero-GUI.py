import random
import PySimpleGUI as sg
import time

class ChuteNumero:
    def __init__(self): #Sempre criamos uma função/método para 'iniciar' a Classe, com os atributos desta classe.
        self.valor_min = 0
        self.valor_max = 10
        self.tentar_novamente = True

    def Iniciar(self): #Após isso, sempre criamos um método para executar as ações daquela Classe.
        #Vamos criar a janela que queremos que o jogo apareça
        #Layout dessa janela
        layout = [
            [sg.Text('Seu chute', size=(100,0))],
            [sg.Input(size=(50,0),key='ValorChute')],
            [sg.Button("Chutar!")],
            [sg.Output(size=(20,10))]
        ]
        #Criação da janela propriamente dita
        self.janela = sg.Window("Adivinhe o número!", layout=layout)
        
        self.GerarNumeroAleatorio()       
        try:
            while True:
                #Fazer com que essa janela receba valores:
                self.evento, self.valores = self.janela.Read()
                if self.evento == sg.WIN_CLOSED:
                    print("Até logo!")
                    self.janela.close()
                    break
                #Fazer algo com esses valores:
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo.")
                            break
                        if int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto.")
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            print("Parabéns! Acertou!!!")
                            self.tentar_novamente = False
                            print("Nosso jogo foi muito bom! Até a próxima!!!")
                            break
                            
            
                
        except:
            print("Digite apenas números.")
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_min, self.valor_max)


#Lembra sempre de que, ao criar uma Classe, temos que instanciar ela!!!
numero = ChuteNumero() #Aqui eu instanciei a Classe ChumeNumero
numero.Iniciar() #Aqui eu 'chamei' o método Iniciar() da instância numero