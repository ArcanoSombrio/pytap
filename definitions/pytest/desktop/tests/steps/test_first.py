from definitions.pytest.desktop.page.calculator.calculator_page import CalculatorPage
from lib.runner.execute.interact.interact import Interact


# Exemplo de classe de testes Desktop utilizando Pytest
class TestFirst:
    def test_first(self):
        Interact.click('name', CalculatorPage.button_one())
        Interact.click('name', CalculatorPage.button_plus())
        Interact.click('name', CalculatorPage.button_seven())
        Interact.click('name', CalculatorPage.button_equals())
