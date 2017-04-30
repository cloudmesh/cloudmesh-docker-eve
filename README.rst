Cloudmesh docker
==============

An dynamically extensible CMD5 based command shell to manager single docker
instances and also docker swarm.The client uses eve rest api and mongodb
and is a multitenant solution for manager docker standalone or docker swarm
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
- Benchmarking scripts for the cloudmesh docker application 

	
Requirements
------------

* Python 2.7.13
* Ubuntu 16.04

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

Docker Community Edition is to be used for local install.Please refer
instrutions on https://www.docker.com/community-edition to install docker.

Create the cloudmesh docker image with the name ‘cloudmesh.docker’::

    make docker-build
	
Start a docker container::

    make docker-machine
	
Login to the started vm so you can execute docker commands::

    make docker-machine-login
	
Please note we have automated mount points for the source code and the data directories.
So we strongly recommend using the above commands to use the repository .You can also use
the standard docker commands to start the container however you will manually need to ensure 
the mouting of the directories and networking requirements for the container.
	
Configuration
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
        base: /app/cloudmesh.docker/

Managing Mongo
^^^^^^^^^^^^^^

Next you need to start the mongo service with::

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

Ansible Scripts
--------------	

The project includes multiple Ansible scripts available in the 
/config/ansible directory.The Ansible playbook YML files are 
available in the /config/ansible/YAML directory

::

	docker.yml -       Install Docker on remote hosts
	
	docker-hosts.yml - Make entry in /etc/hosts for every server
			   in your host file with the host name as defined in
			   the ansible inventory.txt so that we can refer to
			   the hosts via standard names across across servers 
			   without the need for using a Ip address

	docker-image-install.yml - Is a reference template for installing docker
				   on remote hosts.This Playbook will automatically
				   sync the /config/docker folder to the remote
				   and run the Dockerfile in them to build the images.
						   
Ansible Inventory
-----------------

A key requirement for using the repository is to build a host file.A template of the
host file is available in /config/ansible.Please set this up before using the ansible
scripts::

        [docker-cluster]
        docker1 ansible_ssh_user=?? ansible_ssh_host=??.??.??.?? internal_ip=??.??.??.??
        docker2 ansible_ssh_user=?? ansible_ssh_host=??.??.??.?? internal_ip=??.??.??.??
        [swarm-cluster]
        docker3 ansible_ssh_user=?? ansible_ssh_host=??.??.??.?? internal_ip=??.??.??.??
        docker4 ansible_ssh_user=?? ansible_ssh_host=??.??.??.?? internal_ip=??.??.??.??
        [Benchmark-Tool-Server]
        dockerconfig ansible_ssh_user=?? ansible_ssh_host=??.??.??.?? internal_ip=??.??.??.??
	
The docker-hosts ansible playbook uses the internal_ip field to setup the /etc/hosts
entry in all the servers listed here.

Also you would need to make entry for these hosts in the /etc/hosts of your local machine
to start using the test scripts in the repo.::

		??.??.??.?? docker1
		??.??.??.?? docker2
		??.??.??.?? docker3
		??.??.??.?? docker4
		??.??.??.?? dockerconfig

We recommend that you maintain separate host files for each cloud against which you would
like to use the client.eg

::

	hosts.chameleon
	hosts.aws
	hosts.jetstream

If you are using cloudmesh client you can use the below commands to setup a cluster of servers needed.

::

	cm secgroup add docker docker_cluster 1 65535 tcp 0.0.0.0/0
	cm secgroup upload
	cm cluster define --count 3 --image CC-Ubuntu16.04 --flavor m1.large --secgroup docker
	cm cluster allocate
    cm node list
	

Run Ansible Scripts
---------------------

Once the host file setup is done installation of the docker in all the remote hosts is trivial.
You can chose to use the cms command build to run the docker setup ansible scripts

::

	cms docker install hosts.chameleon
	cms swarm install hosts.jetstream

You can also run the playbooks manually at /config/ansible::

	ansible-playbook -i hosts.chameleon docker.yml
	ansible-playbook -i hosts.chameleon docker-hosts.yml


Docker Api
----------

The CMD5 docker and swarm commands can be used to work on docker 
installed on any server. The only requirement is to have docker api
exposed out in a certain port.

