Cloudmesh docker
==============

An dynamically extensible CMD5 based command shell to manager single docker
instances and also docker swarm.The client uses eve rest api and mongodb
and is a mutitenant solution for manager docker standalone or docker swarm
instances across multiple servers remotely.

The repository also includes

        - Ansible scripts to install docker in remote hosts
	- Ansible scripts to install docker images(elasticsearch,esrally) in remote hosts based 
	  on dockerfile from local
	- Scripts leveraging cloudmesh.docker code to start a elasticsearch docker cluster on 
	  remote docker hosts
	- Scripts leveraging cloudmesh.docker code to start a elasticsearch swarm cluster on 
	  remote docker hosts
	- Benchmarking elasticsearch on the docker and swarm clusters using esrally 

	
Requirements
------------

* Python 2.7.13

WARNING
-------

WE HAVE NOT YET BUILD IN AUTHENTICATION INTO THE FRAMEWORK, SO RUNNING THIS IS INSECURE

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
    git clone https://github.com/cloudmesh/cloudmesh.common.git
    git clone https://github.com/cloudmesh/cloudmesh.cmd5.git
    git clone https://github.com/cloudmesh/cloudmesh.docker.git

The cmd5 repository contains the shell, while the cloudmesh.docker directory
contains the commands docker and swarm.

To install them simply to the following::

    cd ~/github/cloudmesh.common
    python setup.py install; pip install -e .
    cd ~/github/cloudmesh.cmd5
    python setup.py install; pip install -e .
    cd ~/github/cloudmesh.rest
    python setup.py install; pip install -e
    cd ~/github/cloudmesh.docker
    python setup.py install; pip install -e

Installation from docker
------------------------

We strongly recommend using the docker install as it takes care of
all dependencies.To install and start
use below commands.Please note docker is to be installed
on your local.

Create the cloudmesh docker image with the name ‘cloudmesh.dockers’::

    make docker-build
	
Start a docker container::

    make docker-build
	
Login to the started vm so you can execute docker commands::

    make docker-machine-login
	
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
	
The refresh commands refresh the current status from remote hosts and the
list commands pull the data from local.(This is yet to be fully integrated)
    
docker command
--------------

    cms> docker::
    
          Usage:
            docker host list
            docker host delete ADDR
            docker host NAME ADDR
            docker image refresh
            docker image list [ARG...]
            docker container create NAME IMAGE [ARG...]
            docker container start NAME [ARG...]
            docker container stop NAME [ARG...]
            docker network create IMAGE [ARG...]
            docker network refresh
            docker network list [ARG...]
            docker container refresh
            docker container list [ARG...]
            docker container delete NAME [ARG...]
            docker container run NAME [ARG...]
            docker container pause NAME [ARG...]
            docker container unpause NAME [ARG...]
            docker process config CNAME

  
          Arguments:
            NAME     The name of the docker Host/Container/Network
            IMAGE    Docker server images
            ADDR     IP or Name:port of docker API
            CNAME    Config File Name
            [ARG..]  Denotes a extensible arguments that can be passed as a name value pair.Docker Containers
                     and networks have a lot of customization options.These options are documented here
                     http://docker-py.readthedocs.io/en/stable/index.html
                     All the options are available by simply passing the values as a name value pair
                     eg
                     docker container create NAME IMAGE network_mode=?? entrypoint=??

          Options:
            -v       verbose mode

          Description:
            Manages a virtual docker on a cloud

swarm command
-------------

    cms> swarm::
    
          Usage:
            swarm host list
            swarm host delete ADDR
            swarm host NAME ADDR
            swarm create [ARG...]
            swarm join ADDR TYPE [ARG...]
            swarm leave [ARG...]
            swarm network create IMAGE [ARG...]
            swarm network list [ARG...]
            swarm service create NAME IMAGE [ARG...]
            swarm service list [ARG...]
            swarm service delete NAME
            swarm node list
            swarm image refresh
            swarm image list [ARG...]


          Arguments:
            NAME     The name of the docker swarm
            IMAGE    Docker server images
            ADDR     Address of host ip:port(if port no given default port is assumed)
            TYPE     Whether the node is Manager or Worker
            URL      URL of docker API
            [ARG..]  Denotes a extensible arguments that can be passed as a name value pair.Swarm Services
                     and networks have a lot of customization options.These options are documented here
                     http://docker-py.readthedocs.io/en/stable/index.html
                     All the options are available by simply passing the values as a name value pair
                     eg
                     swarm service create NAME IMAGE hostname=?? networks=??
          Options:
             -v       verbose mode
   
          Description:
             Manages a virtual docker swarm on a cloud



