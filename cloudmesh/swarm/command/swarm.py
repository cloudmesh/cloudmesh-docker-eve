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
            swarm host list
            swarm host delete ADDR
            swarm host NAME ADDR
            swarm create NAME ADDR [ARG...]
            swarm join ADDR TOKEN [ARG...]
            swarm attrbs [ARG...]
            swarm leave [ARG...]
            swarm update [ARG...]
            swarm reload [ARG...]
            swarm network create IMAGE [ARG...]
            swarm network list [ARG...]
            swarm service create IMAGE [ARG...]
            swarm service list
            swarm node list

          Arguments:
            NAME     The name of the docker swarm
            IMAGE    Docker server images
            ADDR     Swarm Address
            TOKEN    Worker Token to join swarm
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
            swarm = Swarm(os.environ["DOCKER_HOST"])
            swarm.host_list()
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host and arguments.delete:
            swarm = Swarm(os.environ["DOCKER_HOST"])
            swarm.host_delete("{ADDR}".format(**arguments))
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host :
            swarm = Swarm("{ADDR}".format(**arguments))
            swarm.host_create("{ADDR}".format(**arguments),"{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            Base['cloudmesh']['container']['docker']['work']['host'] = "{ADDR}".format(**arguments)
            Base.save()
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker swarm api host(IP or Name : Port )")

        swarm = Swarm(os.environ["DOCKER_HOST"])


        if arguments.create and not(arguments.service):
            out=swarm.create("{NAME}".format(**arguments),"{ADDR}".format(**arguments),kwargs)
            print (out)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.attrbs:
            swarm.get_attrbs(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.leave:
            swarm.leave(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.join and arguments.ADDR and arguments.TOKEN:
            swarm.join("{ADDR}".format(**arguments),"{TOKEN}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.create:
            swarm.service_create("{IMAGE}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.list:
            swarm.service_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.node and arguments.list:
            swarm.node_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.create and arguments.NAME and arguments.IMAGE:
            swarm.network_create("{IMAGE}".format(**arguments), "{NAME}".format(**arguments),kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.list:
            swarm.network_list(kwargs)
            stopwatch.stop('E2E')
            print ('Time Taken:' + str(stopwatch.get('E2E')))
            return