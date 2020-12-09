from definitions.pytest.mobile.page.page import Page


# Exemplo de classe de página herdando atributos da classe de página genérica
class ClockPage(Page):
    url = ''
    title = 'Clock'

    def __init__(self):
        Page.__init__(self)
        self.url = self.url
        self.title = self.title

    @staticmethod
    def tab_alarm():
        return '//*[@class="android.widget.TextView"][@text="Alarm"]'

    @staticmethod
    def tab_timer():
        return '//*[@class="android.widget.TextView"][@text="Timer"]'
