from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.docker_client import Docker
import time
import os

class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
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

        Manages a virtual docker on a cloud

        Arguments:

          NAME     The name of the docker
          CLOUD    The name of the cloud on which the virtual docker
                   is to be deployed
          IMAGE    Docker server images
          URL      URL of docker API

        Options:

           -v       verbose mode

        """
        #print (arguments)
        # TODO: we have a module stop watch that we could
        # introduce into common form cloudmesh client. I can do that
        # today
        start_time = time.time()


        if arguments.api :
            docker = Docker("{URL}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return
        docker = Docker(os.environ["DOCKER_HOST"])
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker api url(eg:http://52.8.252.51:4243): ")

        if arguments.container and arguments.create and arguments.NAME and arguments.IMAGE:
            docker.docker_container_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.start and arguments.NAME:
            status = "start"
            docker.docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.stop and arguments.NAME:
            status = "stop"
            docker.docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        if arguments.container and arguments.list:
            docker.docker_container_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.delete and arguments.NAME:
            docker.docker_container_delete("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.attach and arguments.NAME:
            docker.docker_container_attach("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.pause and arguments.NAME:
            status = "pause"
            docker.docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.unpause and arguments.NAME:
            status = "unpause"
            docker.docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.restart and arguments.NAME:
            status = "restart"
            docker.docker_container_status_change("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        if arguments.image and arguments.list:
            # TODO: makebe get rid of docker_ and cange images to image I think
            # thats what they do in openstack. Lets compare openstack if it is
            # images list or image list and flavors list or flavor list
            
            docker.docker_images_list()
            # Whe have a module stopwatch that we may want to move to common. I can do that today
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        return




