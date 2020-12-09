import os

from lib.utils.date.get_date_time_now import get_date_time_now
from lib.utils.os.get_operational_system import get_operational_system
from lib.utils.settings.settings import Settings


# Função que retorna o nome da plataforma para concatenação no caminho dos testes
def get_platform_path():
    if Settings.platform in ("firefox", "chrome", "edge"):
        return 'web'
    elif Settings.platform == "desktop":
        return 'desktop'
    elif Settings.platform == "mobile":
        return 'mobile'
    elif Settings.platform == "api":
        return 'api'
    else:
        raise Exception('Esta plataforma não é suportada!')


# Função que retorna o caminho raiz da plataforma de testes
def get_current_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        current = way.replace('\n', '').strip()
        return str(current)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        current = way.strip()
        return str(current)


# Função que retorna o caminho da pasta payload no S.O corrente para carregamento dos dados nos testes de API
def get_payload_path(file):
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if Settings.execution_model == "pytest":
            payload = way.replace('\n', '/definitions/pytest/api/page/payload/' + file).strip()
            return str(payload)
        elif Settings.execution_model == "behave":
            payload = way.replace('\n', '/definitions/behave/api/page/payload/' + file).strip()
            return str(payload)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if Settings.execution_model == "pytest":
            payload = way.replace('\n', '\\definitions\\pytest\\api\\page\\payload\\' + file).strip()
            return str(payload)
        elif Settings.execution_model == "behave":
            payload = way.replace('\n', '\\definitions\\behave\\api\\page\\payload\\' + file).strip()
            return str(payload)


# Função que retorna o caminho do arquivo headers.json para carregamento dos dados nos testes de API
def get_headers_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if Settings.execution_model == "pytest":
            headers = way.replace('\n', '/definitions/pytest/api/page/headers.json').strip()
            return str(headers)
        elif Settings.execution_model == "behave":
            headers = way.replace('\n', '/definitions/behave/api/page/headers.json').strip()
            return str(headers)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if Settings.execution_model == "pytest":
            headers = way.replace('\n', '\\definitions\\pytest\\api\\page\\headers.json').strip()
            return str(headers)
        elif Settings.execution_model == "behave":
            headers = way.replace('\n', '\\definitions\\behave\\api\\page\\headers.json').strip()
            return str(headers)


# Função que retorna o caminho do arquivo authentication.json para carregamento dos dados nos testes de API
def get_authentication_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if Settings.execution_model == "pytest":
            authentication = way.replace('\n', '/definitions/pytest/api/page/authentication.json').strip()
            return str(authentication)
        elif Settings.execution_model == "behave":
            authentication = way.replace('\n', '/definitions/behave/api/page/authentication.json').strip()
            return str(authentication)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if Settings.execution_model == "pytest":
            authentication = way.replace('\n', '\\definitions\\pytest\\api\\page\\authentication.json').strip()
            return str(authentication)
        elif Settings.execution_model == "behave":
            authentication = way.replace('\n', '\\definitions\\behave\\api\\page\\authentication.json').strip()
            return str(authentication)


# Função que retorna o caminho do executável do Allure para exibição dos reports pós execução dos testes
def get_allure_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        allure = way.replace('\n', '/lib/tools/allure/bin/allure').strip()
        return str(allure)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        allure = way.replace('\n', '\\lib\\tools\\allure\\bin\\allure.bat').strip()
        return str(allure)


# Função que retorna o caminho do diretório de reports para salvar as execuções e abrir no Allure ou enviar para o X-Ray
def get_reports_path(type):
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if type == "allure":
            reports = way.replace('\n', '/reports/allure/').strip()
            return str(reports)
        elif type == "json":
            reports = way.replace('\n', '/reports/json/').strip()
            return str(reports)
        elif type == "junit":
            reports = way.replace('\n', '/reports/junit/').strip()
            return str(reports)
        else:
            raise Exception('Os tipos de reports suportados são JSON e Allure. Favor escolher uma opção disponível.')
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if type == "allure":
            reports = way.replace('\n', '\\reports\\allure\\').strip()
            return str(reports)
        elif type == "json":
            reports = way.replace('\n', '\\reports\\json\\').strip()
            return str(reports)
        elif type == "junit":
            reports = way.replace('\n', '\\reports\\junit\\').strip()
            return str(reports)
        else:
            raise Exception('Os tipos de reports suportados são JSON e Allure. Favor escolher uma opção disponível.')


