#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
import docker
import os
#from cloudmesh.api.docker_instance import Cloudmeshdocker, Container, Images
import requests
import json

class Swarm(object):
    def __init__(self, url):
        os.environ["DOCKER_HOST"] = url
        self.client = docker.from_env()

    def create(self,name,addr):
        """Creates docker Swarm

        :param str addr: Address of Swarm Manager
        :param str name: Name of the Swarm
        :returns: {Manager:"",Worker:""}
        :rtype: NoneType


        """
        rcode = self.client.swarm.init(name=name,listen_addr=addr,advertise_addr =None)
        print("Swarm is created" )
        return self.client.swarm.attrs['JoinTokens']

    def get_attrbs(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        print(self.client.swarm.attrs)

    def leave(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.leave(True)
        print("Node left Swarm" )

    def join(self,addr,token):
        """Creates docker Swarm
        :param str addr: Address of Swarm Manager
        :returns: None
        :rtype: NoneType


        """
        man_list = []
        man_list.append(addr)
        rcode = self.client.swarm.join(remote_addrs =man_list,join_token =token,listen_addr = "0.0.0.0:2377")
        print("Node Joined Swarm" )

    def node_list(self):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
            print("I am here")
            nodes = self.client.nodes.list()
            print (nodes)
        except docker.errors.APIError as e:
            print(e.explanation)
            return
        if len(nodes) == 0:
            print("No nodes exist")
            return

        for node in nodes:
            print(str(node.attrs['Status']['State']))

    def service_list(self):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        try:
            services = self.client.services.list()
        except docker.errors.APIError as e:
            print(e.explanation)
            return

        if len(services) == 0:
            print("No Services exist")
            return

        print("Name")
        for service in services:
            print(str(service))


    def service_create(self,image):
        """List of docker images

        :param str image: Image for service
        :returns: None
        :rtype: NoneType


        """
        try:
            service = self.client.services.create(image, command=None)
        except docker.errors.APIError as e:
            print(e.explanation)
            return

        print(str(service))

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
            print("Container %s is created" % network.id)
            return network.id
        except docker.errors.APIError as e:
           print(e.explanation)
           return

    def network_list(self,kwargs=None):
        """List of docker networks


        :returns: None
        :rtype: NoneType


        """
        try:
            networks = self.client.networks.list(kwargs)
        except docker.errors.APIError as e:
            print(e.explanation)
            return

        if len(networks) == 0:
            print("No network exist")
            return

        print("Id")
        for network in networks:
            print(str(network.id))