The repository includes a ansible script available in config/ansible
directory to install docker on remote hosts as configured in the Hosts 
file.

The YML configs are available in config/ansible/yaml directory.

The YML file docker.yml will install the latest docker
on all the remote hosts configured in you hosts file and also enable
your docker remote machines for remote acess .

If you have installed docker manually on the remote hosts please
ensure that the ExecStart
value is set in the /lib/systemd/system/docker.service as below::

    ExecStart=/usr/bin/docker daemon -H fd:// -H tcp://0.0.0.0:4243

Setting the above value and restarting the docker service will ensure 
docker api is exposed and accessible remotely.


Execution
---------

To run the shell you can activate it with the cms command. cms stands
for cloudmesh shell::

    $ cms

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

::

          Usage:
            docker host list
            docker host delete ADDR
            docker host install HFILE
            docker host NAME ADDR
            docker benchmark N
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
            docker container run NAME IMAGE [ARG...]
            docker container pause NAME [ARG...]
            docker container unpause NAME [ARG...]
            docker process config CNAME


  
          Arguments:
            NAME     The name of the docker Host/Container/Network
            IMAGE    Docker server images
            ADDR     IP or Name:port of docker API
            CNAME    Config File Name
            HFILE    Ansible Inventory.txt to be used
            N        Number of benchmark iterations
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

::

          Usage:
            swarm host list
            swarm host delete ADDR
            swarm host install HFILE
            swarm host NAME ADDR
            swarm benchmark N
            swarm create [ARG...]
            swarm join ADDR TYPE [ARG...]
            swarm leave [ARG...]
            swarm network create NAME [ARG...]
            swarm network list [ARG...]
            swarm network refresh
            swarm network delete NAME
            swarm service create NAME IMAGE  [ARG...]
            swarm service list [ARG...]
            swarm service delete NAME
            swarm service refresh
            swarm node list
            swarm node refresh
            swarm image refresh
            swarm image list [ARG...]
            swarm container refresh
            swarm container list [ARG...]


          Arguments:
            NAME     The name of the docker swarm
            IMAGE    Docker server images
            HFILE    Ansible Inventory.txt to be used
            N        Number of Benchmark iterations
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


Sample Execution Steps
----------------------

Below are example usage of the command.The first step is always to
set the docker api url

::

	cms docker host docker1 docker1:4243
	Host docker1 is Added and is the default swarm host

::

	cms docker host docker2 docker2:4243
	Host docker2 is Added and is the default swarm host

::

	cms docker host list

	+---------+---------+------+-----------+
	| Ip      | Name    | Port | Swarmmode |
	+---------+---------+------+-----------+
	| docker1 | docker1 | 4243 |           |
	| docker2 | docker2 | 4243 |           |
	| docker4 | docker4 | 4243 |           |
	| docker3 | docker3 | 4243 |           |
	+---------+---------+------+-----------+

::

	cms docker image refresh

	+---------+------------------------------------------+------------------------------------------+----------+
	| Ip      | Id                                       | Repository                               | Size(GB) |
	+---------+------------------------------------------+------------------------------------------+----------+
	| docker1 | sha256:909af725a4032bf00f36b45b358c46d6a | elasticsearch:swarm                      | 0.2      |
	|         | 67f8b3201747c8992c920bc34d3148c          |                                          |          |
	| docker1 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker2 | sha256:f70df3612f57225cb85bc20442c42c744 | elasticsearch:swarm                      | 0.2      |
	|         | bf303e3cdcde08c0092c16a8d655748          |                                          |          |
	| docker2 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker4 | sha256:c66e748329975c1ca97ecc23b2b5fcc02 | elasticsearch:swarm                      | 0.2      |
	|         | f6781885053321add902e9267c42880          |                                          |          |
	| docker4 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker3 | sha256:ec53e8e805a81d93f3c8d812f3b179f08 | elasticsearch:swarm                      | 0.2      |
	|         | 9695fcfb7d8361ada89588c4da69c82          |                                          |          |
	| docker3 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	+---------+------------------------------------------+------------------------------------------+----------+

