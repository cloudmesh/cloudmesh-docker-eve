from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.docker_client import Docker
import time

class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
        Usage:
            docker images list
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

        Options:

           -v       verbose mode

        """
        #print (arguments)

        start_time = time.time()

        print (arguments.container)

        if arguments.container and arguments.create and arguments.NAME and arguments.IMAGE:
            Docker().docker_container_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.start and arguments.NAME:
            status = "start"
            Docker().docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.stop and arguments.NAME:
            status = "stop"
            Docker().docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.list:
            Docker().docker_container_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.delete and arguments.NAME:
            Docker().docker_container_delete("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.attach and arguments.NAME:
            Docker().docker_container_attach("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.pause and arguments.NAME:
            status = "pause"
            Docker().docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.unpause and arguments.NAME:
            status = "unpause"
            Docker().docker_container_status_change(status, "{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.container and arguments.restart and arguments.NAME:
            status = "restart"
            Docker().docker_container_status_change("{NAME}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return

        if arguments.images and arguments.list:
            Docker().docker_images_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return


        return




