import PySimpleGUI as sg

class telapython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown21')
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(20,0), key='nome')],
            [sg.Text('Idade',size=(5,0)), sg.Input(size=(20,0), key='idade')],
            [sg.Text('Qual Provedor de Email e Aceito?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita Cartao')],
            [sg.Radio('Sim', 'cartao',key='aceitacartao')],
            [sg.Radio('Nao', 'cartao',key='naoaceitacartao')],
            [sg.Text('Email', size=(5, 0)), sg.Input(size=(25, 0), key='email')],
            [sg.Slider(range=(0,255), default_value=0, orientation= 'h',size=(15,20), key= 'sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 20))]
        ]
        # Janela
        self.janela = sg.Window('Dados do Usuario').layout(layout)

        # Estrair os dados da tela

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            email = self.values['email']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            aceitacartao = self.values['aceitacartao']
            naoaceitacartao = self.values['naoaceitacartao']
            velocidade = self.values['sliderVelocidade']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'email: {email}')
            print(f'gmail: {gmail}')
            print(f'outlook: {outlook}')
            print(f'yahoo: {yahoo}')
            print(f'aceita cartao: {aceitacartao}')
            print(f'nao aceita cartao: {naoaceitacartao}')
            print(f'velocidade: {velocidade}')

tela = telapython()
tela.Iniciar()