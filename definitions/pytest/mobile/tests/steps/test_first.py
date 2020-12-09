from definitions.pytest.mobile.page.clock.clock_page import ClockPage
from lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Mobile utilizando Pytest
class TestFirst:
    def test_first(self):
        Interact.click('xpath', ClockPage.tab_alarm())
        Interact.click('xpath', ClockPage.tab_timer())
