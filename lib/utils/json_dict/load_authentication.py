from lib.utils.json_dict.dict_json_consumer import load_json_file
from lib.utils.path.get_path import get_authentication_path


# Função que carrega os dados de autenticação das requisições no arquivo authentication.json
def load_authentication():
    authentication = load_json_file(get_authentication_path())
    user = authentication["authentication"]["user"]
    password = authentication["authentication"]["password"]
    return user, password
