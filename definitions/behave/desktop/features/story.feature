# language:pt
# file: story.feature
# -- FILE: structure\definitions\behave\web\features\steps\first_test.py

Funcionalidade: Pesquisa no Google
  @tag
  Cenário: Envio de texto no campo de busca do Google
    Dado que eu acesse a calculadora do Windows
    Quando eu clicar em 1
      E clicar em +
      E clicar em 7
      E clicar em =
    Então a soma é realizada
