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
from  cloudmesh.api.evemongo_client import perform_post ,perform_delete,perform_get

class Swarm(object):
    def __init__(self, url):
        os.environ["DOCKER_HOST"] = url
        self.client = docker.from_env()


    def host_create(self, addr, hostName=None):
        """Creates docker host


        :param str addr: Address for docker
        :param str hostName: Name of docker host
        :returns: None
        :rtype: NoneType


        """
        try:
            host = {}
            host['Name'] = hostName
            host['Ip'] = addr.split(':')[0]
            host['Port'] = int(addr.split(':')[1])
            host['Swarmmanager'] = False
            filter = {}
            filter['Ip'] = addr.split(':')[0]
            r = perform_post('Host',host,filter)
            Console.ok('Host ' + hostName + ' is Added and is the default swarm host')
        except Exception as e:
           Console.error(e.message)
           return

    def host_list(self):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
           scode,hosts = perform_get('Host')
        except Exception as e:
           Console.error(e.message)
           return
        if len(hosts) == 0:
            print("No hosts exist")
            return

        n = 1
        e = {}
        for host in hosts:
            d = {}
            d['Ip'] = str(host['Ip'])
            d['Name'] = str(host['Name'])
            d['Port'] = str(host['Port'])
            d['Swarmmanager'] = str(host['Swarmmanager'])
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Ip','Name','Port','Swarmmanager'])))


    def host_delete(self, addr):
        """Deletes docker host


        :param str addr: Address for docker
        :returns: None
        :rtype: NoneType


        """
        try:
            filter = {}
            filter['Ip'] = addr.split(':')[0]
            r = perform_delete('Host',filter)
            #Delete Host should delete all Containers and Networks for the host
            r = perform_delete('Container', filter)
            r = perform_delete('Network', filter)
            Console.ok('Host ' + addr + 'is deleted')
        except Exception as e:
           Console.error(e.message)
           return

    def create(self,kwargs=None):
        """Creates docker Swarm

        :param str addr: Address of Swarm Manager
        :param str name: Name of the Swarm
        :returns: {Manager:"",Worker:""}
        :rtype: NoneType


        """
        rcode = self.client.swarm.init(**kwargs)
        Console.ok("Swarm is created" )
        return self.client.swarm.attrs['JoinTokens']


    def leave(self,kwargs=None):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.leave(True,**kwargs)
        Console.ok("Node left Swarm" )

    def join(self,addr,type,kwargs=None):
        """Creates docker Swarm
        :param str addr: Address of Swarm Manager
        :returns: None
        :rtype: NoneType


        """
        man_list = []
        man_list.append(addr)
        savehost = os.environ["DOCKER_HOST"]
        os.environ["DOCKER_HOST"] = addr.split(':')[0] +":4243"
        self.client = docker.from_env()
        if type not in ['Manager','Worker']:
            Console.error('Valid values are Manager or Worker')
            return
        token = self.client.swarm.attrs['JoinTokens'][type]
        os.environ["DOCKER_HOST"] = savehost
        self.client = docker.from_env()
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
            d = {}
            d['Id'] = service.short_id
            d['Name'] = service.name
            e[n] = d
            n = n+1
        Console.ok(str(Printer.dict_table(e,order=['Id','Name'])))


    def service_create(self,name,image,kwargs=None):
        """List of docker images

        :param str image: Image for service
        :returns: None
        :rtype: NoneType


        """
        try:
            service = self.client.services.create(image, command=None,name=name,**kwargs)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok("Service " + name + " is created")

    def service_delete(self,name):
        """List of docker images

        :param str image: name for service
        :returns: None
        :rtype: NoneType


        """
        try:
            service = self.client.services.get(name)
            service.remove()
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok("Service " + name + " is deleted")

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
            Console.ok("Network %s is created" % network.id)
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


    def images_list(self, kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """

        try:
            scode, images = perform_get('Image')
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        if len(images) == 0:
            Console.info("No images exist")
            return

        n = 1
        e = {}
        for image in images:
            d = {}
            d['Ip'] = image['Ip']
            d['Id'] = image['Id']
            d['Repository'] = image['RepoTags'][0]
            # d['Size'] = image['Size']
            d['Size(GB)'] = round(image['Size'] / float(1 << 30), 2)  ## Converting the size to GB
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Repository', 'Size(GB)'])))


    def images_refresh(self, kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        scode, hosts = perform_get('Host')
        filter = {}
        n = 1
        e = {}
        data = []
        for host in hosts:
            os.environ["DOCKER_HOST"] = host['Ip'] + ":" + str(host['Port'])
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            self.client = docker.from_env()
            try:
                images = self.client.images.list(**kwargs)
            except docker.errors.APIError as e:
                Console.error(e.explanation)
                return

            if len(images) == 0:
                Console.info("No images exist")
                return

            for imagem in images:
                image = imagem.__dict__['attrs']
                image['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                data.append(image)
                d = {}
                d['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                d['Id'] = image['Id']
                d['Repository'] = image['RepoTags'][0]
                # d['Size'] = image['Size']
                d['Size(GB)'] = round(image['Size'] / float(1 << 30), 2)
                e[n] = d
                n = n + 1
            perform_delete('Image', filter)
        perform_post('Image', data)
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Repository', 'Size(GB)'])))

