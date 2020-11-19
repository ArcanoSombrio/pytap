from selenium.webdriver.common.keys import Keys

from structure.definitions.pytest.web.page.google.google_page import GooglePage
from structure.lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Web utilizando Pytest
class TestFirst:
    def test_first(self):
        Interact.open_url(GooglePage.url)
        Interact.send_keys('name', GooglePage.input_search_element(), "PyCharm")
        Interact.send_keys('name', GooglePage.input_search_element(), Keys.ENTER)
