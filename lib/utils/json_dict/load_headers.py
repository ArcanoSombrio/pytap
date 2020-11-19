from structure.lib.utils.json_dict.dict_json_consumer import load_json_file
from structure.lib.utils.path.get_path import get_headers_path


# Função que carrega dos dados de headers da requisição no arquivo headers.json
def load_headers():
    headers = load_json_file(get_headers_path())
    return headers["headers"]
