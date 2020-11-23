from lib.runner.execute.execute.execute import Execute


# Classe principal da plataforma de testes que recebe a lista de testes e chama a execução
class Main:
    def __init__(self, test_stories_list):
        Execute(test_stories_list)


# Instrução onde é passada a lista de testes como parâmetro para a classe Main
if __name__ == '__main__':
    Main(
        [
            # 'test_first.py',
            'story.feature'
        ]
    )
