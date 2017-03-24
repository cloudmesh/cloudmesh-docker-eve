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

    def swarm_create(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.init()
        print("Swarm is created" )

    def swarm_leave(self):
        """Creates docker Swarm

        :returns: None
        :rtype: NoneType


        """
        rcode = self.client.swarm.leave(True)
        print("Node left Swarm" )

    def docker_container_create(self, image, containerName=None, containers=None):
        """Creates docker container


        :param str image: Available images for docker 
        :param str containerName: Name of docker container
        :param int containers: Number of docker containers to be created
        :returns: None
        :rtype: NoneType


        """
        container = self.client.containers.create(image,name=containerName,detach=True)
        print("Container %s is created" % container.id)


    def docker_container_attach(self, containerName=None):
        """Docker container attach


        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType


        """
        try:
           container = self.client.containers.get(containerName)
           resp = container.attach()
        except docker.errors.APIError as e:
           print(e.explanation)
           return

    def docker_container_status_change(self, status=None, containerName=None):
        """Change status of docker container

        :param str status: Docker container status to be changed to
        :param str containerName: Name of Docker container
        :returns: None
        :rtype: NoneType


        """
        if status is None:
            print("No status specified")
            return

        try:
            container = self.client.containers.get(containerName)
            if status is "start" :
                container.start()
            elif status is "pause":
                container.pause()
            elif status is "unpause":
                container.unpause()
            elif status is "stop":
                container.stop()
            else:
                print ('Invalid Commmand')
                return
        except docker.errors.APIError as e:
            print(e.explanation)
            return




    def docker_container_delete(self, containerName=None):
        """Deleting docker container
        

        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType

        
        """
        try:
           container = self.client.containers.get(containerName)
           container.remove()
        except docker.errors.APIError as e:
           print(e.explanation)
           return

    def docker_container_list(self):
        """List of docker containers



        :returns: None
        :rtype: NoneType


        """
        try:
           containers = self.client.containers.list(all)
        except docker.errors.APIError as e:
           print(e.explanation)
           return
        if len(containers) == 0:
            print("No containers exist")
            return

        print("Name\t\tImage\t\tStatus")
        for container in containers:
            print(container.name + "\t\t" + str((container.attrs)['Config']['Image']) + "\t\t" + container.status)

    def docker_images_list(self):
        """List of docker images
        
        
        :returns: None
        :rtype: NoneType


        """
        try:
           images = self.client.images.list()
        except docker.errors.APIError as e:
           print(e.explanation)
           return

        if len(images) == 0:
            print("No images exist")
            return

        print("Name")
        for image in images:
            print(str(image.tags) )

