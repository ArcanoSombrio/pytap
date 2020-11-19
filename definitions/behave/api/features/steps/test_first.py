from behave import *

from structure.lib.runner.execute.interact.interact import Interact


# Exemplo de classe de teste de API em BDD sem Mock
class TestFirst:
    response = None

    @given(u'que eu envio uma requisição GET para o endereço')
    def send(context):
        context.response = Interact.send_get(
            mock=False,
            session=context._session,
            text=None,
            url=context.url,
            payload=context.payload
        )

    @Then(u'eu recebo o retorno da requisição')
    def show(context):
        print(context.response)