# Função que retorna o caminho da pasta features para execução das histórias no BDD
def get_features_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        features = way.replace('\n', '/definitions/behave/%s/features/' % get_platform_path()).strip()
        return str(features)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        features = way.replace('\n', '\\definitions\\behave\\%s\\features\\' % get_platform_path()).strip()
        return str(features)


# Função que retorna o caminho do executável do chromedriver para instanciamento do selenium no Chrome
def get_chromedriver_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        chromedriver = way.replace('\n', '/lib/runner/drivers/chromedriver/chromedriver').strip()
        return str(chromedriver)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        chromedriver = way.strip() + '\\lib\\runner\\drivers\\chromedriver\\chromedriver.exe'
        return str(chromedriver)


# Função que retorna o caminho do executável do geckodriver para instanciamento do selenium no Firefox
def get_geckodriver_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        geckodriver = way.replace('\n', '/lib/runner/drivers/geckodriver/geckodriver').strip()
        return str(geckodriver)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        geckodriver = way.strip() + "\\lib\\runner\\drivers\\geckodriver\\geckodriver.exe"
        return str(geckodriver)


# Função que retorna o caminho do executável do MicrosoftWebDriver para instanciamento do selenium no Edge
def get_msdriver_path():
    if get_operational_system() != "Windows":
        raise Exception("Este sistema operacional não é suportado!")
    else:
        way = os.popen('cd ,').read()
        msdriver = way.strip() + "\\lib\\runner\\drivers\\msedgedriver\\MicrosoftWebDriver.exe"
        return str(msdriver)


# Função que retorna o caminho do executável do Winium.Desktop.Driver para instanciamento do selenium em Desktop
def get_winiumdriver_path():
    if get_operational_system() != "Windows":
        raise Exception("Este sistema operacional não é suportado!")
    else:
        way = os.popen('cd ,').read()
        winiumdriver = way.strip() + "\\lib\\runner\\drivers\\winiumdriver\\Winium.Desktop.Driver.exe"
        return str(winiumdriver)


# Função que retorna o caminho do arquivo de configuração dos testes settings.json
def get_settings_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        settings = way.replace('\n', '/settings/settings.json').strip()
        return str(settings)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        settings = way.strip() + "\\settings\\settings.json"
        return str(settings)


# Função que retorna o caminho do arquivo de screenshot com padrão de data e hora
def get_screenshot_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        settings = way.replace('\n', '/reports/screenshot/screenshot_%s' % get_date_time_now(True) + '.png').strip()
        return str(settings)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        settings = way.strip() + "\\reports\\screenshot\\screenshot_%s" % get_date_time_now(True) + ".png"
        return str(settings)


# Função que retorna o caminho do diretório de testes com base na plataforma e modelo de execução configurados
def get_tests_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if Settings.execution_model == "pytest":
            tests = way.replace('\n', '/definitions/pytest/%s/tests/steps/' % get_platform_path()).strip()
            return str(tests)
        elif Settings.execution_model == "behave":
            tests = way.replace('\n', '/definitions/behave/%s/tests/steps/' % get_platform_path()).strip()
            return str(tests)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if Settings.execution_model == "pytest":
            tests = way.replace('\n', '\\definitions\\pytest\\%s\\tests\\steps\\' % get_platform_path()).strip()
            return str(tests)
        elif Settings.execution_model == "behave":
            tests = way.replace('\n', '\\definitions\\behave\\%s\\tests\\steps\\' % get_platform_path()).strip()
            return str(tests)


def get_lint_path():
    if get_operational_system() == "Linux":
        way = os.popen('pwd').read()
        if Settings.execution_model == "pytest":
            tests = way.replace('\n', '/definitions/pytest/%s/tests/' % get_platform_path()).strip()
            return str(tests)
        elif Settings.execution_model == "behave":
            tests = way.replace('\n', '/definitions/behave/%s/tests/' % get_platform_path()).strip()
            return str(tests)
    elif get_operational_system() == "Windows":
        way = os.popen('cd ,').read()
        if Settings.execution_model == "pytest":
            tests = way.replace('\n', '\\definitions\\pytest\\%s\\tests\\' % get_platform_path()).strip()
            return str(tests)
        elif Settings.execution_model == "behave":
            tests = way.replace('\n', '\\definitions\\behave\\%s\\tests\\' % get_platform_path()).strip()
            return str(tests)
