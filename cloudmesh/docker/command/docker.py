from __future__ import print_function

import os
from cloudmesh.common.ConfigDict import ConfigDict
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command

from cloudmesh.api.docker_client import Docker


class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
        ::

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
            docker container attach NAME [ARG...]
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

        """

        kwargs = {}

        if arguments.ARG:
            for j in arguments.ARG:
                kwargs[j.split('=')[0].strip()] = j.split('=')[1].strip()

        stopwatch = StopWatch()
        stopwatch.start('E2E')
        Base = ConfigDict('cloudmesh_cmd5.yaml',
                            verbose=False)

        os.environ["DOCKER_HOST"] = Base['cloudmesh']['container']['docker']['work']['host']


        if arguments.host and arguments.list:
            docker = Docker(os.environ["DOCKER_HOST"])
            docker.host_list()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host and arguments.delete:
            docker = Docker(os.environ["DOCKER_HOST"])
            docker.host_delete("{ADDR}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host :
            docker = Docker("{ADDR}".format(**arguments))
            docker.host_create("{ADDR}".format(**arguments),"{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            Base['cloudmesh']['container']['docker']['work']['host'] = "{ADDR}".format(**arguments)
            Base.save()
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker api host(IP or Name : Port )")

        docker = Docker(os.environ["DOCKER_HOST"])


        if arguments.container and arguments.create and arguments.NAME and arguments.IMAGE:
            docker.container_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            #
            # I have not tested this yet but i added
            #
            # stopwatch.verbose = True    # doe snot print if set to false, default is true
            # stopwatch.print('Time Taken:', 'E2E')
            #
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.start and arguments.NAME:
            status = "start"
            docker.container_status_change(status, "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.stop and arguments.NAME:
            status = "stop"
            docker.container_status_change(status, "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return


        if arguments.container and arguments.list:
            docker.container_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.refresh:
            docker.container_refresh(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return


        if arguments.container and arguments.delete and arguments.NAME:
            docker.container_delete("{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.attach and arguments.NAME:
            docker.container_attach("{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.pause and arguments.NAME:
            status = "pause"
            docker.container_status_change(status, "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.unpause and arguments.NAME:
            status = "unpause"
            docker.container_status_change(status, "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.restart and arguments.NAME:
            status = "restart"
            docker.container_status_change("{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return


        if arguments.image and arguments.list:
            docker.images_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.image and arguments.refresh:
            docker.images_refresh(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.create and arguments.NAME and arguments.IMAGE:
            docker.network_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.list:
            docker.network_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.refresh:
            docker.network_refresh(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.process and arguments.config and arguments.CNAME:
            print (Base['cloudmesh']['config']['path'])

            Config = ConfigDict(arguments.CNAME,
                                verbose=True, load_order=[Base['cloudmesh']['config']['path']],reload=True)
            print (Config)

            docker = Docker(Config['docker']['host'])
            containerId = docker.container_create(Config['docker']['container']['image'])

            if Config['docker']['container']['start'] == True:
                status = 'start'
                docker.container_status_change(status, containerName=containerId)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return




