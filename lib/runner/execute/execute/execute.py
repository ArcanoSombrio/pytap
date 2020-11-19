from behave.__main__ import main as behave_main
from pytest import main as pytest_main
from pylint.lint import Run as PylintRun

from structure.lib.runner.execute.interact.interact import Interact
from structure.lib.utils.date.get_date_time_now import get_date_time_now
from structure.lib.utils.json_dict.get_settings import get_model_settings, get_platform_settings
from structure.lib.utils.json_dict.get_settings import get_headless_settings, get_lint_settings
from structure.lib.utils.path.get_path import get_features_path, get_reports_path
from structure.lib.utils.path.get_path import get_tests_path, get_lint_path
from structure.lib.utils.settings.settings import Settings


# Função que faz a chamada dos métodos de carregamento das configurações do arquivo settings.json
def load_settings():
    get_model_settings()
    get_platform_settings()
    get_headless_settings()
    get_lint_settings()


# Classe que realiza a execução dos testes passados em lista
class Execute:
    # Função principal que chama o carregamento das configurações, setup do ambiente, execução dos testes e teardown
    def __init__(self, test_stories_list):
        load_settings()
        self.execute_lint_verification()
        Interact.setup()
        self.execute_tests_with_settings(test_stories_list)
        Interact.teardown()

    # Método estático que realiza execução da lista de testes passada como argumento
    @staticmethod
    def execute_tests_with_settings(test_stories_list):
        try:
            if Settings.execution_model == "pytest":
                for test in test_stories_list:
                    pytest_main(
                        [
                            get_tests_path() + test,
                            '--alluredir=%s' % get_reports_path("allure"),
                            '--json=%s' % get_reports_path("json") + get_date_time_now(True) + '_test_result.json',
                            '--cache-clear',
                            '--cov=%s' % get_tests_path(),
                            '--disable-warnings'
                        ]
                    )
            elif Settings.execution_model == "behave":
                for story in test_stories_list:
                    behave_main(
                        [
                            get_features_path() + story,
                            '-v',
                            '--summary',
                            '--capture-stderr',
                            '--capture',
                            '--logcapture',
                            '--logging-level=DEBUG',
                            '-f=allure_behave.formatter:AllureFormatter',
                            '-o=%s' % get_reports_path("allure"),
                            '-f=json',
                            '-o=%s' % get_reports_path("json") + get_date_time_now(True) + '_test_result.json',
                            '--logging-format="%(asctime) s: %(levelname) s: %(message) s"',
                            '--logging-datefmt="%d/%m/%y %I:%M:%S"',
                            '--show-timings'
                        ]
                    )
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
                    get_lint_path()
                ]
            )
