from behave.__main__ import main as behave_main
from pytest import main as pytest_main
from pylint.lint import Run as PylintRun

from lib.runner.execute.interact.interact import Interact
from lib.utils.settings.settings import Settings


# Classe que realiza a execução dos testes passados em lista
class Execute:
    # Função principal que chama o carregamento das configurações, setup do ambiente, execução dos testes e teardown
    def __init__(self, test_stories_list):
        Interact.load_settings()
        self.execute_lint_verification()
        Interact.setup()
        self.execute_tests_with_settings(test_stories_list)
        Interact.teardown()

    # Método estático que realiza execução da lista de testes passada como argumento
    @staticmethod
    def execute_tests_with_settings(test_stories_list):
        try:
            if Settings.execution_model == "pytest":
                Interact.stop_allure_serve()
                for test in test_stories_list:
                    pytest_main(
                        [
                            Interact.call_get_tests_path() + test,
                            '--alluredir=%s' % Interact.call_get_reports_path("allure"),
                            '--json=%s' % Interact.call_get_reports_path("json") + Interact.call_get_date_time_now(True) + '_test_result.json',
                            '--cache-clear',
                            '--cov=%s' % Interact.call_get_tests_path(),
                            '--disable-warnings'
                        ]
                    )
                    Interact.start_allure_serve()
            elif Settings.execution_model == "behave":
                Interact.stop_allure_serve()
                for story in test_stories_list:
                    behave_main(
                        [
                            Interact.call_get_features_path() + story,
                            '-v',
                            '--summary',
                            '--capture-stderr',
                            '--capture',
                            '--logcapture',
                            '--logging-level=DEBUG',
                            '-f=allure_behave.formatter:AllureFormatter',
                            '-o=%s' % Interact.call_get_reports_path("allure"),
                            '-f=json',
                            '-o=%s' % Interact.call_get_reports_path("json") + Interact.call_get_date_time_now(True) + '_test_result.json',
                            '--logging-format="%(asctime) s: %(levelname) s: %(message) s"',
                            '--logging-datefmt="%d/%m/%y %I:%M:%S"',
                            '--show-timings'
                        ]
                    )
                Interact.start_allure_serve()
        except Exception as e:
            if Settings.platform in ("firefox", "chrome", "edge", "desktop"):
                Interact.get_screenshot()
                Interact.teardown()
                print(e)

    # Método estático que executa a verificação Lint de cobertura do código de testes conforme configuração
    @staticmethod
    def execute_lint_verification():
        if Settings.lint:
            PylintRun(
                [
                    Interact.call_get_lint_path()
                ]
            )
