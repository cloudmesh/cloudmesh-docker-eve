Cloudmesh extdocker
==============

An dynamically extensible CMD5 based command shell to manager single docker instances and also docker swarm

Requirements
------------

* Python 2.7.13

Installation from source
------------------------

Setup a virtualenv either with virtualenv or pyenv.

virtualenv::

    virtualenv ~/ENV2

pyenv::

    pyenev virtualenv 2.7.13 ENV2

Now you need to get two source directories. We assume yo place them in
~/github::

    mkdir ~/github
    cd ~/github
    git clone https://github.com/cloudmesh/common.git
    git clone https://github.com/cloudmesh/cmd5.git
    git clone https://github.com/cloudmesh/extdocker.git

The cmd5 repository contains the shell, while the extdocker directory
contains the commands docker and swarm.

To install them simply to the following::

    cd ~/github/common
    python setup.py install
    cd ~/github/cmd5
    python setup.py install
    cd ~/github/extdocker
    python setup.py install

Execution
---------

to run the shell you can activate it with the cms command. cms stands
for cloudmesh shell::

    (ENV2) $ cms

It will print the banner and enter the shell::

    +-------------------------------------------------------+
    |   ____ _                 _                     _      |
    |  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   |
    | | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  |
    | | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | |
    |  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| |
    +-------------------------------------------------------+
    |                  Cloudmesh CMD5 Shell                 |
    +-------------------------------------------------------+

    cms>


To see the list of commands you can say::

    cms> help

To see the manula page for a specific command, please use::

    help COMMANDNAME

Commands
---------

The following commands are added as part of the project and available
for use via the cloudmesh shell::

    docker
    swarm
    
docker command
--------------

    cms> docker::

      Usage:
        docker api URL
        docker image list
        docker container create NAME IMAGE
        docker container start NAME
        docker container stop NAME
        docker container list
        docker container delete NAME
        docker container attach NAME
        docker container pause NAME
        docker container unpause NAME


      Arguments:
        NAME     The name of the docker
        CLOUD    The name of the cloud on which the virtual docker
                 is to be deployed
        IMAGE    Docker server images
        URL      URL of docker API

      Options:
        -v       verbose mode

      Description:
        Manages a virtual docker on a cloud

swarm command
-------------

    cms> swarm::

      Usage:
        swarm api URL
        swarm create NAME ADDR
        swarm join ADDR
        swarm leave
        swarm update
        swarm reload
        swarm service create IMAGE
        swarm service list
        swarm node list

      Arguments:
        NAME     The name of the docker swarm
        IMAGE    Docker server images
        ADDR     Swarm Address
        URL      URL of docker API

      Options:
         -v       verbose mode

      Description:
         Manages a virtual docker swarm on a cloud


Docker Api
----------

The CMD5 docker and swarm commands can be used to work on docker 
installed on any server.The only requirement is to have docker api
exposed out in a certain port.

As part of the project we are also building a dockerfile which will
contain a docker image with setup files for installing docker on 
remote VM using ansible.(This is currently WIP)

Once docker is instlled on remove please ensure that the DOCKER_OPTS
value is set in the docker file in /etc/default as below::

    DOCKER_OPTS="-H unix:// -H tcp://0.0.0.0:3243"

Setting the above value and restarting the docker service will ensure 
docker api is exposed and accessible remotely

Steps to execute
----------------
Below are example usage of the command.The first step is always to
set the docker api url::

    cms> docker api http://x.x.x.x:4243

    cms> docker image list

    cms> docker container list
    Name            Image           Status
    reverent_cray           ubuntu:latest           created
    suspicious_bhabha               ubuntu:latest           created
    condescending_feynman           ubuntu:latest           exited
    infallible_hodgkin              ubuntu:latest           exited
    gigantic_noyce          ubuntu:latest           exited
    berserk_hugle           ubuntu:latest           exited
    tiny_franklin           ubuntu:latest           exited
    modest_volhard          ubuntu:latest           created
    condescending_heyrovsky         ubuntu:latest           exited
    sad_mccarthy            ubuntu          exited
