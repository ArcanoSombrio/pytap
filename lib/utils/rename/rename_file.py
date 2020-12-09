import os

from lib.utils.os.get_operational_system import get_operational_system


# Função utilizada para renomear um arquivo de acordo com o S.O
def rename_file(path, file, new_file):
    if get_operational_system() == "Linux":
        os.popen('cd ' + path + ' && mv ' + file + ' ' + new_file)
    elif get_operational_system() == "Windows":
        os.popen('cd ' + path + ' && rename ' + file + ' ' + new_file)
