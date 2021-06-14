import PySimpleGUI as sg
import math

G = 6.6726e-11
ms = 1.99e30


class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Período orbital em anos: ', justification='center'), sg.Input(key='periodo')],
            [sg.Text('Excentricidade: ', justification='center'), sg.Input(key='excentricidade', pad=(57, 0))],
            [sg.Button('Calcular', pad=(215, 0))],
            [sg.Output(size=(30, 10), pad=(135, 0))],
            [sg.Text('Programa criado por Felipe Bezerra Freitas - IFSP Birigui', pad=(100, 0))]
        ]
        # Janela
        self.janela = sg.Window("Cálculo de Energia Orbital").layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            t = float(self.values['periodo'])
            epsilon = float(self.values['excentricidade'])
            t1 = t * 365.25 * 24 * 3600
            a = ((G * ms) * (t1 ** 2)) / (4 * (math.pi ** 2))
            a1 = pow(a, 1 / 3)
            rmin = a1 * (1 - epsilon)
            rmax = a1 * (1 + epsilon)
            E = (G * (ms ** 2)) / (2 * a1)
            print(f'Energia: {E}\n')
            print(f'Raio: {a}\n')
            print(f'Afélio: {rmax}\n')
            print(f'Periélio: {rmin}\n')
            print('!CÁLCULOS CONCLUíDOS!')


tela = TelaPython()
tela.Iniciar()
