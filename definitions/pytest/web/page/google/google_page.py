from structure.definitions.pytest.web.page.page import Page


# Exemplo de classe de página herdando atributos da classe de página genérica
class GooglePage(Page):
    url = 'https://www.google.com/'
    title = 'Google'

    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    @staticmethod
    def input_search_element():
        return 'q'
