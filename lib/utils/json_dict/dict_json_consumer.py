import json


# Função que converte um JSON em dicionário do Python
def json_to_dict(json_file):
    return dict(json.dumps(json_file, indent=0))


# Função que converte um dicionário do Python em JSON
def dict_to_json(dictionary):
    return json.dumps(dictionary, indent=0)


# Função que captura o valor de uma chave em um dicionário Python ou JSON
def get_value_from_key(obj, key):
    return obj[key].value()


# Função que conta a quantidade de valores de uma chave em um dicionário Python ou JSON
def get_len_from_key(obj, key):
    return obj[key].len()


# Função que carrega os dados de um arquivo JSON
def load_json_file(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)
