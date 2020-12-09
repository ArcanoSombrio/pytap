from lib.utils.json_dict.dict_json_consumer import load_json_file
from lib.utils.path.get_path import get_payload_path


# Função que carrega os dados de URL e payload pela tag do arquivo de payload no formato JSON
def load_data(tag, file):
    data = load_json_file(get_payload_path(file))
    url = data[tag]["url"]
    payload = data[tag]["payload"]
    return url, payload
