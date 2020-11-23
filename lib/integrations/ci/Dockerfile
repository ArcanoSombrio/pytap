# Utilizar imagem base do Python 3.8.5
FROM python:3.8.5-buster

# Definir o mantenedor da imagem
LABEL maintener="daniel.ferreira@zup.com.br"

# Definir as variáveis que serão utilizadas ao longo do build
ARG http_proxy=http://proxyad.itau:8080
ARG https_proxy=http://proxyad.itau:8080
ARG git_url=https://github.com/ArcanoSombrio/pytap.git
ARG workspaces=/root/Documents/Workspaces
ARG pip_proxy_conf='[global]\nindex-url = https://painel.repodep.des.cloud.ihf/artifactory/api/pypi/python-devel/simple\ntrusted-host = painel.repodep.des.cloud.ihf'

# Ajustar fuso horário
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Exportar configurações de proxy para o S.O e para o pip
RUN mkdir -p $HOME/.config/pip/ && echo $pip_proxy_conf > $HOME/.config/pip/pip.conf
RUN echo export http_proxy=$http_proxy > $HOME/.bashrc && echo export https_proxy=$https_proxy > $HOME/.bashrc
RUN /bin/bash -c "source $HOME/.bashrc"

# Atualizar a imagem e instalar dependências do S.O
RUN apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy update && \
    apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy full-upgrade -f -y && \
    apt -o Acquire::http::proxy=$http_proxy \
    -o Acquire::https::proxy=$https_proxy install -f -y \
    sudo git chromium firefox-esr xvfb curl wget

# Clonar o projeto e instalar dependências do projeto no Python
RUN git config --global http.sslVerify false
RUN mkdir -p $workspaces && cd $workspaces && git clone $git_url
RUN sudo python3.8 -m pip install --upgrade pip && sudo python3.8 -m pip install -r $workspaces/pytap/requirements.txt

# Criar variável de ambiente para Workspaces
ENV workspaces=$workspaces

# Configurar execução do projeto
CMD ["python3.8", "/root/Documents/Workspaces/pytap/main.py"]
# CMD ["/bin/bash"]