::

	cms docker image list

	+---------+------------------------------------------+------------------------------------------+----------+
	| Ip      | Id                                       | Repository                               | Size(GB) |
	+---------+------------------------------------------+------------------------------------------+----------+
	| docker1 | sha256:909af725a4032bf00f36b45b358c46d6a | elasticsearch:swarm                      | 0.2      |
	|         | 67f8b3201747c8992c920bc34d3148c          |                                          |          |
	| docker1 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker3 | sha256:ec53e8e805a81d93f3c8d812f3b179f08 | elasticsearch:swarm                      | 0.2      |
	|         | 9695fcfb7d8361ada89588c4da69c82          |                                          |          |
	| docker3 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker2 | sha256:f70df3612f57225cb85bc20442c42c744 | elasticsearch:swarm                      | 0.2      |
	|         | bf303e3cdcde08c0092c16a8d655748          |                                          |          |
	| docker2 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	| docker4 | sha256:c66e748329975c1ca97ecc23b2b5fcc02 | elasticsearch:swarm                      | 0.2      |
	|         | f6781885053321add902e9267c42880          |                                          |          |
	| docker4 | sha256:ccec59a7dd849e99addc11a9bd11b15e9 | docker.elastic.co/elasticsearch/elastics | 0.19     |
	|         | addf2dff7741cf82b603d01d0ccdb54          | earch:5.3.0                              |          |
	+---------+------------------------------------------+------------------------------------------+----------+

::

	cms docker container refresh

	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| Ip      | Id                                       | Name            | Image                | Status | StartedAt                      |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| docker1 | 31d3cfb389f14f3fbf3ff434584690590c70b37f | /elasticsearch1 | elasticsearch:docker | exited | 2017-04-22T16:47:31.585424378Z |
	|         | c5cd6416db389e49df4d643e                 |                 |                      |        |                                |
	| docker1 | 8a7e6543f9fa1052c05617cbdd4ac87824b402c0 | /elasticsearch2 | elasticsearch:docker | exited | 2017-04-22T16:47:39.25325675Z  |
	|         | 86cd0219b72178d9b75aec0b                 |                 |                      |        |                                |
	| docker2 | 42bd36cfb7a6b44bf423373f5cbbcb11d3a24313 | /elasticsearch4 | elasticsearch:docker | exited | 2017-04-22T16:48:06.191045149Z |
	|         | bcd85565f87f0dcffd9c4122                 |                 |                      |        |                                |
	| docker2 | cb06419167b6d403bd868fca0229637f4cc84fa1 | /elasticsearch3 | elasticsearch:docker | exited | 2017-04-22T16:48:13.076917845Z |
	|         | 6195a7650129038b7e85895b                 |                 |                      |        |                                |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+

::

	cms docker container list

	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| Ip      | Id                                       | Name            | Image                | Status | StartedAt                      |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| docker1 | 31d3cfb389f14f3fbf3ff434584690590c70b37f | /elasticsearch1 | elasticsearch:docker | exited | 2017-04-22T16:47:31.585424378Z |
	|         | c5cd6416db389e49df4d643e                 |                 |                      |        |                                |
	| docker1 | 8a7e6543f9fa1052c05617cbdd4ac87824b402c0 | /elasticsearch2 | elasticsearch:docker | exited | 2017-04-22T16:47:39.25325675Z  |
	|         | 86cd0219b72178d9b75aec0b                 |                 |                      |        |                                |
	| docker2 | 42bd36cfb7a6b44bf423373f5cbbcb11d3a24313 | /elasticsearch4 | elasticsearch:docker | exited | 2017-04-22T16:48:06.191045149Z |
	|         | bcd85565f87f0dcffd9c4122                 |                 |                      |        |                                |
	| docker2 | cb06419167b6d403bd868fca0229637f4cc84fa1 | /elasticsearch3 | elasticsearch:docker | exited | 2017-04-22T16:48:13.076917845Z |
	|         | 6195a7650129038b7e85895b                 |                 |                      |        |                                |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+

::

	cms docker container create test1 elasticsearch:docker
	Container test1 is Created

::

	cms docker container start test1
	Container test1 status changed to start

