from behave import *

from definitions.behave.desktop.page.calculator.calculator_page import CalculatorPage
from lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Desktop utilizando BDD
class TestFirst:
    response = None

    @given(u'que eu acesse a calculadora do Windows')
    def open(context):
        pass

    @When(u'eu clicar em 1')
    def send(context):
        Interact.click('name', CalculatorPage.button_one())

    @When(u'clicar em +')
    def send(context):
        Interact.click('name', CalculatorPage.button_plus())

    @When(u'clicar em 7')
    def send(context):
        Interact.click('name', CalculatorPage.button_seven())

    @When(u'clicar em =')
    def send(context):
        Interact.click('name', CalculatorPage.button_equals())

    @Then(u'a soma é realizada')
    def send(context):
        pass
