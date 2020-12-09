import os

from lib.utils.os.get_operational_system import get_operational_system
from lib.utils.settings.settings import Settings


# Função que mata (encerra) o processo do driver do selenium no S.O corrente
def kill_driver():
    def kill_linux():
        if Settings.platform == "firefox":
            pid = os.popen('pgrep -x geckodriver').read()
            if pid is not None or pid != '':
                os.popen('pkill -f "geckodriver"')
        elif Settings.platform == "chrome":
            pid = os.popen('pgrep -x chromedriver').read()
            if pid is not None or pid != '':
                os.popen('pkill -f "chromedriver"')
        elif Settings.platform == "opera":
            pid = os.popen('pgrep -x operadriver').read()
            if pid is not None or pid != '':
                os.popen('pkill -f "operadriver"')

    def kill_windows():
        if Settings.platform == "firefox":
            pid = os.popen('tasklist | find /i "geckodriver.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im geckodriver.exe')
        elif Settings.platform == "chrome":
            pid = os.popen('tasklist | find /i "chromedriver.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im chromedriver.exe')
        elif Settings.platform == "desktop":
            pid = os.popen('tasklist | find /i "Winium.Desktop.Driver.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im Winium.Desktop.Driver.exe')
        elif Settings.platform == "edge":
            pid = os.popen('tasklist | find /i "MicrosoftWebDriver.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im MicrosoftWebDriver.exe')
        elif Settings.platform == "ie":
            pid = os.popen('tasklist | find /i "IEDriverServer.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im IEDriverServer.exe')
        elif Settings.platform == "opera":
            pid = os.popen('tasklist | find /i "operadriver.exe"').read()
            if pid is not None or pid != '':
                os.popen('taskkill /f /im operadriver.exe')

    if get_operational_system() == "Linux":
        kill_linux()
    elif get_operational_system() == "Windows":
        kill_windows()
