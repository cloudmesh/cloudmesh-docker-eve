from __future__ import print_function
from cloudmesh_client.shell.command import command
from cloudmesh_client.shell.command import PluginCommand


class DockerCommand(PluginCommand):

    @command
    def do_docker(self, args, arguments):
        """
        Usage:
            docker service start CLOUD
            docker service cloud list
            docker service cloud delete
            docker container create NAME IMAGE
            docker container start NAME
            docker container stop NAME
            docker container list
            docker container delete NAME
            docker container attach NAME
            docker container pause NAME
            docker container unpause NAME
            docker images list

        Manages a virtual docker on a cloud

        Arguments:

          NAME     The name of the docker
          CLOUD    The name of the cloud on which the virtual docker
                   is to be deployed
          IMAGE    Docker server images

        Options:

           -v       verbose mode

        """
        print(arguments)



