from behave import *

from definitions.behave.mobile.page.clock.clock_page import ClockPage
from lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Mobile utilizando BDD
class TestFirst:
    response = None

    @given(u'que eu acesse o aplicativo Clock no Android')
    def open(context):
        pass

    @When(u'eu clicar em Alarm')
    def send(context):
        Interact.click('xpath', ClockPage.tab_alarm())

    @When(u'clicar em Timer')
    def send(context):
        Interact.click('xpath', ClockPage.tab_timer())

    @Then(u'as abas são trocadas')
    def send(context):
        pass
