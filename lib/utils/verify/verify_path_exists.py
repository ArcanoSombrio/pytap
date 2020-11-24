import os


# Função que realiza uma verificação de existência de um arquivo ou pasta no S.O
def verify_path_exists(path):
    return os.path.isfile(path)
