from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.docker_client import Docker
import time
import os
from cloudmesh.common.ConfigDict import ConfigDict

class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
        ::

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
            docker process config

  
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

        """
        #print (arguments)
        # TODO: we have a module stop watch that we could use. it is now in common
        start_time = time.time()


        if arguments.api :
            docker = Docker("{URL}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return
        docker = Docker(os.environ["DOCKER_HOST"])
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker api url(eg:http://x.x.x.x:yyyy): ")

        if arguments.container and arguments.create and arguments.NAME and arguments.IMAGE:
            docker.container_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.start and arguments.NAME:
            status = "start"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.stop and arguments.NAME:
            status = "stop"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        if arguments.container and arguments.list:
            docker.container_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.delete and arguments.NAME:
            docker.container_delete("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.attach and arguments.NAME:
            docker.container_attach("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.pause and arguments.NAME:
            status = "pause"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.unpause and arguments.NAME:
            status = "unpause"
            docker.container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.restart and arguments.NAME:
            status = "restart"
            docker.container_status_change("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        if arguments.image and arguments.list:
            docker.images_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.process and arguments.config:
            Config = ConfigDict("docker.yaml",
                                verbose=True, load_order=[r'/home/ubuntu/git/cloudmesh.docker/config'])
            print(Config['docker'])
            docker = Docker(Config['docker']['host'])
            docker.container_create(Config['docker']['container']['Image'])
            return