::

	cms docker container list

	+---------+------------------------------------------+-----------------+----------------------+---------+--------------------------------+
	| Ip      | Id                                       | Name            | Image                | Status  | StartedAt                      |
	+---------+------------------------------------------+-----------------+----------------------+---------+--------------------------------+
	| docker1 | 31d3cfb389f14f3fbf3ff434584690590c70b37f | /elasticsearch1 | elasticsearch:docker | exited  | 2017-04-22T16:47:31.585424378Z |
	|         | c5cd6416db389e49df4d643e                 |                 |                      |         |                                |
	| docker1 | 8a7e6543f9fa1052c05617cbdd4ac87824b402c0 | /elasticsearch2 | elasticsearch:docker | exited  | 2017-04-22T16:47:39.25325675Z  |
	|         | 86cd0219b72178d9b75aec0b                 |                 |                      |         |                                |
	| docker2 | 42bd36cfb7a6b44bf423373f5cbbcb11d3a24313 | /elasticsearch4 | elasticsearch:docker | exited  | 2017-04-22T16:48:06.191045149Z |
	|         | bcd85565f87f0dcffd9c4122                 |                 |                      |         |                                |
	| docker2 | cb06419167b6d403bd868fca0229637f4cc84fa1 | /elasticsearch3 | elasticsearch:docker | exited  | 2017-04-22T16:48:13.076917845Z |
	|         | 6195a7650129038b7e85895b                 |                 |                      |         |                                |
	| docker2 | ad271e34bfb32422b1bc134250daec2941461910 | /test1          | elasticsearch:docker | running | 2017-04-24T11:42:04.659965801Z |
	|         | 933ed3537a4705a26f93a67d                 |                 |                      |         |                                |
	+---------+------------------------------------------+-----------------+----------------------+---------+--------------------------------+

::

	cms docker container stop test1
	Container test1 status changed to stop

::

	cms docker container delete test1
	Container test1 is deleted

::

	cms docker container list

	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| Ip      | Id                                       | Name            | Image                | Status | StartedAt                      |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+
	| docker1 | 31d3cfb389f14f3fbf3ff434584690590c70b37f | /elasticsearch1 | elasticsearch:docker | exited | 2017-04-22T16:47:31.585424378Z |
	|         | c5cd6416db389e49df4d643e                 |                 |                      |        |                                |
	| docker1 | 8a7e6543f9fa1052c05617cbdd4ac87824b402c0 | /elasticsearch2 | elasticsearch:docker | exited | 2017-04-22T16:47:39.25325675Z  |
	|         | 86cd0219b72178d9b75aec0b                 |                 |                      |        |                                |
	| docker2 | 42bd36cfb7a6b44bf423373f5cbbcb11d3a24313 | /elasticsearch4 | elasticsearch:docker | exited | 2017-04-22T16:48:06.191045149Z |
	|         | bcd85565f87f0dcffd9c4122                 |                 |                      |        |                                |
	| docker2 | cb06419167b6d403bd868fca0229637f4cc84fa1 | /elasticsearch3 | elasticsearch:docker | exited | 2017-04-22T16:48:13.076917845Z |
	|         | 6195a7650129038b7e85895b                 |                 |                      |        |                                |
	+---------+------------------------------------------+-----------------+----------------------+--------+--------------------------------+

