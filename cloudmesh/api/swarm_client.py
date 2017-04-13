#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
import docker
import os
import requests
import json
from cloudmesh.common.console import Console
from cloudmesh.common.Printer import Printer

class Swarm(object):
    def __init__(self, url):
        os.environ["DOCKER_HOST"] = url
        self.client = docker.from_env()

    def create(self,name,addr,kwargs=None):
        """Creates docker Swarm

        :param str addr: Address of Swarm Manager
        :param str name: Name of the Swarm
        :returns: {Manager:"",Worker:""}
        :rtype: NoneType


        """
        rcode = self.client.swarm.init(name=name,listen_addr=addr,advertise_addr =None,**kwargs)
        Console.ok("Swarm is created" )
        return self.client.swarm.attrs['JoinTokens']

    def get_attrbs(self,kwargs=None):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        Console.ok(self.client.swarm.attrs,**kwargs)

    def leave(self,kwargs=None):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.leave(True,**kwargs)
        Console.ok("Node left Swarm" )

    def join(self,addr,token,kwargs=None):
        """Creates docker Swarm
        :param str addr: Address of Swarm Manager
        :returns: None
        :rtype: NoneType


        """
        man_list = []
        man_list.append(addr)
        rcode = self.client.swarm.join(remote_addrs =man_list,join_token =token,listen_addr = "0.0.0.0:2377",**kwargs)
        Console.ok("Node Joined Swarm" )

    def node_list(self,kwargs=None):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
            nodes = self.client.nodes.list(**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return
        if len(nodes) == 0:
            Console.info("No nodes exist")
            return

        n = 1
        e = {}
        for node in nodes:
            print(json.dumps(node.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = node.short_id
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id'])))

    def service_list(self,kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        try:
            services = self.client.services.list(**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        if len(services) == 0:
            Console.info("No Services exist")
            return

        n = 1
        e = {}
        for service in services:
            print(json.dumps(service.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = service.short_id
            d['Name'] = service.name
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Name'])))


    def service_create(self,image,kwargs=None):
        """List of docker images

        :param str image: Image for service
        :returns: None
        :rtype: NoneType


        """
        try:
            service = self.client.services.create(image, command=None,**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok(str(service))

    def network_create(self, image, networkName=None, kwargs=None):
        """Creates docker network


        :param str image: Available images for docker
        :param str networkName: Name of docker container
        :param list arg: custom args for container
        :returns: str networkID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            network = self.client.networks.create(image,name=networkName,detach=True,**kwargs)
            Console.ok("Container %s is created" % network.id)
            return network.id
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return

    def network_list(self,kwargs=None):
        """List of docker networks


        :returns: None
        :rtype: NoneType


        """
        try:
            networks = self.client.networks.list(**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        if len(networks) == 0:
            Console.info("No network exist")
            return

        n = 1
        e = {}
        for network in networks:
            d = {}
            d['Id'] = network.short_id
            d['Name'] = network.name
            d['Containers'] = network.containers
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Name','Containers'])))
