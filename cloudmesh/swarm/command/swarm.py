from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.api.swarm_client import Swarm
from cloudmesh.common.ConfigDict import ConfigDict
from cloudmesh.common.StopWatch import StopWatch
import os
import ast


class SwarmCommand(PluginCommand):
    @command
    def do_swarm(self, args, arguments):
        """
        ::

          Usage:
            swarm host list
            swarm host delete ADDR
            swarm host NAME ADDR
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

        """

        kwargs = {}
        if arguments.ARG:
            for j in arguments.ARG:
                kwargs[j.split('=', 1)[0].strip()] = j.split('=', 1)[1].strip()
                val = j.split('=', 1)[1].strip()
                print(val)
                if '[' in j.split('=', 1)[1].strip():
                    val = val.replace('[', '').replace(']', '').split(',')
                    kwargs[j.split('=', 1)[0].strip()] = val


        stopwatch = StopWatch()
        stopwatch.start('E2E')
        Base = ConfigDict('cloudmesh_cmd5.yaml',
                          verbose=False)
        os.environ["DOCKER_HOST"] = Base['cloudmesh']['container']['docker']['work']['host']
        if arguments.host and arguments.list:
            swarm = Swarm(os.environ["DOCKER_HOST"])
            swarm.host_list()
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host and arguments.delete:
            swarm = Swarm(os.environ["DOCKER_HOST"])
            swarm.host_delete("{ADDR}".format(**arguments))
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.host:
            swarm = Swarm("{ADDR}".format(**arguments))
            swarm.host_create("{ADDR}".format(**arguments), "{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            Base['cloudmesh']['container']['docker']['work']['host'] = "{ADDR}".format(**arguments)
            Base.save()
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if "DOCKER_HOST" not in os.environ:
            os.environ["DOCKER_HOST"] = raw_input("Please enter docker swarm api host(IP or Name : Port )")

        swarm = Swarm(os.environ["DOCKER_HOST"])

        if arguments.network and arguments.create and arguments.NAME:
            swarm.network_create("{NAME}".format(**arguments), kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.create and not (arguments.service):
            swarm.create(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.leave:
            swarm.leave(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.join and arguments.ADDR and arguments.TYPE:
            swarm.join("{ADDR}".format(**arguments), "{TYPE}".format(**arguments), kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.create:
            swarm.service_create("{NAME}".format(**arguments), "{IMAGE}".format(**arguments), kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.list:
            swarm.service_list(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.refresh:
            swarm.service_refresh(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.service and arguments.delete:
            swarm.service_delete("{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.node and arguments.list:
            swarm.node_list(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.node and arguments.refresh:
            swarm.node_refresh()
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.list:
            swarm.network_list(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.refresh:
            swarm.network_refresh(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.image and arguments.list:
            swarm.images_list(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.image and arguments.refresh:
            swarm.images_refresh(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.list:
            swarm.container_list(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.container and arguments.refresh:
            swarm.container_refresh(kwargs)
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return

        if arguments.network and arguments.delete:
            swarm.network_delete("{NAME}".format(**arguments))
            stopwatch.stop('E2E')
            print('Time Taken:' + str(stopwatch.get('E2E')))
            return
