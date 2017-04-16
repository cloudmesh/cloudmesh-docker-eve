FROM ubuntu
# Update the package repository
#RUN locale-gen en_US.UTF-8  
#ENV LANG en_US.UTF-8  
#ENV LANGUAGE en_US:en  
#ENV LC_ALL en_US.UTF-8 
RUN mkdir ~/app
WORKDIR ~/app
RUN mkdir ~/app/cloudmesh.docker
ADD . ~/app/cloudmesh.docker/
RUN apt-get update
RUN apt-get install -y git python-pip mongodb 
RUN git clone https://github.com/cloudmesh/cloudmesh.common.git
RUN git clone https://github.com/cloudmesh/cloudmesh.cmd5.git
RUN git clone https://github.com/cloudmesh/cloudmesh.docker.git
RUN git clone https://github.com/cloudmesh/cloudmesh.rest.git
RUN mkdir ~/.cloudmesh
COPY config/cloudmesh_cmd5.yaml ~/.cloudmesh/
RUN mkdir ~/.cloudmesh/eve
COPY config/restjson/settings.py ~/.cloudmesh/eve/