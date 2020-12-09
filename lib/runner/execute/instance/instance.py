import json
import os
from json.decoder import JSONDecodeError

import requests_mock
from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver, webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from lib.utils.settings.settings import Settings
from lib.utils.validate.validate_status_code import validate_status_code
from lib.utils.os.get_operational_system import get_operational_system
from lib.utils.path.get_path import get_msdriver_path, get_geckodriver_path
from lib.utils.path.get_path import get_chromedriver_path, get_winiumdriver_path


# Classe que cria a instância dos drivers do Selenium para cada platafoma
class Instance:
    driver = None

    # Função principal que seta a variável driver que receberá a instância do Selenium
    def __init__(self):
        self.driver = self.driver

    # Função que cria a instância do driver do Selenium para o navegador Chrome
    def chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = selenium_driver.Chrome(
            get_chromedriver_path(),
            chrome_options=chrome_options
        )
        self.driver.maximize_window()

    # Função que cria a instância do driver do Selenium para o navegador Firefox
    def firefox_driver(self):
        firefox_profile = selenium_driver.FirefoxProfile()
        firefox_profile.set_preference(
            'webdriver.load.strategy',
            'unstable'
        )
        capabilities = DesiredCapabilities().FIREFOX
        if get_operational_system() == "Linux":
            capabilities["marionette"] = True
        elif get_operational_system() == "Windows":
            capabilities["marionette"] = False

        self.driver = selenium_driver.Firefox(
            capabilities=capabilities,
            firefox_profile=firefox_profile,
            executable_path=r'' + get_geckodriver_path()
        )

    # Função que cria a instância do driver do Selenium para o navegador Edge
    def edge_driver(self):
        os.popen(get_msdriver_path())
        self.driver = selenium_driver.Edge()
        self.driver.maximize_window()

    # Função que cria a instância do driver do Selenium para aplicações Desktop
    def winium_driver(self):
        os.popen(get_winiumdriver_path())
        self.driver = selenium_driver.Remote(
            command_executor='http://localhost:9999',
            desired_capabilities={
                'debugConnectToRunningApp': 'false',
                'app': Settings.application_path
            }
        )

    # Função que cria a instância da conexão com o Appium para execução em Mobile
    def appium_driver(self):
        self.driver = appium_driver.Remote(
            command_executor=Settings.command_executor,
            desired_capabilities={
                'platformName': Settings.platform_name,
                'platformVersion': Settings.platform_version,
                'deviceName': Settings.device_name,
                'appPackage': Settings.application_package,
                'appActivity': Settings.application_activity,
                'automationName': Settings.automation_name,
                'browserName': Settings.browser_name,
                'app': Settings.app,
                'noReset': Settings.no_reset,
                'mcWorkspaceName': Settings.workspace_name,
                'oauthClientId': Settings.oauth_client_id,
                'oauthClientSecret': Settings.oauth_client_secret,
                'tenantId': Settings.tenant_id,
                'autoGrantPermissions': Settings.auto_grant_permissions,
                'udid': Settings.udid
            } if Settings.platform_name == "Android" else
            {
                'platformName': Settings.platform_name,
                'platformVersion': Settings.platform_version,
                'deviceName': Settings.device_name,
                'automationName': Settings.automation_name,
                'browserName': Settings.browser_name,
                'app': Settings.app,
                'noReset': Settings.no_reset,
                'mcWorkspaceName': Settings.workspace_name,
                'oauthClientId': Settings.oauth_client_id,
                'oauthClientSecret': Settings.oauth_client_secret,
                'tenantId': Settings.tenant_id,
                'autoGrantPermissions': Settings.auto_grant_permissions,
                'udid': Settings.udid
            }
        )

    # Método estático que cria uma requisição genérica com PyPac
    @staticmethod
    def pypac_request(mock, session, text, method, url, headers, payload):
        if mock is False:
            request = session.request(method=method, url=url, headers=headers, data=payload)
            status_code = request.status_code
            validate_status_code(status_code)
            try:
                response = request.json()
            except JSONDecodeError:
                response = {}

            return response
        elif mock:
            adapter = requests_mock.Adapter()
            session.mount('mock://', adapter)
            adapter.register_uri(method=method, url=url, text=text, _real_http=False)
            request = session.request(method=method, url=url, headers=headers, data=payload)
            status_code = request.status_code
            validate_status_code(status_code)
            try:
                response = json.dumps(request.text)
            except JSONDecodeError:
                response = {}

            return response
