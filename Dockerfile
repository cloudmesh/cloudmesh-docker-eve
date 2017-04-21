FROM ubuntu
# Update the package repository
#RUN locale-gen en_US.UTF-8
#ENV LANG en_US.UTF-8
#ENV LANGUAGE en_US:en
#ENV LC_ALL en_US.UTF-8
USER root
RUN mkdir $HOME/app
WORKDIR $HOME/app
RUN mkdir cloudmesh.docker
COPY . $HOME/app/cloudmesh.docker/
RUN apt-get update
RUN apt-get install -y git python-pip mongodb vim
WORKDIR $HOME/app
RUN git clone https://github.com/karvenka/cloudmesh.common.git
RUN git clone https://github.com/karvenka/cmd5.git
RUN git clone https://github.com/karvenka/cloudmesh.rest.git
WORKDIR $HOME/app/cloudmesh.common
RUN python setup.py install
WORKDIR $HOME/app/cmd5
RUN python setup.py install
WORKDIR $HOME/app/cloudmesh.rest
RUN python setup.py install
WORKDIR $HOME/app/cloudmesh.docker
RUN python setup.py install
RUN mkdir $HOME/.cloudmesh
RUN mkdir $HOME/.cloudmesh/eve
WORKDIR /root/.cloudmesh
COPY config/restjson/settings.py eve/
COPY config/cloudmesh_cmd5.yaml .
