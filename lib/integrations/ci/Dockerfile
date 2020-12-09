# Utilizar imagem base do Python 3.8.5 em Debian
FROM python:3.8.5-buster

# Definir o mantenedor da imagem
LABEL maintener="daniel.ferreira@zup.com.br"

# Definir as variáveis que serão utilizadas ao longo do build
ARG proxy
ARG git_url
ARG workspaces
ARG pip_proxy_conf

# Ajustar fuso horário
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Exportar configurações de proxy para o S.O e para o pip
RUN mkdir -p $HOME/.config/pip/ && echo $pip_proxy_conf > $HOME/.config/pip/pip.conf
ENV http_proxy=$proxy
ENV https_proxy=$proxy

# Atualizar a imagem e instalar dependências do S.O para o projeto
RUN apt -o Acquire::http::proxy=$proxy \
    -o Acquire::https::proxy=$proxy update && \
    apt -o Acquire::http::proxy=$proxy \
    -o Acquire::https::proxy=$proxy full-upgrade -f -y && \
    apt -o Acquire::http::proxy=$proxy \
    -o Acquire::https::proxy=$proxy install -f -y \
    sudo git chromium firefox-esr xvfb curl wget vim \
    default-jdk

# Configurar verificação de SSL no Git
RUN git config --global http.sslVerify false

# Clonar o projeto e instalar dependências do projeto no Python
RUN mkdir -p $workspaces && cd $workspaces && git clone $git_url
RUN sudo python3.8 -m pip install --upgrade pip && sudo python3.8 -m pip install -r $workspaces/pytap/requirements.txt

# Criar variável de ambiente para Workspaces
ENV workspaces=$workspaces

# Configurar execução do projeto
CMD ["/bin/bash", "-c", "cd $workspaces/pytap/ && python3.8 main.py"]
