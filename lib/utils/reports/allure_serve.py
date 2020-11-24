import os

from lib.utils.os.get_operational_system import get_operational_system
from lib.utils.path.get_path import get_allure_path, get_reports_path
from lib.utils.sleep.time_sleep import time_sleep


# Função que inicia Allure Serve na pasta de logs do Allure
def open_serve():
    time_sleep(2)
    os.popen(get_allure_path() + ' serve -h localhost -p 80 ' + get_reports_path("allure"))


# Função que encerra o processo do Allure Serve
def stop_serve():
    try:
        if get_operational_system() == "Linux":
            pid = os.popen('pgrep -x java').read()
            if pid is None or pid == '':
                os.popen('pkill -f "java"')
        elif get_operational_system() == "Windows":
            pid = os.popen('tasklist | find /i "java.exe"').read()
            if pid is None or pid == '':
                os.popen('taskkill /f /im java.exe')
    except Exception as e:
        print(e)
