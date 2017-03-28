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

    def create(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.init()
        print("Swarm is created" )

    def leave(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.leave(True)
        print("Node left Swarm" )

    def node_list(self):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
            nodes = self.client.nodes.list(all)
        except docker.errors.APIError as e:
            print(e.explanation)
            return
        if len(nodes) == 0:
            print("No containers exist")
            return

        print("Name\t\tImage\t\tStatus")
        for node in nodes:
            print(node.name + "\t\t" + str((node.attrs)))

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
