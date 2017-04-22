#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
import docker
import os
import requests
import json
import ast
from cloudmesh.common.console import Console
from cloudmesh.common.Printer import Printer
from cloudmesh.api.evemongo_client import perform_post, perform_delete, perform_get


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
            host['Swarmmode'] = ''
            host['SwarmmanagerIp'] = ''
            host['Swarmhost'] = ''
            filter = {}
            filter['Ip'] = addr.split(':')[0]
            perform_delete('Host',filter)
            r = perform_post('Host', host)
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
            d['SwarmmanagerIp'] = str(host['SwarmmanagerIp'])
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Name', 'Port', 'Swarmmode','SwarmmanagerIp'])))

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
            r = perform_delete('Service', filter)
            r = perform_delete('Container', filter)
            r = perform_delete('Network', filter)
            Console.ok('Host ' + addr + 'is deleted')
        except Exception as e:
            Console.error(e.message)
            return

    def create(self, kwargs=None):
        """Creates docker Swarm

        :param str addr: Address of Swarm Manager
        :param str name: Name of the Swarm
        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.init(**kwargs)
        Console.ok("Swarm is created")
        filter = {}
        filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
        scode, hosts = perform_get('Host', filter)
        d = {}
        for host in hosts:
            d['Ip'] = host['Ip']
            d['Name'] = host['Name']
            d['Port'] = host['Port']
            d['Swarmmode'] = 'Manager'
            d['SwarmmanagerIp'] = ''
            d['Swarmhost'] = ''
        perform_post('Host',d,filter)
        self.node_refresh()


    def leave(self, kwargs=None):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """

        rcode = self.client.swarm.leave(True,**kwargs)
        filter = {}
        filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
        scode, hosts = perform_get('Host', filter)
        d ={}
        for host in hosts:
            d['Ip'] = host['Ip']
            d['Name'] = host['Name']
            d['Port'] = host['Port']
            d['Swarmmode'] = ''
            d['SwarmmanagerIp'] = ''
            d['Swarmhost'] = False
        perform_post('Host',d,filter)
        self.node_refresh()
        Console.ok("Node left Swarm" )


    def join(self, addr, type, kwargs=None):
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
        if type not in ['Manager', 'Worker']:
            Console.error('Valid values are Manager or Worker')
            return

        token = self.client.swarm.attrs['JoinTokens']
        os.environ["DOCKER_HOST"] = savehost
        self.client = docker.from_env()
        rcode = self.client.swarm.join(remote_addrs=man_list, join_token=token[type], listen_addr="0.0.0.0:2377", **kwargs)
        filter = {}
        filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
        scode, hosts = perform_get('Host', filter)
        d = {}
        for host in hosts:
            d['Ip'] = host['Ip']
            d['Name'] = host['Name']
            d['Port'] = host['Port']
            d['Swarmmode'] = type
            d['SwarmmanagerIp'] = addr.split(':')[0]
            d['Swarmhost'] = ''
        perform_post('Host', d,filter)
        self.node_refresh()
        Console.ok("Node Joined Swarm")

    def node_refresh(self):
        """Refresh of swarm nodes



        :returns: None
        :rtype: NoneType


        """
        filter = {}
        filter['Swarmmode'] = 'Manager'
        scode, hosts = perform_get('Host',filter)
        filter = {}
        n = 1
        e = {}
        data = []
        for host in hosts:
            os.environ["DOCKER_HOST"] = host['Ip'] + ":" + str(host['Port'])
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            self.client = docker.from_env()
            try:
                nodes = self.client.nodes.list()
            except docker.errors.APIError as e:
                Console.error(e.explanation)
                return
            if len(nodes) == 0:
                Console.info("No nodes exist for manager" + os.environ["DOCKER_HOST"].split(':') )
                continue

            n = 1
            e = {}
            data = []
            for node in nodes:
                d = {}
                node_dict = node.__dict__['attrs']
                d['Id'] = node_dict['ID']
                data.append(node_dict)
                d['Role'] = node_dict['Spec']['Role']
                d['Status'] = node_dict['Status']['State']
                if d['Role'] == 'manager':
                    d['Ip'] = node_dict['ManagerStatus']['Addr'].split(':')[0]
                    d['Manager Ip'] = ''
                else:
                    d['Ip'] = node_dict['Status']['Addr']
                    d['Manager Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                d['Host Name'] = node_dict['Description']['Hostname']
                e[n] = d
                n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip','Host Name','Id', 'Role', 'Status', 'Manager Ip'])))
        perform_delete('Node')
        perform_post('Node', data)

    def node_list(self, kwargs=None):
        """List of docker swarm nodes 



        :returns: None
        :rtype: NoneType


        """
        scode, nodes = perform_get('Node')
        if len(nodes) == 0:
            Console.info("No nodes exist")
            return
        n = 1
        e = {}
        data = []
        for node in nodes:
            d = {}
            node_dict = node
            d['Id'] = node_dict['ID']
            data.append(node_dict)
            d['Role'] = node_dict['Spec']['Role']
            d['Status'] = node_dict['Status']['State']
            if d['Role'] == 'manager':
                d['Ip'] = node_dict['ManagerStatus']['Addr'].split(':')[0]
                d['Manager Ip'] = ''
            else:
                d['Ip'] = node_dict['Status']['Addr']
                d['Manager Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            d['Host Name'] =  node_dict['Description']['Hostname']

            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip','Host Name','Id', 'Role', 'Status', 'Manager Ip'])))

    def service_list(self, kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        try:
            scode, services = perform_get('Service')
        # services = self.client.services.list(**kwargs)
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
            d['Ip'] = service['Ip']
            d['Id'] = service['ID']
            d['Name'] = service['Spec']['Name']
            d['Image'] = service['Spec']['TaskTemplate']['ContainerSpec']['Image']
            d['Replicas'] = service['Spec']['Mode']['Replicated']['Replicas']
            # need to see if status needs to be added.
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip','Id', 'Name', 'Image', 'Replicas'])))

    def service_refresh(self, kwargs=None):
        """List of docker images


        :returns: None
        :rtype: NoneType


        """
        filter = {}
        scode, hosts = perform_get('Host',filter)
        filter = {}
        n = 1
        e = {}
        data = []
        for host in hosts:
            os.environ["DOCKER_HOST"] = host['Ip'] + ":" + str(host['Port'])
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            self.client = docker.from_env()
            try:
                services = self.client.services.list(**kwargs)
            except docker.errors.APIError as e:
                Console.error(e.explanation)
                return

            if len(services) == 0:
                Console.info("No service exist on host" + host['Ip'])
                return

            for servicem in services:
                d = {}
                service = servicem.__dict__['attrs']
                service['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                data.append(service)
                d['Ip'] = service['Ip']
                d['Id'] = service['ID']
                d['Name'] = service['Spec']['Name']
                d['Image'] = service['Spec']['TaskTemplate']['ContainerSpec']['Image']
                d['Replicas'] = service['Spec']['Mode']['Replicated']['Replicas']
                e[n] = d
                n = n + 1
            perform_delete('Service', filter)
        perform_post('Service', data)
        Console.ok(str(Printer.dict_table(e, order=['Ip','Id', 'Name', 'Image', 'Replicas'])))

    def service_create(self, name, image, kwargs=None):
        """List of docker images

        :param str image: Image for service
        :returns: None
        :rtype: NoneType


        """
        try:
            if kwargs:
                j = {}
                ckwargs = {}
                for k in kwargs:
                    if '.' in k:
                        val = k.split('.')
                        if val[1] == 'replicas':
                            kwargs[k] = int(kwargs[k])
                        if val[0] in j:
                            j[val[0]].update({val[1]: kwargs[k]})
                        else:
                            j[val[0]] = {val[1]: kwargs[k]}
                    else:
                        ckwargs[k] = kwargs[k]

                # Mapping to complex container spec types this needs to be enhanced in future
                kwargs = ckwargs
                for t in j:
                    if t == 'ServiceMode':
                        kwargs['mode'] = docker.types.ServiceMode(**j[t])
                    if t == 'EndpointSpec':
                        kwargs['endpoint_spec'] = docker.types.EndpointSpec(ports={9200: 9200, 9300: 9300})
            service = self.client.services.create(image, command=None, name=name, **kwargs)
            data = []
            data.append(service.attrs)
            data[0]['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            perform_post('Service', data)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok("Service " + name + " is created")

    def service_delete(self, name):
        """List of docker images

        :param str name: name for service
        :returns: None
        :rtype: NoneType


        """
        try:
            service = self.client.services.get(name)
            service.remove()
            filter = {}
            filter['ID'] = service.id
            filter['Name'] = service.name
            filter['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            perform_delete('Service', filter)
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok("Service " + name + " is deleted")

    def network_create(self, networkName=None, kwargs=None):
        """Creates docker network


        :param str image: Available images for docker
        :param str networkName: Name of docker container
        :param list arg: custom args for container
        :returns: str networkID: Id of the docker Container
        :rtype: NoneType


        """
        try:
            ipam_pool = docker.types.IPAMPool(
                subnet='10.0.10.0/24'
            )
            ipam_config = docker.types.IPAMConfig(
                pool_configs=[ipam_pool])
            Options = {"encrypted": ""}
            network = self.client.networks.create(name=networkName, options=Options, ipam=ipam_config, **kwargs)
            data = []
            network_dict = network.__dict__['attrs']
            network_dict['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
            data.append(network_dict)
            perform_post('Network', data)
            Console.ok("Network %s is created" % network.id)
            # perform_post('Network',network.__dict__['attrs'])
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
            d['Ip'] = network['Ip']
            d['Id'] = network['Id']
            d['Name'] = network['Name']
            d['Containers'] = network['Containers']
            e[n] = d
            n = n + 1
        Console.ok(str(Printer.dict_table(e, order=['Ip','Id', 'Name', 'Containers'])))

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
            if image['RepoTags'] == None:
                d['Repository'] = image['RepoDigests'][0]
            else:
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
        filter = {}
        scode, hosts = perform_get('Host',filter)
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
                Console.info("No images exist on host " + host['Ip'])
                continue

            for imagem in images:
                image = imagem.__dict__['attrs']
                image['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                data.append(image)
                d = {}
                d['Ip'] = os.environ["DOCKER_HOST"].split(':')[0]
                d['Id'] = image['Id']
                if image['RepoTags'] == None:
                    d['Repository'] = image['RepoDigests'][0]
                else:
                    d['Repository'] = image['RepoTags'][0]
                # d['Size'] = image['Size']
                d['Size(GB)'] = round(image['Size'] / float(1 << 30), 2)
                e[n] = d
                n = n + 1
            perform_delete('Image', filter)
        perform_post('Image', data)
        Console.ok(str(Printer.dict_table(e, order=['Ip', 'Id', 'Repository', 'Size(GB)'])))

    def network_refresh(self, kwargs=None):
        """List of docker networks


        :returns: None
        :rtype: NoneType


        """
        filter = {}
        scode, hosts = perform_get('Host',filter)
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
        filter = {}
        scode, hosts = perform_get('Host',filter)
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
                return
            if len(containers) == 0:
                print("No containers exist" + str(host['Ip']))
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

    def network_delete(self, name):
        """List of docker images

        :param str name: name for network
        :returns: None
        :rtype: NoneType


        """
        try:
            network = self.client.networks.get(name)
            network.remove()
        except docker.errors.APIError as e:
            Console.error(e.explanation)
            return

        Console.ok("Network " + name + " is deleted")
