#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
import docker
import os
#from cloudmesh.api.docker_instance import Cloudmeshdocker, Container, Images
#BUG: urllib2 is a library we should not use, use requests
#import urllib2
import requests
import json

#TODO: BUG no hardcoding of ips even during development
os.environ["DOCKER_HOST"] = 'http://52.8.252.51:4243'

# IS THERE NOT ANOTHER WAY TO SET THE HOST VIA API?
# THIS SEEMS NON SCALABLE SOLUTION TO SET os variable


client = docker.from_env()
class Docker(object):

    def docker_container_create(self, image, containerName=None, containers=None):
        """Creates docker container


        :param str image: Available images for docker 
        :param str containerName: Name of docker container
        :param int containers: Number of docker containers to be created
        :returns: None
        :rtype: NoneType


        """
        container = client.containers.create(image,name=containerName,detach=True)
        print("Container %s is created" % container.id)


    def docker_container_attach(self, containerName=None):
        """Docker container attach


        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType


        """
        try:
           container = client.containers.get(containerName)
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
            container = client.containers.get(containerName)
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
           container = client.containers.get(containerName)
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
           containers = client.containers.list(all)
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
           images = client.images.list()
        except docker.errors.APIError as e:
           print(e.explanation)
           return

        if len(images) == 0:
            print("No images exist")
            return

        print("Name")
        for image in images:
            print(str(image.tags) )

