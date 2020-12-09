from lib.runner.execute.interact.interact import Interact

request_session = None
url, payload = Interact.load_request_data('tag', 'payload.json')
text = '{"test_1": 1, "test_2": "two", "test_3": "iii"}'


# Exemplo de classe de testes de API utilizando Pytest e Mock
class Test:
    def test_first(self):
        response = Interact.send_get(
            mock=True,
            session=_session,
            text=text,
            url=url,
            payload=payload
        )
        print(response)
