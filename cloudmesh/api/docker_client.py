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
from cloudmesh.api.evemongo_client import perform_post, perform_delete, perform_get
import time


class Docker(object):
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
            host['Swarmmode'] = ''
            host['SwarmmanagerIp'] = ''
            host['Swarmhost'] = False
            filter = {}
            filter['Ip'] = addr.split(':')[0]
            r = perform_post('Host', host, filter)
            Console.ok('Host ' + hostName + ' is Added and is the default host')
        except Exception as e:
            Console.error(e.message)
            return

    def host_list(self):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
            scode, hosts = perform_get('Host')
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
            d['Swarmmode'] = str(host['Swarmmode'])
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Name', 'Port', 'Swarmmode'])))

    def host_delete(self, addr):
        """Deletes docker host


        :param str addr: Address for docker
        :returns: None
        :rtype: NoneType


        """
        try:
            filter = {}
            filter['Ip'] = addr.split(':')[0]
            r = perform_delete('Host', filter)
            # Delete Host should delete all Containers and Networks for the host
            r = perform_delete('Container', filter)
            r = perform_delete('Network', filter)
            Console.ok('Host ' + addr + ' is deleted')
        except Exception as e:
            Console.error(e.message)
            return

    def container_create(self, image, containerName=None, kwargs=None):
        """Creates docker container


        :param str image: Available images for docker 
        :param str containerName: Name of docker container
        :param list arg: custom args for container
        :returns: str containeID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            container = self.client.containers.create(image, name=containerName, detach=True, **kwargs)
            data = []
            container_dict = container.__dict__['attrs']
            container_dict['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            # container_dict['State']['StartedAt'] = time.asctime(time.localtime(time.time()))
            data.append(container_dict)
            perform_post('Container', data)
            Console.ok('Container ' + container.name + ' is Created')
            return container.id
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

    def container_run(self, image, containerName=None, kwargs=None):
        """Creates docker container


        :param str image: Available images for docker
        :param str containerName: Name of docker container
        :param list arg: custom args for container
        :returns: str containeID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            container = self.client.containers.run(image, name=containerName, detach=True, **kwargs)
            Console.ok("Container %s is created" % container.id)
            data = []
            container_dict = container.__dict__['attrs']
            container_dict['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            # container_dict['State']['StartedAt'] = time.asctime(time.localtime(time.time()))
            data.append(container_dict)
            perform_post('Container', data)
            Console.ok('Container ' + container.name + ' is Started')
            return container.id
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

    def container_status_change(self, status=None, containerName=None, kwargs=None):
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
            # need to check this ..
            if status is "start":
                container.start(**kwargs)
            elif status is "pause":
                container.pause(**kwargs)
            elif status is "unpause":
                container.unpause(**kwargs)
            elif status is "stop":
                container.stop(**kwargs)
            else:
                Console.error('Invalid Commmand')
                return

            container = self.client.containers.get(containerName)
            filter = {}
            container_dict = container.__dict__['attrs']
            filter['Id'] = container_dict['Id']
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            container_dict['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            perform_post('Container', container_dict, filter)
            Console.ok('Container ' + container.name + ' status changed to ' + status)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

    def container_delete(self, containerName=None, kwargs=None):
        """Deleting docker container
        

        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType

        
        """
        try:
            container = self.client.containers.get(containerName)
            container.remove(**kwargs)
            filter = {}
            filter['Id'] = container.__dict__['attrs']['Id']
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            perform_delete('Container', filter)
            Console.ok('Container ' + container.name + ' is deleted')
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

    def container_list(self, kwargs=None):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
            scode, containers = perform_get('Container')
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return
        if len(containers) == 0:
            print("No containers exist")
            return

        n = 1
        e = {}
        for container in containers:
            d = {}
            d['Ip'] = container['Ip']
            d['Id'] = container['Id']
            d['Name'] = container['Name']
            d['Image'] = container['Config']['Image']
            d['Status'] = container['State']['Status']
            d['StartedAt'] = container['State']['StartedAt']
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Name', 'Image', 'Status', 'StartedAt'])))

    def container_refresh(self, kwargs=None):
        """List of docker containers



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
            self.client = docker.from_env()
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            try:
                containers = self.client.containers.list(all, **kwargs)
            except docker.errors.APIError as e:
                Console.error(e.explanation)
                perform_delete('Container', filter)
                continue
            if len(containers) == 0:
                print("No containers exist " + str(host['Ip']))
                perform_delete('Container', filter)
                continue

            for containerm in containers:
                container = containerm.__dict__['attrs']
                container['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                data.append(container)
                d = {}
                d['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                d['Id'] = container['Id']
                d['Name'] = container['Name']
                d['Image'] = container['Config']['Image']
                d['Status'] = container['State']['Status']
                d['StartedAt'] = container['State']['StartedAt']
                e[n] = d
                n = n + 1
            perform_delete('Container', filter)
        perform_post('Container', data)
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Name', 'Image', 'Status', 'StartedAt'])))

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
            d['Size(GB)'] = round(image['Size'] / float(1 << 30), 2)  # Converting the size to GB
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

    def network_create(self, networkName=None, kwargs=None):
        """Creates docker network


        :param str image: Available images for docker
        :param str networkName: Name of docker container
        :param list arg: custom args for container
        :returns: str networkID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            network = self.client.networks.create(name=networkName, **kwargs)
            data = []
            network_dict = network.__dict__['attrs']
            network_dict['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            data.append(network_dict)
            perform_post('Network', data)
            Console.ok("Network %s is created" % network.Name)
            return network.id
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

    def network_list(self, kwargs=None):
        """List of docker networks


        :returns: None
        :rtype: NoneType


        """
        try:
            scode, networks = perform_get('Network')
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
            d = {}
            d['Ip'] = network['Ip']
            d['Id'] = network['Id']
            d['Name'] = network['Name']
            d['Containers'] = network['Containers']
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Name', 'Containers'])))

    def network_refresh(self, kwargs=None):
        """List of docker networks


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
                networks = self.client.networks.list(**kwargs)
            except docker.errors.APIError as e:
                Console.error(e.explanation)
                continue

            if len(networks) == 0:
                Console.info("No network exist" + host['Ip'])
                continue

            for networkm in networks:
                network = networkm.__dict__['attrs']
                network['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                data.append(network)
                d = {}
                d['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                d['Id'] = network['Id']
                d['Name'] = network['Name']
                d['Containers'] = network['Containers']
                e[n] = d
                n = n + 1
            r = perform_delete('Network', filter)
        r = perform_post('Network', data)
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Name', 'Containers'])))

    def process_config(self):
        Config = ConfigDict("docker.yaml",
                            verbose=True, load_order=[r'/home/ubuntu/git/cloudmesh.docker/config'])
        Console.ok(Config['docker'])
