from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')

class SaldoSeguro(App):
    def build(self):
        return GUI
    
SaldoSeguro().run()