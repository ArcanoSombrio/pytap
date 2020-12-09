from requests import HTTPError


ok_200 = '200 - O recurso solicitado foi processado e retornado com sucesso.'
created_201 = '201 - O recurso informado foi criado com sucesso.'
no_content_204 = '204 - O recurso solicitado não necessita de redirecionamento. Serão utilizados os dados em cache.'
moved_permanently_301 = '301 - O recurso solicitado foi movido permanentemente.'
not_modified_304 = '304 - O recurso solicitado não foi modificado. Serão utilizados os dados em cache.'
temporary_redirect_307 = '307 - O recurso solicitado foi movido temporáriamente.'
bad_request_400 = '400 - Não foi possível interpretar a requisição. Verifique a sintaxe das informações enviadas.'
unauthorized_401 = '401 - A chave da API está desativada, incorreta ou não foi informada corretamente.'
forbidden_403 = '403 - O acesso ao recurso não foi autorizado.'
not_found_404 = '404 - O recurso solicitado ou o endpoint não foi encontrado.'
not_acceptable_406 = '406 - O formato enviado não é aceito.'
unprocessable_entity_422 = '422 - A requisição foi recebida com sucesso, porém contém parâmetros inválidos.'
too_many_requests_429 = '429 - O limite de requisições foi atingido.'
internal_server_error_500 = '500 - Ocorreu uma falha na plataforma.'
service_unavailable_503 = '503 - Serviço fora do ar, em manutenção ou sobrecarregado.'


# Função que valida o status code de retorno das requisições em API
def validate_status_code(status_code):
    if status_code == 200:
        return ok_200
    elif status_code == 201:
        return created_201
    elif status_code == 204:
        return no_content_204
    elif status_code == 301:
        return moved_permanently_301
    elif status_code == 304:
        return not_modified_304
    elif status_code == 307:
        return temporary_redirect_307
    elif status_code == 400:
        raise HTTPError(bad_request_400)
    elif status_code == 401:
        raise HTTPError(unauthorized_401)
    elif status_code == 403:
        raise HTTPError(forbidden_403)
    elif status_code == 404:
        raise HTTPError(not_found_404)
    elif status_code == 406:
        raise HTTPError(not_acceptable_406)
    elif status_code == 422:
        raise HTTPError(unprocessable_entity_422)
    elif status_code == 429:
        raise HTTPError(too_many_requests_429)
    elif status_code == 500:
        raise HTTPError(internal_server_error_500)
    elif status_code == 503:
        raise HTTPError(service_unavailable_503)
    else:
        raise HTTPError(status_code)
