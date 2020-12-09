from definitions.behave.desktop.page.page import Page


# Exemplo de classe de página herdando atributos da classe de página genérica
class CalculatorPage(Page):
    title = 'Calculadora'

    def __init__(self):
        Page.__init__(self)
        self.title = self.title

    @staticmethod
    def button_one():
        return '1'

    @staticmethod
    def button_plus():
        return '+'

    @staticmethod
    def button_seven():
        return '7'

    @staticmethod
    def button_equals():
        return '='