CMD5 configuration
------------------

To configure access to docker on a machine please use the cloudmesh_cmd5.yaml file available
in teh config directory.This file is to be copied to ~/.cloudmesh directory

You will have to do the following modifications to match you machine::

    profile:
        firstname: TBD
        lastname: TBD
        email: TBD
        user: TBD


	system:
        data: ~/.cloudmesh/cloudmesh_inventory.yaml
        console_color: true
    logging:
        file: ~/.cloudmesh/cloudmesh.log
        level: DEBUG
    config:
        path: ~/app/cloudmesh.docker/config/
		
		
Docker Api
----------

The CMD5 docker and swarm commands can be used to work on docker 
installed on any server. The only requirement is to have docker api
exposed out in a certain port.

The repository includes a ansible script availble in config/ansible
directory to install docker on remote hosts as configured in the Hosts 
file.

The YML configs are available in config/ansible/yaml directory.

The YML file docker-chameleon.yml will install the latest docker
on all the remote hosts configured in you hosts file and also enable
your docker remote machines for remote acess .

If you have installed docker manually on the remote hosts please
ensure that the ExecStart
value is set in the /lib/systemd/system/docker.service as below::

    ExecStart=/usr/bin/docker daemon -H fd:// -H tcp://0.0.0.0:4243

Setting the above value and restarting the docker service will ensure 
docker api is exposed and accessible remotely.

Managing Mongo
^^^^^^^^^^^^^^

Next you need to start the mongo service with

::

    cms admin mongo start

You can look at the status and information about the service with ::

    cms admin mongo info
    cms admin mongo status

If you need to stop the service you can use::

    cms admin mongo stop

Managing Eve
^^^^^^^^^^^^^

The settings.py file available as part of cloudmesh.docker/config/restjson needs to be copied to 
~/.cloudmesh/eve directory.The setting.py file has the schema details of the mongo db objects used 
by the client.

Now it is time to start the REST service. THis is done in a separate window with the following commands::

  cms admin rest start

This file is than used by the start action to start the eve service.
Please make sure that you execute this command in a separate window, as
for debugging purposses you will be able to monitor this way interactions
with this service


Steps to execute
----------------
Below are example usage of the command.The first step is always to
set the docker api url::

    cms> docker host test x.x.x.x:4243

    cms> docker host list
	
+----------------+-------+------+--------------+
| Ip             | Name  | Port | Swarmmanager |
+----------------+-------+------+--------------+
| x.x.x.x        | elast | 4243 | False        |
+----------------+-------+------+--------------+

::

    cms> docker image list
+----------------+------------------------------------------+---------------------------------------+------------+
| Ip             | Id                                       | Repository                            | Size       |
+----------------+------------------------------------------+---------------------------------------+------------+
| xxx.xxx.xx.xxx | sha256:5545f4e3b27e330bdeb2b5198e0211273 | karvenka/cloudmesh.docker:latest      | 5586904430 |
|                | 1654d237a0f81ccd0b0e287480a718d          |                                       |            |
| xxx.xxx.xx.xxx | sha256:a21e19753b0c86f2f45a3722e10c1c7f6 | docker.elastic.co/kibana/kibana:5.3.0 | 679453962  |
|                | 2e767e0e4da09043b5ce49b29fa8582          |                                       |            |
+----------------+------------------------------------------+---------------------------------------+------------+

::

    cms> docker container list
