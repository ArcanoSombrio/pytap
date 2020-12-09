# language:pt
# file: story.feature
# -- FILE: structure\definitions\behave\mobile\features\steps\first_test.py

Funcionalidade: Teste no relógio do Android
  @tag
  Cenário: Teste de mudança de aba no relógio
    Dado que eu acesse o aplicativo Clock no Android
    Quando eu clicar em Alarm
      E clicar em Timer
    Então as abas são trocadas
