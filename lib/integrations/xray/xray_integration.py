from json.decoder import JSONDecodeError
from pypac import PACSession
from requests.auth import HTTPBasicAuth

from lib.utils.validate.validate_status_code import validate_status_code


def send_tests_results_to_xray(url, payload):
    session = PACSession()
    user, password = "daniel", "pass"
    session.auth = HTTPBasicAuth(user, password)

    request = session.request(
        method='POST',
        url=url+'/rest/raven/1.0/import/execution/behave',
        headers={
            'Content-Type': 'application/json'
        },
        data=payload
    )
    status_code = request.status_code
    validate_status_code(status_code)
    try:
        response = request.json()
    except JSONDecodeError:
        response = {}

    print(response)
