from behave import *
from selenium.webdriver.common.keys import Keys

from definitions.behave.web.page.google.google_page import GooglePage
from lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Web utilizando BDD
class TestFirst:
    response = None

    @given(u'que eu acesso a página do Google')
    def open(context):
        Interact.open_url(GooglePage.url)

    @When(u'eu digitar o texto no campo de pesquisa')
    def send(context):
        Interact.send_keys('name', GooglePage.input_search_element(), "PyCharm")

    @When(u'teclar ENTER ou clicar em Pesquisa Google')
    def send(context):
        Interact.send_keys('name', GooglePage.input_search_element(), Keys.ENTER)

    @Then(u'a pesquisa é realizada')
    def send(context):
        pass
