from appium.webdriver.common.touch_action import TouchAction
from pypac import PACSession
from requests.auth import HTTPBasicAuth
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from lib.utils.json_dict.load_authentication import load_authentication
from lib.utils.json_dict.load_data import load_data
from lib.utils.reports.allure_serve import open_serve, stop_serve
from lib.utils.settings.settings import Settings
from lib.runner.execute.instance.instance import Instance
from lib.utils.display.open_display import open_display
from lib.utils.excel.get_excel_data import get_excel_data
from lib.utils.json_dict.load_headers import load_headers
from lib.utils.kill.kill_driver import kill_driver
from lib.utils.path.get_path import get_payload_path, get_screenshot_path
from lib.utils.sleep.time_sleep import time_sleep
from lib.utils.verify.verify_path_exists import verify_path_exists

instance = Instance()


# Classe de abstração das ações utilizadas nos testes
class Interact:
    # Função principal com validação da plataforma configurada no arquivo settings.json e chamada da instância
    def __init__(self):
        if Settings.platform == "firefox":
            instance.firefox_driver()
        elif Settings.platform == "chrome":
            instance.chrome_driver()
        elif Settings.platform == "edge":
            instance.edge_driver()
        elif Settings.platform == "desktop":
            instance.winium_driver()
        elif Settings.platform == "mobile":
            instance.appium_driver()
        elif Settings.platform == "api":
            pass
        else:
            raise Exception('Plataforma de execução de testes selecionada não suportada pela aplicação!')

    # Método estático que realiza o setup com ou sem interface gráfica na plataforma instanciada
    @staticmethod
    def setup():
        if Settings.headless is False:
            Interact()
            time_sleep(3)
        elif Settings.headless:
            if Settings.platform in ("firefox", "chrome", "edge"):
                open_display()
                Interact()
                time_sleep(3)
            else:
                Interact()
                time_sleep(3)

    # Método estático que realiza o teardown e mata os processos do driver na plataforma configurada
    @staticmethod
    def teardown():
        if Settings.platform in ("firefox", "chrome", "edge", "desktop"):
            try:
                Interact.close_browser()
            except WebDriverException:
                pass
            kill_driver()
        elif Settings.platform == "mobile":
            Interact.close_application()

    # Método estático que realiza a abertura de uma URL no navegador Web
    @staticmethod
    def open_url(url):
        instance.driver.get(url)

    # Método estático que realiza a abertura de um aplicativo Android ou iOS no aparelho mobile ou emulador
    @staticmethod
    def lunch_app():
        instance.driver.lunch_app()

    # Método estático que simula a realização de um click em um elemento Web, Mobile ou Desktop
    @staticmethod
    def click(selector, element):
        def click_by_css_selector():
            instance.driver.find_element_by_css_selector(element).click()

        def click_by_xpath():
            instance.driver.find_element_by_xpath(element).click()

        def click_by_id():
            instance.driver.find_element_by_id(element).click()

        def click_by_class_name():
            instance.driver.find_element_by_class_name(element).click()

        def click_by_name():
            instance.driver.find_element_by_name(element).click()

        try:
            if selector == 'css':
                click_by_css_selector()
            elif selector == 'xpath':
                click_by_xpath()
            elif selector == 'id':
                click_by_id()
            elif selector == 'class':
                click_by_class_name()
            elif selector == 'name':
                click_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que simula a realização de um envio de texto para um elemento de input  Web, Mobile ou Desktop
    @staticmethod
    def send_keys(selector, element, value):
        def send_keys_by_css_selector():
            instance.driver.find_element_by_css_selector(element).send_keys(value)

        def send_keys_by_xpath():
            instance.driver.find_element_by_xpath(element).send_keys(value)

        def send_keys_by_id():
            instance.driver.find_element_by_id(element).send_keys(value)

        def send_keys_by_class_name():
            instance.driver.find_element_by_class_name(element).send_keys(value)

        def send_keys_by_name():
            instance.driver.find_element_by_name(element).send_keys(value)

        try:
            if selector == 'css':
                send_keys_by_css_selector()
            elif selector == 'xpath':
                send_keys_by_xpath()
            elif selector == 'id':
                send_keys_by_id()
            elif selector == 'class':
                send_keys_by_class_name()
            elif selector == 'name':
                send_keys_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que simula a realização de um duplo click em um elemento Web, Mobile ou Desktop
    @staticmethod
    def double_click(selector, element):
        action = ActionChains(instance.driver)

        def double_click_by_css_selector():
            action.double_click(instance.driver.find_element_by_css_selector(element))

        def double_click_by_xpath():
            action.double_click(instance.driver.find_element_by_xpath(element))

        def double_click_by_id():
            action.double_click(instance.driver.find_element_by_id(element))

        def double_click_by_class_name():
            action.double_click(instance.driver.find_element_by_class_name(element))

        def double_click_by_name():
            action.double_click(instance.driver.find_element_by_name(element))

        try:
            if selector == 'css':
                double_click_by_css_selector()
            elif selector == 'xpath':
                double_click_by_xpath()
            elif selector == 'id':
                double_click_by_id()
            elif selector == 'class':
                double_click_by_class_name()
            elif selector == 'name':
                double_click_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.perform()
        action.reset_actions()

    # Método estático que realiza a espera de visibilidade de um elemento Web, Mobile ou Desktop
    @staticmethod
    def wait_visible_element(selector, time_wait, element):
        def wait_visible_element_by_css_selector():
            WebDriverWait(instance.driver, time_wait).until(
                ec.visibility_of_element_located((By.CSS_SELECTOR, element)))

        def wait_visible_element_by_xpath():
            WebDriverWait(instance.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.XPATH, str(element))))

        def wait_visible_element_by_id():
            WebDriverWait(instance.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.ID, str(element))))

        def wait_visible_element_by_class_name():
            WebDriverWait(instance.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.CLASS_NAME, str(element))))

        def wait_visible_element_by_name():
            WebDriverWait(instance.driver, float(time_wait)).until(
                ec.visibility_of_element_located((By.NAME, str(element))))

        try:
            if selector == 'css':
                wait_visible_element_by_css_selector()
            elif selector == 'xpath':
                wait_visible_element_by_xpath()
            elif selector == 'id':
                wait_visible_element_by_id()
            elif selector == 'class':
                wait_visible_element_by_class_name()
            elif selector == 'name':
                wait_visible_element_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza a espera de presença de um elemento Web, Mobile ou Desktop
    @staticmethod
    def wait_presence_element(selector, time_wait, element):
        def wait_presence_element_by_css_selector():
            WebDriverWait(instance.driver, time_wait).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, element)))

        def wait_presence_element_by_xpath():
            WebDriverWait(instance.driver, time_wait).until(
                ec.presence_of_element_located((By.XPATH, element)))

        def wait_presence_element_by_id():
            WebDriverWait(instance.driver, time_wait).until(
                ec.presence_of_element_located((By.ID, element)))

        def wait_presence_element_by_class_name():
            WebDriverWait(instance.driver, time_wait).until(
                ec.presence_of_element_located((By.CLASS_NAME, element)))

        def wait_presence_element_by_name():
            WebDriverWait(instance.driver, time_wait).until(
                ec.presence_of_element_located((By.NAME, element)))

        try:
            if selector == 'css':
                wait_presence_element_by_css_selector()
            elif selector == 'xpath':
                wait_presence_element_by_xpath()
            elif selector == 'id':
                wait_presence_element_by_id()
            elif selector == 'class':
                wait_presence_element_by_class_name()
            elif selector == 'name':
                wait_presence_element_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza a espera de não presença de um elemento Web, Mobile ou Desktop
    @staticmethod
    def wait_element_not_present(selector, time_wait, element):
        def wait_element_not_present_by_css_selector():
            WebDriverWait(instance.driver, time_wait).until(
                ec.invisibility_of_element_located((By.CSS_SELECTOR, element)))

        def wait_element_not_present_by_xpath():
            WebDriverWait(instance.driver, time_wait).until(
                ec.invisibility_of_element_located((By.XPATH, element)))

        def wait_element_not_present_by_id():
            WebDriverWait(instance.driver, time_wait).until(
                ec.invisibility_of_element_located((By.ID, element)))

        def wait_element_not_present_by_class_name():
            WebDriverWait(instance.driver, time_wait).until(
                ec.invisibility_of_element_located((By.CLASS_NAME, element)))

        def wait_element_not_present_by_name():
            WebDriverWait(instance.driver, time_wait).until(
                ec.invisibility_of_element_located((By.NAME, element)))

        try:
            if selector == 'css':
                wait_element_not_present_by_css_selector()
            elif selector == 'xpath':
                wait_element_not_present_by_xpath()
            elif selector == 'id':
                wait_element_not_present_by_id()
            elif selector == 'class':
                wait_element_not_present_by_class_name()
            elif selector == 'name':
                wait_element_not_present_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza a captura de texto de um elemento Web, Mobile ou Desktop
    @staticmethod
    def get_text(selector, element):
        def get_text_by_css_selector():
            return instance.driver.find_element_by_css_selector(element).text

        def get_text_by_xpath():
            return instance.driver.find_element_by_xpath(element).text

        def get_text_by_id():
            return instance.driver.find_element_by_id(element).text

        def get_text_by_class_name():
            return instance.driver.find_element_by_class_name(element).text

        def get_text_by_name():
            return instance.driver.find_element_by_name(element).text

        try:
            if selector == 'css':
                get_text_by_css_selector()
            elif selector == 'xpath':
                get_text_by_xpath()
            elif selector == 'id':
                get_text_by_id()
            elif selector == 'class':
                get_text_by_class_name()
            elif selector == 'name':
                get_text_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza a limpeza de um elemento de texto Web, Mobile ou Desktop
    @staticmethod
    def clear_text(selector, element):
        def clear_text_by_css_selector():
            instance.driver.find_element_by_css_selector(element).clear()

        def clear_text_by_xpath():
            instance.driver.find_element_by_xpath(element).clear()

        def clear_text_by_id():
            instance.driver.find_element_by_id(element).clear()

        def clear_text_by_class_name():
            instance.driver.find_element_by_class_name(element).clear()

        def clear_text_by_name():
            instance.driver.find_element_by_name(element).clear()

        try:
            if selector == 'css':
                clear_text_by_css_selector()
            elif selector == 'xpath':
                clear_text_by_xpath()
            elif selector == 'id':
                clear_text_by_id()
            elif selector == 'class':
                clear_text_by_class_name()
            elif selector == 'name':
                clear_text_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza o posicionamento do ponteiro do mouse em cima de um elemento Web, Mobile ou Desktop
    @staticmethod
    def mouse_over(selector, element):
        action = ActionChains(instance.driver)

        def mouse_over_by_css_selector():
            action.move_to_element(instance.driver.find_element_by_css_selector(element)).perform()

        def mouse_over_by_xpath():
            action.move_to_element(instance.driver.find_element_by_xpath(element)).perform()

        def mouse_over_by_id():
            action.move_to_element(instance.driver.find_element_by_id(element)).perform()

        def mouse_over_by_class_name():
            action.move_to_element(instance.driver.find_element_by_class_name(element)).perform()

        def mouse_over_by_name():
            action.move_to_element(instance.driver.find_element_by_name(element)).perform()

        try:
            if selector == 'css':
                mouse_over_by_css_selector()
            elif selector == 'xpath':
                mouse_over_by_xpath()
            elif selector == 'id':
                mouse_over_by_id()
            elif selector == 'class':
                mouse_over_by_class_name()
            elif selector == 'name':
                mouse_over_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.reset_actions()

    # Método estático que realiza a captura de um atributo em um elemento Web
    @staticmethod
    def get_attribute(selector, element, attribute):
        def get_attribute_by_css_selector():
            return instance.driver.find_element_by_css_selector(element).get_attribute(attribute)

        def get_attribute_by_xpath():
            return instance.driver.find_element_by_xpath(element).get_attribute(attribute)

        def get_attribute_by_id():
            return instance.driver.find_element_by_id(element).get_attribute(attribute)

        def get_attribute_by_class_name():
            return instance.driver.find_element_by_class_name(element).get_attribute(attribute)

        def get_attribute_by_name():
            return instance.driver.find_element_by_name(element).get_attribute(attribute)

        try:
            if selector == 'css':
                get_attribute_by_css_selector()
            elif selector == 'xpath':
                get_attribute_by_xpath()
            elif selector == 'id':
                get_attribute_by_id()
            elif selector == 'class':
                get_attribute_by_class_name()
            elif selector == 'name':
                get_attribute_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

    # Método estático que realiza a simulação de um touch click em um elemento Mobile
    @staticmethod
    def tap(selector, element):
        action = TouchAction(instance.driver)

        def tap_by_css_selector():
            action.tap(instance.driver.find_element_by_css_selector(element))

        def tap_by_xpath():
            action.tap(instance.driver.find_element_by_xpath(element))

        def tap_by_id():
            action.tap(instance.driver.find_element_by_id(element))

        def tap_by_class_name():
            action.tap(instance.driver.find_element_by_class_name(element))

        def tap_by_name():
            action.tap(instance.driver.find_element_by_name(element))

        try:
            if selector == 'css':
                tap_by_css_selector()
            elif selector == 'xpath':
                tap_by_xpath()
            elif selector == 'id':
                tap_by_id()
            elif selector == 'class':
                tap_by_class_name()
            elif selector == 'name':
                tap_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.perform()

    # Método estático que realiza a simulação de um double touch click em um elemento Mobile
    @staticmethod
    def double_tap(selector, element):
        action = TouchAction(instance.driver)

        def double_tap_by_css_selector():
            action.tap(instance.driver.find_element_by_css_selector(element), count=2)

        def double_tap_by_xpath():
            action.tap(instance.driver.find_element_by_xpath(element), count=2)

        def double_tap_by_id():
            action.tap(instance.driver.find_element_by_id(element), count=2)

        def double_tap_by_class_name():
            action.tap(instance.driver.find_element_by_class_name(element), count=2)

        def double_tap_by_name():
            action.tap(instance.driver.find_element_by_name(element), count=2)

        try:
            if selector == 'css':
                double_tap_by_css_selector()
            elif selector == 'xpath':
                double_tap_by_xpath()
            elif selector == 'id':
                double_tap_by_id()
            elif selector == 'class':
                double_tap_by_class_name()
            elif selector == 'name':
                double_tap_by_name()
        except NoSuchElementException:
            raise NoSuchElementException("Element not found!")
        except WebDriverException:
            raise WebDriverException("Element not found!")
        except ElementNotInteractableException:
            raise ElementNotInteractableException("Element not found!")

        action.perform()

    # Método estático que realiza uma pausa na execução do código nos segundos passados
    @staticmethod
    def delay(wait_time):
        time_sleep(wait_time)

    # Método estático que realiza uma espera implícita de algum carregamento na aplicação nos segundos passados
    @staticmethod
    def implicity_wait(wait_time):
        instance.driver.implicitly_wait(wait_time)

    # Método estático que realiza a simulação de um pressionamento no botão de volta do aparelho Mobile
    @staticmethod
    def press_back():
        instance.driver.back()

    # Método estático que realiza a execução de um comando JavaScript na página Web
    @staticmethod
    def execute_javascript(script):
        instance.driver.execute_script(script=script)

    # Método estático que realiza um refresh na página Web
    @staticmethod
    def refresh():
        instance.driver.refresh()

    # Método estático que captura a URL de uma pagina Web
    @staticmethod
    def get_url():
        return instance.driver.current_url()

    # Método estático que captura o título de uma página Web
    @staticmethod
    def get_title():
        return instance.driver.title

    # Método estático que realiza uma captura de tela
    @staticmethod
    def get_screenshot():
        instance.driver.save_screenshot(get_screenshot_path())

    # Método estático que realiza a instalação de um aplicativo no aparelho Mobile
    @staticmethod
    def install_app(app_path):
        instance.driver.install_app(app_path)

    # Método estático que realiza o fechamento de um navegador Web
    @staticmethod
    def close_browser():
        instance.driver.close()

    # Métido estático que realiza o fechamento de uma aplicação Mobile
    @staticmethod
    def close_application():
        instance.driver.close_app()

    # Método estático que verifica a existência de um diretório ou arquivo no S.O
    @staticmethod
    def check_path_exists(path):
        return verify_path_exists(path)

    # Método estático que realiza a captura de dados na planilha em um arquivo excel
    @staticmethod
    def get_excel_value(path, sheet, row, column):
        return get_excel_data(path, sheet, row, column)

    # Método estático que realiza a abertura de uma sessão no PyPac para envio de requisições autenticadas
    @staticmethod
    def open_session():
        session = PACSession()
        user, password = load_authentication()
        session.auth = HTTPBasicAuth(user, password)
        return session

    # Método estático que realiza o envio de uma requisição GET por meio do PyPac
    @staticmethod
    def send_get(mock, session, text, url, payload):
        return instance.pypac_request(mock, session, text, 'GET', url, load_headers(), payload)

    # Método estático que realiza o envio de uma requisição POST por meio do PyPac
    @staticmethod
    def send_post(mock, session, text, url, payload):
        return instance.pypac_request(mock, session, text, 'POST', url, load_headers(), payload)

    # Método estático que realiza o envio de uma requisição PUT por meio do PyPac
    @staticmethod
    def send_put(mock, session, text, url, payload):
        return instance.pypac_request(mock, session, text, 'PUT', url, load_headers(), payload)

    # Método estático que realiza o envio de uma requisição DELETE por meio do PyPac
    @staticmethod
    def send_delete(mock, session, text, url, payload):
        return instance.pypac_request(mock, session, text, 'DELETE', url, load_headers(), payload)

    # Método estático que retorna a URL e payload por tags para preenchimento dos dados das requisições
    @staticmethod
    def load_request_data(tag, payload):
        return load_data(tag, payload)

    # Método estático que chama a função de start do allure
    @staticmethod
    def start_allure_serve():
        open_serve()

    # Método estático que chama a função de stop do allure
    @staticmethod
    def stop_allure_serve():
        stop_serve()
