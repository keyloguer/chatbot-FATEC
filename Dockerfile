FROM ashander/miniconda3gcc

# 2. Copiar arquivos
# Especificar arquivo-a-arquivo sempre que possível, evitando posívies injeções externas.
#    IN                         OUT
COPY environment.yml            /tmp/environment.yml

RUN apt-get update -qq && \
  apt-get install -y --no-install-recommends \
  build-essential \
  wget \
  openssh-client \
  graphviz-dev \
  graphviz \
  pkg-config \
  git-core \
  openssl \
  libssl-dev \
  libffi6 \
  libffi-dev \
  libpng-dev \
  curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# 3. Declaração de variáveis locais
# ARG: Visível em buildtime
# ENV: Visível em buildtime e runtime. 
ARG ENVROOT=/opt/conda/envs
ARG ENVNAME=rasa-env
ARG ENVPATH=${ENVROOT}/${ENVNAME}
ARG PYTHON=${ENVPATH}/bin/python
ARG PIP=${ENVPATH}/bin/pip

# 4. Configuração de ambiente
# 4a. Atualização do gerenciador de dependências
RUN conda update --yes conda
# 4b. Configuração do ambiente pro rasa.
RUN conda create --name ${ENVNAME} python=3.5 pip
# 4c. Ativa o ambiente. Como o processo é feito por comando source, precisamos passar para o .bashrc e adiciona ao path do OS.
RUN echo "source activate ${ENVNAME}" > ~/.bashrc
ENV PATH ${PYTHONPATH}/bin:$PATH
# 4d. Instala o sklearn em sua última versão

WORKDIR /app

COPY requirements.txt /app

RUN ${PIP} install -r requirements.txt
# 4e. Instala o corpus em português para o spacy.
# RUN $ENVS/rasa-env/bin/python -m spacy download pt
RUN ${PYTHON} -m spacy download pt

COPY /models/  /app/models
COPY . /app/
CMD [ "/bin/bash", "app.sh" ]