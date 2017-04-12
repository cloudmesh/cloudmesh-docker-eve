#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
import docker
import os
import requests
import json
import sys
from cloudmesh.common.console import Console
from cloudmesh.common.Printer import Printer
import json
from  cloudmesh.api.evemongo_client import perform_post ,perform_delete

class Docker(object):
    def __init__(self, url):
        os.environ["DOCKER_HOST"] = url
        self.client = docker.from_env()

    def container_create(self, image, containerName=None, kwargs=None):
        """Creates docker container


        :param str image: Available images for docker 
        :param str containerName: Name of docker container
        :param list arg: custom args for container
        :returns: str containeID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            container = self.client.containers.create(image,name=containerName,detach=True,**kwargs)
            Console.ok("Container %s is created" % container.id)
            return container.id
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return

    def container_attach(self, containerName=None,kwargs=None):
        """Docker container attach


        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType


        """
        try:
           container = self.client.containers.get(containerName)
           resp = container.attach(**kwargs)
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return

    def container_status_change(self, status=None, containerName=None,kwargs=None):
        """Change status of docker container

        :param str status: Docker container status to be changed to
        :param str containerName: Name of Docker container
        :returns: None
        :rtype: NoneType


        """
        if status is None:
            Console.info("No status specified")
            return

        try:
            container = self.client.containers.get(containerName)
            if status is "start" :
                container.start(**kwargs)
            elif status is "pause":
                container.pause(**kwargs)
            elif status is "unpause":
                container.unpause(**kwargs)
            elif status is "stop":
                container.stop(**kwargs)
            else:
                Console.error ('Invalid Commmand')
                return
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return




    def container_delete(self, containerName=None,kwargs=None):
        """Deleting docker container
        

        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType

        
        """
        try:
           container = self.client.containers.get(containerName)
           container.remove(**kwargs)
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return

    def container_list(self,kwargs=None):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
           containers = self.client.containers.list(all,**kwargs)
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return
        if len(containers) == 0:
            print("No containers exist")
            return

        n = 1
        e = {}
        data = []
        for container in containers:
            data.append(json.dumps (container.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = container.short_id
            d['Name'] = container.name
            d['Image'] = str((container.attrs)['Config']['Image'])
            d['Status'] = container.status
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Name','Image','Status'])))

    def container_refresh(self,kwargs=None):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
           containers = self.client.containers.list(all,**kwargs)
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return
        if len(containers) == 0:
            print("No containers exist")
            return

        n = 1
        e = {}
        data = []
        for container in containers:
            data.append(json.dumps (container.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = container.short_id
            d['Name'] = container.name
            d['Image'] = str((container.attrs)['Config']['Image'])
            d['Status'] = container.status
            e[n] = d
            n = n+1
        perform_delete('Container')
        perform_post('Container',data)
        Console.ok(str(Printer.dict_table(e,order=['Id','Name','Image','Status'])))

    def images_list(self,kwargs=None):
        """List of docker images
        
        
        :returns: None
        :rtype: NoneType


        """
        try:
           images = self.client.images.list(**kwargs)
        except docker.errors.APIError as e:
           Console.error(e.explanation)
           return

        if len(images) == 0:
            Console.info("No images exist")
            return

        n = 1
        e = {}
        data = []
        for image in images:
            data.append(json.dumps(image.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = image.short_id
            d['Repository'] = image.tags[0]
            d['Size'] = image.attrs['Size']
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Repository','Size'])))

    def images_refresh(self, kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        try:
            images = self.client.images.list(**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        if len(images) == 0:
            Console.info("No images exist")
            return

        n = 1
        e = {}
        data = []
        for image in images:
            data.append(json.dumps(image.__dict__['attrs'], indent=4))
            d = {}
            d['Id'] = image.short_id
            d['Repository'] = image.tags[0]
            d['Size'] = image.attrs['Size']
            e[n] = d
            n = n + 1
        perform_delete('Image')
        print ('After Delete')
        perform_post('Image',data)
        Console.ok(str(Printer.dict_table(e, order=['Id', 'Repository', 'Size'])))


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
        data = []
        for network in networks:
            data.append(json.dumps(network.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = network.short_id
            d['Name'] = network.name
            d['Containers'] = network.containers
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Name','Containers'])))

    def network_refresh(self,kwargs=None):
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
        data = []
        for network in networks:
            data.append(json.dumps(network.__dict__['attrs'],indent=4))
            d = {}
            d['Id'] = network.short_id
            d['Name'] = network.name
            d['Containers'] = network.containers
            e[n] = d
            n = n+1
        perform_delete('Network')
        perform_post('Network',data)
        Console.ok(str(Printer.dict_table(e,order=['Id','Name','Containers'])))


    def process_config(self):
        Config =  ConfigDict("docker.yaml",
                   verbose=True,load_order=[r'/home/ubuntu/git/cloudmesh.docker/config'])
        Console.ok (Config['docker'])

