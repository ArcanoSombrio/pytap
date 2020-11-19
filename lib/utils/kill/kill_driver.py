import os

from structure.lib.utils.os.get_operational_system import get_operational_system
from structure.lib.utils.settings.settings import Settings


# Função que mata (encerra) o processo do driver do selenium no S.O corrente
def kill_driver():
    def kill_linux():
        if Settings.platform == "firefox":
            os.popen('killall geckodriver')
        elif Settings.platform == "chrome":
            os.popen('killall chromedriver')

    def kill_windows():
        if Settings.platform == "firefox":
            os.popen('tskill geckodriver*')
        elif Settings.platform == "chrome":
            os.popen('tskill chromedriver*')
        elif Settings.platform == "desktop":
            os.popen('tskill Winium*')
        elif Settings.platform == "edge":
            os.popen('tskill msdriver*')

    if get_operational_system() == "Linux":
        kill_linux()
    elif get_operational_system() == "Windows":
        kill_windows()