::

	cms docker network refresh

	+---------+------------------------------------------+-----------------+------------+
	| Ip      | Id                                       | Name            | Containers |
	+---------+------------------------------------------+-----------------+------------+
	| docker1 | feb6b33ba133ccb1f72e881e9ac46974f1ea117d | none            | {}         |
	|         | b0b4db39fb087644d55c6342                 |                 |            |
	| docker1 | 4a3311f9f6acf4401461e2e2dc3ddb39c9143bed | host            | {}         |
	|         | 611b20d907b3d899b595e597                 |                 |            |
	| docker1 | 87209b9615716884e2ed8490b59ea805780598a8 | bridge          | {}         |
	|         | 5a18bee6c27ba03aad58f14a                 |                 |            |
	| docker2 | 57bcbb05a76f042e4c07b265d6b4cb2126abdcb6 | host            | {}         |
	|         | 0a07e0e2e173dfacb3d09769                 |                 |            |
	| docker2 | 9f44589db4def03fe5c11e0f560b357909d46528 | bridge          | {}         |
	|         | f02b8ce4161acf58f57202c4                 |                 |            |
	| docker2 | bc39e454661b05050da6b933ee2ec52fbf466caa | none            | {}         |
	|         | 565de287de1941760babbec0                 |                 |            |
	| docker2 | da862dc075bd3458063579675ed2007c65425261 | docker_gwbridge | {}         |
	|         | dd937f49c3231699b86057a3                 |                 |            |
	| docker4 | 92c7eed3ae09c5bf04ee2edcbcd9d8f40c3e52ec | bridge          | {}         |
	|         | d8efd268f7ade74fe2436b74                 |                 |            |
	| docker4 | 3c90bf98d4d991a17db762e07e5f4c3ab9df06f2 | none            | {}         |
	|         | 6f09679144e45236b995a6d3                 |                 |            |
	| docker4 | a134cbac21ea9c7e43d28314266f1aec4c8fcedd | docker_gwbridge | {}         |
	|         | 3ae60ba3041f0d7cc8ff7bbc                 |                 |            |
	| docker4 | c87d97dde5870d21e4f57052d4bd51d7e670d671 | host            | {}         |
	|         | 99a71552f5e5c9514e965e18                 |                 |            |
	| docker3 | 0db9de4744c642ea406aa3b22d2d185b46716e53 | docker_gwbridge | {}         |
	|         | 0c6e5dedbb90be1e4b59236e                 |                 |            |
	| docker3 | 861862abf66bec01af7d4149c91c28d979e1dda7 | host            | {}         |
	|         | 31266eb30bc5c76a7aae551f                 |                 |            |
	| docker3 | 109ed16096d208442f4697b1c25559e99565fd27 | bridge          | {}         |
	|         | 17bd3e5b2285de7513066d62                 |                 |            |
	| docker3 | ceee39512a4de82efdaefb6e6f24d3fc9f73c19e | none            | {}         |
	|         | 88be3886cb2c74f0d9b30e71                 |                 |            |
	+---------+------------------------------------------+-----------------+------------+

::

	cms docker network list

	+---------+------------------------------------------+-----------------+------------+
	| Ip      | Id                                       | Name            | Containers |
	+---------+------------------------------------------+-----------------+------------+
	| docker1 | 4a3311f9f6acf4401461e2e2dc3ddb39c9143bed | host            | {}         |
	|         | 611b20d907b3d899b595e597                 |                 |            |
	| docker3 | 861862abf66bec01af7d4149c91c28d979e1dda7 | host            | {}         |
	|         | 31266eb30bc5c76a7aae551f                 |                 |            |
	| docker3 | ceee39512a4de82efdaefb6e6f24d3fc9f73c19e | none            | {}         |
	|         | 88be3886cb2c74f0d9b30e71                 |                 |            |
	| docker1 | feb6b33ba133ccb1f72e881e9ac46974f1ea117d | none            | {}         |
	|         | b0b4db39fb087644d55c6342                 |                 |            |
	| docker1 | 87209b9615716884e2ed8490b59ea805780598a8 | bridge          | {}         |
	|         | 5a18bee6c27ba03aad58f14a                 |                 |            |
	| docker2 | 57bcbb05a76f042e4c07b265d6b4cb2126abdcb6 | host            | {}         |
	|         | 0a07e0e2e173dfacb3d09769                 |                 |            |
	| docker2 | 9f44589db4def03fe5c11e0f560b357909d46528 | bridge          | {}         |
	|         | f02b8ce4161acf58f57202c4                 |                 |            |
	| docker2 | bc39e454661b05050da6b933ee2ec52fbf466caa | none            | {}         |
	|         | 565de287de1941760babbec0                 |                 |            |
	| docker2 | da862dc075bd3458063579675ed2007c65425261 | docker_gwbridge | {}         |
	|         | dd937f49c3231699b86057a3                 |                 |            |
	| docker4 | 92c7eed3ae09c5bf04ee2edcbcd9d8f40c3e52ec | bridge          | {}         |
	|         | d8efd268f7ade74fe2436b74                 |                 |            |
	| docker4 | 3c90bf98d4d991a17db762e07e5f4c3ab9df06f2 | none            | {}         |
	|         | 6f09679144e45236b995a6d3                 |                 |            |
	| docker4 | a134cbac21ea9c7e43d28314266f1aec4c8fcedd | docker_gwbridge | {}         |
	|         | 3ae60ba3041f0d7cc8ff7bbc                 |                 |            |
	| docker4 | c87d97dde5870d21e4f57052d4bd51d7e670d671 | host            | {}         |
	|         | 99a71552f5e5c9514e965e18                 |                 |            |
	| docker3 | 0db9de4744c642ea406aa3b22d2d185b46716e53 | docker_gwbridge | {}         |
	|         | 0c6e5dedbb90be1e4b59236e                 |                 |            |
	| docker3 | 109ed16096d208442f4697b1c25559e99565fd27 | bridge          | {}         |
	|         | 17bd3e5b2285de7513066d62                 |                 |            |
	+---------+------------------------------------------+-----------------+------------+


