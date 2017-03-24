from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.swarm_client import Swarm
import time
import os

class SwarmCommand(PluginCommand):

    @command
    def do_swarm(self, args, arguments):
        """
        ::

          Usage:
            swarm api URL
            swarm create NAME ADDR
            swarm join ADDR
            swarm leave
            swarm update
            swarm reload
            swarm node list
            swarm service create IMAGE
            swarm service list

          Arguments:
            NAME     The name of the docker swarm
            IMAGE    Docker server images
            ADDR     Swarm Address
            URL      URL of docker API

          Options:
             -v       verbose mode
   
          Description:
             Manages a virtual docker swarm on a cloud

        """
        print (arguments)

        start_time = time.time()

        if arguments.api :
            swarm = Swarm("{URL}".format(**arguments))
            print("--- %s seconds ---" % (time.time() - start_time))
            return
        #
        # TODO: I think we need to move DOCKER_HOST
        # to a yaml file and use the value read from the yaml file
        # So instead of using DOCKER HOST we explicitly add it to the
        # call via the name in the yaml file
        swarm = Swarm(os.environ["DOCKER_HOST"])
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter Swarm Node api url(eg:http://52.8.252.51:4243): ")

        if arguments.create:
            swarm.swarm_create()

        if arguments.leave:
            swarm.swarm_leave()

        if arguments.container and arguments.list:
            docker.docker_container_list()
            print("--- %s seconds ---" % (time.time() - start_time))
            return
