# language:pt
# file: story.feature
# -- FILE: structure\definitions\behave\web\features\steps\first_test.py

Funcionalidade: Pesquisa no Google
  @tag
  Cenário: Envio de texto no campo de busca do Google
    Dado que eu acesso a página do Google
    Quando eu digitar o texto no campo de pesquisa
      E teclar ENTER ou clicar em Pesquisa Google
    Então a pesquisa é realizada