Unit Tests
----------

We are providing a simple set of tests that verify the integration of docker
into cloudmesh. They can either be run with `nosetests` .

Use::

  nosetests -v --nocapture tests/test_docker.py
  nosetests -v --nocapture tests/test_swarm.py

to check them out and see if the tests succeed.

Benchmarking
------------

We are providing a set of benchmark scripts that will help you to easily benchmark
the application. They can either be run with cms command .

Use::

  cms docker benchmark N
  cms swarm  benchmark N

N denotes the number of iterations the benchmark is to be done.The results will shown
on the on the command prompt as well as a detailed csv will be generated to 
/benchmark directory with the timestamp of each run.

Use case scripts
----------------

We are providing a set of sample scripts to demonstrate the possible usecases of the
cloudmesh client.The scripts are available at /scripts directory.The scripts can be 
run using the below command.

::

	python run_script.py FILENAME [HOSTFILE]

A sample script to setup elastic search cluster on docker

::

	Command Name#Command
	ansible-docker-image#ansible-playbook --inventory-file=../config/ansible/$hosts ../config/ansible/yaml/docker-image-install.yml
	Host-Create1#cms docker host docker1 docker1:4243
	Container-Create1#cms docker container create elasticsearch1 elasticsearch:docker network_mode=host environment=["http.host=0.0.0.0","transport.host=0.0.0.0","discovery.zen.ping.unicast.hosts=docker1,docker2"]
	Container-Create2#cms docker container create elasticsearch2 elasticsearch:docker network_mode=host environment=["http.host=0.0.0.0","transport.host=0.0.0.0","discovery.zen.ping.unicast.hosts=docker1,docker2"]
	Container-Start1#cms docker container start elasticsearch1
	Sleep1#sleep 10
	Container-Start2#cms docker container start elasticsearch2
	Sleep2#sleep 10
	Container-List1#cms docker container list
	Container-Refresh1#cms docker container refresh
	Host-Creat2#cms docker host docker2 docker2:4243
	Container-Create3#cms docker container create elasticsearch3 elasticsearch:docker network_mode=host environment=["http.host=0.0.0.0","transport.host=0.0.0.0","discovery.zen.ping.unicast.hosts=docker1,docker2"]
	Container-Create4#cms docker container create elasticsearch4 elasticsearch:docker network_mode=host environment=["http.host=0.0.0.0","transport.host=0.0.0.0","discovery.zen.ping.unicast.hosts=docker1,docker2"]
	Container-Start3#cms docker container start elasticsearch3
	Sleep3#sleep 10
	Container-Start4#cms docker container start elasticsearch4
	Sleep5#sleep 10
	Container-List2#cms docker container list
	Container-Refresh2#cms docker container refresh

A sample script to setup elastic search cluster on swarm

::

	Command Name#Command
	ansible-docker-image#ansible-playbook --inventory-file=../config/ansible/$host ../config/ansible/yaml/docker-image-install.yml
	Host-Create1#cms swarm host docker3 docker3:4243
	Host-Create2#cms swarm host docker4 docker4:4243
	Swarm-Create#cms swarm create
	Host-Create3#cms swarm host docker3 docker3:4243
	Swarm-Join#cms swarm join docker4 Worker
	Host-Create4#cms swarm host docker4 docker4:4243
	Network-Create1#cms swarm network create elastic_cluster driver="overlay"
	Sleep1#sleep 10
	Service-Create1#cms swarm service create elasticsearch elasticsearch:swarm ServiceMode.mode="replicated" ServiceMode.replicas=4 EndpointSpec.ports=["9200:9200"] networks=["elastic_cluster"] env=["SERVICE_NAME=elasticsearch"]
	Sleep1#sleep 15
	Container-Refresh1#cms swarm container refresh



