# language:pt
# file: story.feature
# -- FILE: structure\definitions\behave\api\features\steps\first_test.py

Funcionalidade: Requisição
  @tag
  Cenário: Envio de requisição GET e resposta do servidor em JSON
    Dado que eu envio uma requisição GET para o endereço
    Então eu recebo o retorno da requisição