+----------------+------------------------------------------+----------+---------------------------------------+---------+
| Ip             | Id                                       | Name     | Image                                 | Status  |
+----------------+------------------------------------------+----------+---------------------------------------+---------+
| xxx.xxx.xx.xxx | b816b199580aa775d747383f179e414dfa9943d4 | /kibana  | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 8fa42c574de747904d501942                 |          |                                       |         |
| xxx.xxx.xx.xxx | f3f6751884c513731564b424b7a9ca4d74a41e7f | /kibana1 | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 15718f580d897f3452f1b85f                 |          |                                       |         |
+----------------+------------------------------------------+----------+---------------------------------------+---------+

::

    cms> docker container create cloudmesh karvenka/cloudmesh.docker:latest
Container 41e9dd186159bc324ed287a0a8db464c723a041e2e29b019a06a35c52f4e613f is created

::

    cms> docker container refresh

+----------------+------------------------------------------+------------+---------------------------------------+---------+
| Ip             | Id                                       | Name       | Image                                 | Status  |
+----------------+------------------------------------------+------------+---------------------------------------+---------+
| xxx.xxx.xx.xxx | 41e9dd186159bc324ed287a0a8db464c723a041e | /cloudmesh | karvenka/cloudmesh.docker:latest      | created |
|                | 2e29b019a06a35c52f4e613f                 |            |                                       |         |
| xxx.xxx.xx.xxx | f3f6751884c513731564b424b7a9ca4d74a41e7f | /kibana1   | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 15718f580d897f3452f1b85f                 |            |                                       |         |
| xxx.xxx.xx.xxx | b816b199580aa775d747383f179e414dfa9943d4 | /kibana    | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 8fa42c574de747904d501942                 |            |                                       |         |
+----------------+------------------------------------------+------------+---------------------------------------+---------+

::

    cms> docker container start 41e9dd186159bc324ed287a0a8db464c723a041e2e29b019a06a35c52f4e613f
    cms> docker container refresh
    
+----------------+------------------------------------------+------------+---------------------------------------+---------+
| Ip             | Id                                       | Name       | Image                                 | Status  |
+----------------+------------------------------------------+------------+---------------------------------------+---------+
| xxx.xxx.xx.xxx | 41e9dd186159bc324ed287a0a8db464c723a041e | /cloudmesh | karvenka/cloudmesh.docker:latest      | exited  |
|                | 2e29b019a06a35c52f4e613f                 |            |                                       |         |
| xxx.xxx.xx.xxx | f3f6751884c513731564b424b7a9ca4d74a41e7f | /kibana1   | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 15718f580d897f3452f1b85f                 |            |                                       |         |
| xxx.xxx.xx.xxx | b816b199580aa775d747383f179e414dfa9943d4 | /kibana    | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 8fa42c574de747904d501942                 |            |                                       |         |
+----------------+------------------------------------------+------------+---------------------------------------+---------+

::

    cms> docker container list

+----------------+------------------------------------------+------------+---------------------------------------+---------+
| Ip             | Id                                       | Name       | Image                                 | Status  |
+----------------+------------------------------------------+------------+---------------------------------------+---------+
| xxx.xxx.xx.xxx | b816b199580aa775d747383f179e414dfa9943d4 | /kibana    | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 8fa42c574de747904d501942                 |            |                                       |         |
| xxx.xxx.xx.xxx | 41e9dd186159bc324ed287a0a8db464c723a041e | /cloudmesh | karvenka/cloudmesh.docker:latest      | exited  |
|                | 2e29b019a06a35c52f4e613f                 |            |                                       |         |
| xxx.xxx.xx.xxx | f3f6751884c513731564b424b7a9ca4d74a41e7f | /kibana1   | docker.elastic.co/kibana/kibana:5.3.0 | created |
|                | 15718f580d897f3452f1b85f                 |            |                                       |         |
+----------------+------------------------------------------+------------+---------------------------------------+---------+
Unit Tests
----------

We are providing a simple set of tests that verify the integration of docker
into cloudmesh. They can either be run with `nosetests` .

Use::

  nosetests -v --nocapture tests/test_docker.py
  nosetests -v --nocapture tests/test_swarm.py

to check them out and see if the tests succeed.




