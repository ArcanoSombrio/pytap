# Utilizar imagem base do Python 3.8.5
FROM python:3.8.5-buster

# Definir o mantenedor da imagem
LABEL maintener="daniel.ferreira@zup.com.br"

# Definir as variáveis que serão utilizadas ao longo do build
ARG http_proxy=http://proxyad.itau:8080
ARG https_proxy=http://proxyad.itau:8080
ARG git_url
ARG workspaces=$HOME/Documents/Workspaces
ARG pip_proxy_conf='[global]\nindex-url = https://painel.repodep.des.cloud.ihf/artifactory/api/pypi/python-devel/simple\ntrusted-host = painel.repodep.des.cloud.ihf'

# Exportar configurações de proxy para o S.O
RUN echo export http_proxy=$http_proxy > $HOME/.bashrc
RUN echo export https_proxy=$https_proxy > $HOME/.bashrc
RUN /bin/bash -c "source $HOME/.bashrc"

# Atualizar a imagem
RUN apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy update
RUN apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy full-upgrade -f -y

# Instalar dependências do S.O
RUN apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy update
RUN apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy install -f -y \
    git chromium firefox-esr xvfb curl wget

# Clonar o projeto e instalar dependências do projeto no Python
RUN mkdir -p $workspaces
RUN git config --global http.sslVerify false
RUN cd $workspaces && git clone $git_url
RUN mkdir -p $HOME/.config/pip/
RUN echo $pip_proxy_conf > $HOME/.config/pip/pip.conf
RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r $workspaces/pytap/requirements.txt
