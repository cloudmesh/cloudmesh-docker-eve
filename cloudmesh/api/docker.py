#!/usr/bin/env python
# Docker class to connect to docker server box and perform docker operations
from __future__ import print_function
import cloudmesh
from cloudmesh_docker.api.docker_instance import Cloudmeshdocker, Container, Images
from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from cloudmesh.cm_mongo import cm_mongo
import urllib2
import requests
import json

username = cloudmesh.load().username()
#mesh = cloudmesh.mesh("mongo")
# mesh.activate(username)
#cm = cm_mongo("docker")
#get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)


class Docker(object):

    def docker_container_create(self, image, containerName=None, containers=None):
        """Creates docker container


        :param str image: Available images for docker 
        :param str containerName: Name of docker container
        :param int containers: Number of docker containers to be created
        :returns: None
        :rtype: NoneType


        """
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("Cloud is not defined yet")
            return

        for server in dockerserverobjs:
            dockerserver = server.dockerserver

        dockerserverurl = "http://%s:4243" % dockerserver

        postUrl = "%s/containers/create" % dockerserverurl
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        payload = {"Hostname": "",
                   "User": "",
                   "Memory": 0,
                   "MemorySwap": 0,
                   "AttachStdin": 'true',
                   "AttachStdout": 'true',
                   "AttachStderr": 'true',
                   "PortSpecs": 'null',
                   "Privileged": 'false',
                   "Tty": 'false',
                   "OpenStdin": 'true',
                   "StdinOnce": 'true',
                   "Env": 'null',
                   "Dns": 'null',
                   "Volumes": '{}',
                   "VolumesFrom": "",
                   "WorkingDir": ""}
        payload["Image"] = str(image)
        if containerName is not None:
            postUrl += "?name=%s" % containerName
            resp = requests.post(
                url=postUrl, data=json.dumps(payload), headers=headers)
            data = json.loads(resp.text)
            print("Container %s is created" % containerName)
            Container(containerName=containerName, containerImage=str(
                image), containerId=data['Id'], containerStatus="created").save()

    def docker_container_attach(self, containerName=None):
        """Docker container attach


        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType


        """
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("Cloud is not defined yet")
            return

        for server in dockerserverobjs:
            dockerserver = server.dockerserver

        dockerserverurl = "http://%s:4243" % dockerserver
        containerInfo = Container.objects.get(containerName=containerName)
        if len(containerInfo) == 0:
            print("Container does not exist")
            return

        postUrl = "%s/containers/%s/attach?logs=1&stream=0&stdout=1" % (
            dockerserverurl, containerInfo.containerId)
        resp = requests.post(url=postUrl)

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

        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("Cloud is not defined yet")
            return

        for server in dockerserverobjs:
            dockerserver = server.dockerserver

        dockerserverurl = "http://%s:4243" % dockerserver
        containerInfo = Container.objects.get(containerName=containerName)
        if len(containerInfo) == 0:
            print("Container does not exist")
            return

        postUrl = "%s/containers/%s/%s" % (dockerserverurl,
                                           containerInfo.containerId, status)
        resp = requests.post(url=postUrl)

        if status is "unpause" or status is "start":
            status = "running"

        containerInfo.update(set__containerStatus=status)

    def docker_container_delete(self, containerName=None):
        """Deleting docker container
        

        :param str containerName: Name of docker container
        :returns: None
        :rtype: NoneType

        
        """
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("Cloud is not defined yet")
            return

        for server in dockerserverobjs:
            dockerserver = server.dockerserver

        dockerserverurl = "http://%s:4243" % dockerserver
        containerInfo = Container.objects.get(containerName=containerName)
        if len(containerInfo) == 0:
            print("Container does not exist")
            return

        deleteUrl = "%s/containers/%s?v=1" % (
            dockerserverurl, containerInfo.containerId)
        resp = requests.delete(url=deleteUrl)

        # Delete from database
        containerInfo.delete()

    def docker_container_list(self):
        """List of docker containers


        :returns: None
        :rtype: NoneType


        """
        containers = Container.objects()
        if len(containers) == 0:
            print("No containers exist")
            return

        print("Name\t\tStatus")
        for container in containers:
            print(container.containerName + "\t\t" + container.containerStatus)

    def docker_service_start(self, cloud):
        """Starting docker cloud service


        :param str cloud: Name of cloud where docker server is deployed
        :returns: None
        :rtype: NoneType


        """
        ##
        # TODO: Add support for more clouds
        ##
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) != 0:
            self.docker_service_cloud_delete()

        print("Starting Docker Service...")

        dockerserverurl = "http://%s:4243" % cloud

        # LIST IMAGES
        postUrl = "%s/images/json" % dockerserverurl
        payload = {}
        resp = requests.get(url=postUrl)
        data = json.loads(resp.text)
        print("Listing Available Images....")
        if len(data) == 0:
            print("No images found on docker server")
            return

        for imageData in data:
            images = imageData["RepoTags"]
            for image in images:
                Images(imageName=image, imageId=imageData[
                       "Id"], imageSize=str(imageData["Size"])).save()
                print(image)

        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            Cloudmeshdocker(dockerserver=cloud).save()
            return

        for server in dockerserverobjs:
            if str(server.dockerserver) == cloud:
                print("Cloud already exist")
                return

        Cloudmeshdocker(dockerserver=cloud).save()

    def docker_images_list(self):
        """List of docker images
        
        
        :returns: None
        :rtype: NoneType


        """
        images = Images.objects()
        if len(images) == 0:
            print("No images exist")
            return

        for image in images:
            print(image.imageName)

    def docker_service_cloud_list(self):
        """List the docker clouds


        :returns: None
        :rtype: NoneType


        """
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("No cloud exist yet")
            return

        print("Listing existing cloud..")
        for server in dockerserverobjs:
            print(server.dockerserver)

    def docker_service_cloud_delete(self, cloud=None):
        """Deletes docker cloud


        :param str cloud: Name of docker cloud
        :returns: None
        :rtype: NoneType


        """
        dockerserverobjs = Cloudmeshdocker.objects()
        if len(dockerserverobjs) == 0:
            print("No cloud to remove")
            return

        for server in dockerserverobjs:
            server.delete()

        images = Images.objects()
        for image in images:
            image.delete()
