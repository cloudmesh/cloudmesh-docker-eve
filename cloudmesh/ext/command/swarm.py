from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.swarm_client import Swarm
from cloudmesh.common.ConfigDict import ConfigDict
from cloudmesh.common.StopWatch import StopWatch
import os

class SwarmCommand(PluginCommand):

    @command
    def do_swarm(self, args, arguments):
        """
        ::

          Usage:
            swarm api URL
            swarm create NAME ADDR [ARG...]
            swarm join ADDR TOKEN [ARG...]
            swarm attrbs [ARG...]
            swarm leave [ARG...]
            swarm update [ARG...]
            swarm reload [ARG...]
            swarm service create IMAGE [ARG...]
            swarm service list
            swarm node list

          Arguments:
            NAME     The name of the docker swarm
            IMAGE    Docker server images
            ADDR     Swarm Address
            TOKEN    Worker Token to join swarm
            URL      URL of docker API

          Options:
             -v       verbose mode
   
          Description:
             Manages a virtual docker swarm on a cloud

        """
        stopwatch = StopWatch()
        stopwatch.start('E2E')

        if arguments.api :
            swarm = Swarm("{URL}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return
        #
        # TODO: I think we need to move DOCKER_HOST
        # to a yaml file and use the value read from the yaml file
        # So instead of using DOCKER HOST we explicitly add it to the
        # call via the name in the yaml file
        swarm = Swarm(os.environ["DOCKER_HOST"])
        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter Swarm Node api url(eg:http://x.x.x.x:yyyy): ")

        if arguments.create and not(arguments.service):
            out=swarm.create("{NAME}".format(**arguments),"{ADDR}".format(**arguments))
            print (out)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.attrbs:
            swarm.get_attrbs()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.leave:
            swarm.leave()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.join and arguments.ADDR and arguments.TOKEN:
            swarm.join("{ADDR}".format(**arguments),"{TOKEN}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.create:
            swarm.service_create("{IMAGE}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.list:
            swarm.service_list()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.node and arguments.list:
            swarm.node_list()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return
