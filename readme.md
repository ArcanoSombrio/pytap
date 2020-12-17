# PYTAP - Python Test Automation Platform

    Esta platafoma foi construída com o foco de centralizar as bibliotecas de automação para os seguintes níveis:
        - Testes funcionais
        - Testes de aceitação
        - Testes de regressão
        - Testes integrados


## Tecnologias utilizadas
    Linguagem utilizada:
        - Python versão 3.8.5

    Frameworks utilizados:
        - behave
        - pytest
        - allure-behave
        - allure-pytest
        - pytest-json
        - pytest-cov
        - Appium-Python-Client
        - selenium
        - PyVirtualDisplay
        - behave_restful
        - pypac
        - requests_mock
        - PyHamcrest
        - xlrd
        - pylint
        - requests
        - Algumas libs Built-in do Python


### Disposição das funcionalidades

    Plataformas suportadas:
        - Aplicações Web (Browsers suportados: Firefox, Chrome, Edge, Internet Explorer e Opera)
        - Aplicações Mobile (S.O's suportados: Android e iOS)
        - Service API
        - Desktop Windows

    Funcionalidades:
        - Execução de testes de frontend em Firefox, Chrome, Edge, Internet Explorer e Opera por meio do Selenium
        - Execução de testes de API por meio do PyPac
        - Execução de testes Desktop com Winium (Implementação do Selenium para aplicações nativas do Windows)
        - Execução de testes Mobile em Android ou iOS com Appium
        - Execução de testes sem interface gráfica com PyVirtualDisplay
        - Execução de testes com BDD utilizando Behave
        - Execução de testes com Pytest
        - Reports com Allure
        - Resports em JSON
        - Suporte a integração com Jira X-Ray
        - Suporte a integração com Silk
        - Dockerfile para instalar dependências da plataforma em containers para execução de CI
        - Captura de dados a partir de arquivos excel para DDT
        - Captura de tela em erros na execução dos testes Web e Desktop

---
## Mapeamento de diretórios e arquivos do projeto

 - OBS: os arquivos que começarem com o nome "xxxxx" + ".extensão" podem ser renomeados da maneira que preferir.

### Definição da estrutura de testes

    Diretórios de definição dos testes:
        - definitions (Diretório onde são definidos os testes, ou seja, o passo a passo e iterações com as aplicações)
            - behave (Diretório onde são escritos os testes no modelo BDD)
                - api (Diretório dos testes de API's)
                    - features (Diretório onde são definitos os testes e cenários do BDD)
                        - steps (Diretório onde se situam as classes de testes relacionadas as histórias)
                        - environment.py (Gatilhos do BDD utilizado para executar ações antes e depois dos testes)
                        - xxxxx.feature (Arquivo que descreve o as histórias contendo o cenário de teste do BDD)
                    - page (Diretório onde são definidos os JSON com dados de autenticação, headers e payload)
                        - payload (Diretórios onde se situam as payloads em JSON com padrão de tags)
                            - xxxxx.json (Arquivo com a url e payload divididas por tags e enviadas nas requisições)
                        - authentication.json (Arquivo JSON onde se situa o usuário e senha para autenticação)
                        - headers.json (Arquivo JSON onde se situa os headers enviados nas requisições)
                - * desktop, mobile e web (Diretórios dos testes Desktop, Mobile e Web [Firefox, Chrome e Edge])
                    - features (Diretório onde são definitos os testes e cenários do BDD)
                        - steps (Diretório onde se situam as classes de testes relacionadas as histórias)
                        - environment.py (Gatilhos do BDD utilizado para executar ações antes e depois dos testes)
                        - xxxxx.feature (Arquivo que descreve o as histórias contendo o cenário de teste do BDD)
                    - page (Diretório onde são definidas as páginas web e a base com base no padrão Page Objects)
                        - xxxxx (Diretório onde ficam as classes das páginas relacionadas aos módulos da aplicação)
                            - xxxxx.py (Classe onde se situa o código da página ou módulo da aplicação)
                        - page.py (Classe da página que será herdada por outras que contém os mesmos atributos)
                        
            - pytest (Diretório onde são escritos os testes no modelo do Pytest)
                - api (Diretório dos testes de API's)
                    - tests (Diretório onde são definitos os testes)
                        - steps (Diretório onde se situam as classes de testes)
                        - conftest.py (Gatilhos do Pytest utilizado para executar ações antes e depois dos testes)
                    - page (Diretório onde são definidos os JSON com dados de autenticação, headers e payload)
                        - payload (Diretórios onde se situam as payloads em JSON com padrão de tags)
                            - xxxxx.json (Arquivo com a url e payload divididas por tags e enviadas nas requisições)
                        - authentication.json (Arquivo JSON onde se situa o usuário e senha para autenticação)
                        - headers.json (Arquivo JSON onde se situa os headers enviados nas requisições)
                - * desktop, mobile e web (Diretórios dos testes Desktop, Mobile e Web [Firefox, Chrome e Edge])
                    - tests (Diretório onde são definitos os testes)
                        - steps (Diretório onde se situam as classes de testes)
                        - conftest.py (Gatilhos do Pytest utilizado para executar ações antes e depois dos testes)
                    - page (Diretório onde são definidas as páginas web e a base com base no padrão Page Objects)
                        - xxxxx (Diretório onde ficam as classes das páginas relacionadas aos módulos da aplicação)
                            - xxxxx.py (Classe onde se situa o código da página ou módulo da aplicação)
                        - page.py (Classe da página que será herdada por outras que contém os mesmos atributos)
                        
                        
    * A estrutura de diretórios dos testes Desktop, Mobile e Web são a mesma, o que os diferencia são os os testes implementados e os objetos mapeados na base.
        

### Definição das configurações de execução dos testes

    Diretório de definição das configurações:
        - settings (Diretório onde se encontra o arquivo JSON de configuração da execução dos testes)
            - settings.json (Arquivo JSON de configuração da execução da automação)


### Definição de reports das execuções

    Diretório dos reports das execuções dos testes:
        - reports (Diretório onde se encontram os arquivos de reports das execuções e captura de erros em imagens)
            - allure (Diretório onde se encontram os reports gerados para visualização com Allure)
                - xxxxx.json (Arquivo JSON de report no padrão do allure preparado para leitura e visualização)
            - json (Diretório onde se encontram os reports gerados em JSON para envio ao X-Ray)
                - DD-MM-YYYY_hh_mm_ss_test_result.json (Arquivo JSON de report no padrão que o X-Ray recebe via REST)
            - screenshot (Diretório onde se encontram as capturas de telas geradas em erros na execução dos testes)
                - DD-MM-YYYY_hh_mm_ss_screenshot.png (Captura de tela com o padrão de data e hora da captura no nome)


### Definição dos arquivos na raiz do projeto

    Diretório raiz da aplicação:
        - main.py (Classe onde são passados os testes que serão executados, onde se inicia todo o processo de execução)
        - .gitignore (Arquivo de configuração com diretórios e arquivos que não subiram para o servidor do Git)
        - requirements.txt (Arquivo de dependências do projeto, onde é realizada injeção de dependências)


### Definição da biblioteca de execução

    Diretório da biblioteca de execução:
        - lib (Diretório com estrutura de bibliotecas implementadas para execução dos testes com base na configuração)
            - integrations (Diretório onde se encontram as implementações de integração com Jira X-Ray e CI)
                - ci (Diretório onde se encontra o Dockerfile para execução do Sonarqube e levantamento de dependência)
                - xray (Diretório onde se encontra o arquivo de classe que faz o envio das execuções para o X-Ray)
            - runner (Diretório com implementação das bibliotecas e abstração das funções de teste)
                - drivers (Diretório onde se encontram os drivers do Selenium para cada navegador web suportado)
                    - chromedriver (Diretório onde se encontra o executável Windows e Linux do driver para Chrome)
                        - chromedriver.exe (Executável Windows do driver do Selenium para Chrome)
                        - chromedriver (Executável Linux do driver do Selenium para Chrome)
                    - geckodriver (Diretório onde se encontra o executável Windows e Linux do driver para Firefox)
                        - geckodriver.exe (Executável Windows do driver do Selenium para Firefox)
                        - geckodriver (Executável Linux do driver do Selenium para Firefox)
                    - iedriver (Diretório onde se encontra o executável Windows do driver para Internet Explorer)
                        - IEDriverServer.exe ((Executável Windows do driver do Selenium para Internet Explorer)
                    - msdriver (Diretório onde se encontra o executável Windows do driver para Edge)
                        - MicrosoftWebDriver.exe (Executável Windows do driver do Selenium para Edge)
                    - operadriver (Diretório onde se encontra o executável Windows e Linux do driver para Opera)
                        - operadriver.exe (Executável Windows do driver do Selenium para Opera)
                        - operadriver (Executável Linux do driver do Selenium para Opera)
                    - winiumdriver (Diretório onde se encontra o executável Windows do driver para Desktop Application)
                        - Winium.Desktop.Driver.exe (Executável Windows do driver do Selenium para Desktop Application)
                - execute (Diretório onde se encontram as implementações e abstrações das funções de testes)
                    - execute (Diretório onde se encontra o arquivo de classe com a abstração da execução dos testes)
                        - execute.py (Classe com implentação das execuções dos testes com base nas configurações)
                    - instance (Diretório onde se encontra o arquivo de classe da instância com base na configuração)
                        - instance.py (Classe com instância dos drivers do Selenium e requisição do PyPac)
                    - interact (Diretório onde se encontra o arquivo de classe com a abastração das funções dos testes)
                        - interact.py (Classe com abstração das funções do Selenium e do Pypac + algumas funções úteis)
            - tools (Diretório com executáveis do Allure para início automático de report pós execução dos testes)
                - allure (Diretório com estrutura dos executáveis do Allure para Linux e Windows)
            - utils (Diretório com funções utilizadas no processo de testes e instância das plataformas)
                - date (Diretório com implementação de função para capturar data e hora atual)
                    - get_date_time_now.py (Arquivo de classe com implementação da função de captura da data e hora)
                - display (Diretório com implementação de função para abrir um virtual display)
                    - open_display.py (Arquivo de classe com implementação da função de abertura de display virtual)
                - excel (Diretório com implementação de função para captura de dados de planilhas excel)
                    - get_excel_data.py (Arquivo de classe com implementação da função de captura de dados excel)
                - json_dict (Diretório com implementação de funções de carregamento do JSON e conversão para dict)
                    - dict_json_consumer.py (Arquivo de classe com implementação de funções para consumo de JSON e dict)
                    - get_settings.py (Arquivo de classe com implementação de função para carregamento do settings.json)
                    - load_authentication.py (Arquivo de classe com implementação da função de carregamento dos dados de autenticação das requisições)
                    - load_data.py (Arquivo de classe com implementação da função de carregamento da url e payload das requisições com base na tag)
                    - load_headers.py (Arquivo de classe com implementação da função de carregamento dos headers das requisições)
                - kill (Diretório com implementação de função para matar o processo do driver do Selenium no S.O)
                    - kill_driver.py (Arquivo de classe com implementação da função para matar o proceso do driver)
                - os (Diretório com implementação de função para captura do sistema operacional corrente)
                    - get_operational_system.py (Arquivo de classe com implementação da função para identificação do S.O corrente)
                - path (Diretório com implementação de funções para captura de diretórios utilizados no projeto)
                    - get_path (Arquivo de classe com implementação da função para captura dos diretórios)
                - rename (Diretório com implementação de função de troca no nome de arquivos)
                    - rename_file.py (Arquivo de classe com implementação de função para troca de nome de arquivos)
                - reports (Diretório com implementação de funções para start e stop do Allure pós execução dos testes)
                    - allure_serve.py (Arquivo de classe com implementação das funções de start e stop do Allure)
                - settings (Diretório com a classe onde são salvas as configurações do arquivo settings.json)
                    - settings.py (Classe onde são salvas as configuraçõs de execução dos testes pós carregamento)
                - sleep (Diretótio com implementação da função de pausa na execução em segundos predefinidos)
                    - time_sleep.py (Arquivo de classe com implementação da função para pausa na execução)
                - validate (Diretório com implementação da função que valida o status code da requisição)
                    - calidate_status_code.py (Arquivo de classe com implementação da função para validação do status code da requisição)
                - verify (Diretório com implementação de função que verifica a existência de um diretório ou arquivo)
                    - verify_path_exists.py (Arquivo de classe com implementação da função para validação de existência de um arquivo ou diretório)


---
## Possíveis configurações de execução
### Possibilidades para o arquivo settings.json
    {
        "platform_settings": {
            "platform": "api", ["api", "chrome", "firefox", "edge", "ie", "opera", "mobile", "desktop"]
            "application_path": "", ["Caminho do executável da aplicação Windows caso a plataforma seja Desktop"]
            "platform_name": "", ["Nome da plataforma Android ou iOS"]
            "platform_version": "", ["Versão do sistema operacional Android ou iOS"]
            "device_name": "", ["Nome do aparelho Android ou iOS"]
            "application_package": "", ["Pacote da aplicação Android"]
            "application_activity": "", ["Activity da aplicação Android"]
            "automation_name": "", ["Engine de automação ("Appium", "UiAutomator2", "Espresso", "UiAutomator1", "XCUITest")"]
            "app": "", ["Caminho ou URL do executável da aplicação Android ou iOS"]
            "no_reset": "", ["Resetar dados da aplicação true para sim ou false para não"]
            "oauth_client_id": "", ["Client ID gerado no Mobile Center"]
            "oauth_client_secret": "", ["Client Secret Key gerado no Mobile Center"]
            "tenant_id": "", ["ID gerado no Mobile Center"]
            "workspace_name": "", ["Nome da Workspace gerada no Mobile Center"]
            "auto_grant_permissions": "", ["Garantir permissões automaticamente true para sim ou false para não"]
            "udid": "" ["UDID no aparelho no Mobile Center"]
        },
        "execution_model": "behave", ["Modelo de execução dos testes "behave" para BDD, "pytest" para Pytest"]
        "headless": false ["true para execução sem interface, false para execução com interface"]
    }


---
## Iteração dos testes
### Testes Web, Mobile, Desktop e API
    - Sempre que escrever um teste, importar a classe Interact do arquivo de classe interact.py.
    - Neste arquivo está toda a abstração das funções mais úteis do Selenium. 
    - Para utilizar basta chamar a função da classe e passar os parâmetros.
    - As funções do Selenium estão tratando os problemas de não encontro de elementos nas aplicações.
    - As mesmas funções utilizadas para Web, servem para Mobile e Desktop.
    - Nesta classe existem algumas funções úteis, como execução de javascript em páginas Web, verificar existência de arquivos no sistema operacional ou carregamento de dados de um arquivo excel.
    - Nesta classe se encontram as funções de envio de requisições que podem ser utilizadas nos testes de API.
    - Nos testes pode ser utilizada a biblioteca PyHamcrest para testar assertividade
    - No arquivo main.py na raiz, podem ser montadas as suites de execuções dos testes, passando na lista o nome e extensão do arquivo python de teste ou nome e extensão da história do BDD conforme configuração.
    - Esta plataforma suporta Mock nos testes de API, basta enviar o parâmetro “mock=True” e o "text='Dados esperados'"  na requisição a ser realizada dentro do teste escrito.


    * Vale ressaltar que os dados URL e payload são carregados de arquivos JSON e controlados por tags no BDD, portanto o padrão de um arquivo de payload é:
        {
            "Nome da Tag": {
                "url": "URL da requisição",
                "payload": {
                    "Dados da payload"
                }
            }
        }
    Vale ressaltar também que os executáveis dos drivers para instância dos navegadores Web: Firefox, Chrome e Edge devem ser atualizados manualmente conforme necessidade.
    Links para download dos drivers atualizados ou em versões correspondentes: 
        - Firefox: https://github.com/mozilla/geckodriver/releases
        - Chrome: https://chromedriver.chromium.org/downloads
        - Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        - Internet Explorer: https://www.selenium.dev/downloads/
        - Opera: https://github.com/operasoftware/operachromiumdriver/releases
        - Desktop Windows: https://github.com/2gis/Winium.Desktop/releases


---
## Dúvidas

    - Caso seja necessário informações sobre a escrita dos testes, mais detalhes sobre a plataforma, dúvidas ou sugestões, entrar em contato no e-mail: daniel.ferreira@zup.com.br
