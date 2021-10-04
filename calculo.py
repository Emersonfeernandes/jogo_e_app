from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 600)
Builder.load_file('calculadora.kv')

class Teclado(Widget):
    def clear(self):
        self.ids.calcolo_feito.text = '0'

    def button_press(self, button):
        var = self.ids.calcolo_feito.text
        if var == '0':
            self.ids.calcolo_feito.text = ''
            self.ids.calcolo_feito.text = f'{button}'
        else:
            self.ids.calcolo_feito.text = f'{var}{button}'

    def remover(self):
        var = self.ids.calcolo_feito.text
        var = var[:-1]
        self.ids.calcolo_feito.text = var

    def virgula(self):
        var = self.ids.calcolo_feito.text
        if ',' in var:
            pass
        else:
            var = f'{var},'
            self.ids.calcolo_feito.text = var

    def ponto(self):
        var = self.ids.calcolo_feito.text
        if '.' in var:
            pass
        else:
            var = f'{var}.'
            self.ids.calcolo_feito.text = var

    def math_sinal(self, sinal):
        var = self.ids.calcolo_feito.text
        self.ids.calcolo_feito.text = f'{var}{sinal}'

    def equals(self):
        var = self.ids.calcolo_feito.text
        if '+' in var:
            numlista = var.split('+')
            num = 0
            for numero in numlista:
                num = num + int(numero)
            self.ids.calcolo_feito.text = str(num)
        if '*' in var:
            numlista = var.split('*')
            num = 0
            for numero in numlista:
                indece = 0
                indece1 = 1
                num = int(numlista[indece]) * int(numlista[indece1])
                indece1 = indece1 + 1
            self.ids.calcolo_feito.text = str(num)
        if '-' in var:
            numlista = var.split('-')
            num = 0
            for numero in numlista:
                indece = 0
                indece1 = 1
                num = int(numlista[indece]) - int(numlista[indece1])
                indece1 = indece1 + 1
            self.ids.calcolo_feito.text = str(num)
        if '/' in var:
            numlista = var.split('/')
            num = 0
            for numero in numlista:
                indece = 0
                indece1 = 1
                if int(numlista[indece1]) == 0:
                    num = str('Não divide por 0')
                else:
                    num = int(numlista[indece]) / int(numlista[indece1])
                indece1 = indece1 + 1
            self.ids.calcolo_feito.text = str(num)

class Calculadora_k(App):
    def build(self):
        return Teclado()

Calculadora_k().run()
