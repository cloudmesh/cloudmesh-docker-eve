from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.docker_client import Docker
import os
from cloudmesh.common.ConfigDict import ConfigDict
from cloudmesh.common.StopWatch import StopWatch


class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
        ::

          Usage:
            docker api URL
            docker image list
            docker container create NAME IMAGE [ARG...]
            docker container start NAME [ARG...]
            docker container stop NAME [ARG...]
            docker container list
            docker container delete NAME [ARG...]
            docker container attach NAME [ARG...]
            docker container pause NAME [ARG...]
            docker container unpause NAME [ARG...]
            docker process config CNAME

  
          Arguments:
            NAME     The name of the docker
            CLOUD    The name of the cloud on which the virtual docker
                     is to be deployed
            IMAGE    Docker server images
            URL      URL of docker API
            CNAME    Config File Name

          Options:
            -v       verbose mode

          Description:
            Manages a virtual docker on a cloud

        """

        print (arguments)
        stopwatch = StopWatch()
        stopwatch.start('E2E')
        Base = ConfigDict('cloudmesh_cmd5.yaml',
                            verbose=False)


        if arguments.api :
            docker = Docker("{URL}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return
        docker = Docker(os.environ["DOCKER_HOST"])
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker api url(eg:http://x.x.x.x:yyyy): ")

        if arguments.container and arguments.create and arguments.NAME and arguments.IMAGE:
            docker.container_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.start and arguments.NAME:
            status = "start"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.stop and arguments.NAME:
            status = "stop"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return


        if arguments.container and arguments.list:
            docker.container_list()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.delete and arguments.NAME:
            docker.container_delete("{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.attach and arguments.NAME:
            docker.container_attach("{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.pause and arguments.NAME:
            status = "pause"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.unpause and arguments.NAME:
            status = "unpause"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.restart and arguments.NAME:
            status = "restart"
            docker.container_status_change("{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return


        if arguments.image and arguments.list:
            docker.images_list()
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




