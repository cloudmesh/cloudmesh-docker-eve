import sys

import json
import random
import requests





def post_Image():
    Image = [
        {
            "Created": 1491793422,
            "Labels": {},
            "VirtualSize": 728281564,
            "SharedSize": -1,
            "ParentId": "",
            "Size": 728281564,
            "RepoDigests": [
                "karvenka/cloudmesh.docker@sha256:cab75f19406238aa0f416a4f164a53c086f19c278ee5f5c948e7f6ec9d34421b"
            ],
            "Key": "sha256:e5458e538e295080fa58b8c80cc6c6bcba3a41ad2a2fa7491d75f2df51446c0a",
            "Id": "sha256:e5458e538e295080fa58b8c80cc6c6bcba3a41ad2a2fa7491d75f2df51446c0a",
            "Containers": -1,
            "RepoTags": [
                "karvenka/cloudmesh.docker:latest"
            ]
        },
        {
            "Created": 1491594492,
            "Labels": {},
            "VirtualSize": 834628884,
            "SharedSize": -1,
            "ParentId": "",
            "Size": 834628884,
            "RepoDigests": [
                "karvenka/esrally@sha256:f70a58d3027d23afe26b8e6a48fa0531b89ee1d3140477aec07f0d2beaecd7b6"
            ],
            "Key": "sha256:f6a8b681665ae0efcfc14fbf77598bd2d9ddfb26816ed662cad41d994749d301",
            "Id": "sha256:f6a8b681665ae0efcfc14fbf77598bd2d9ddfb26816ed662cad41d994749d301",
            "Containers": -1,
            "RepoTags": [
                "karvenka/esrally:latest"
            ]
        },
        {
            "Created": 1490829254,
            "Labels": {},
            "VirtualSize": 679374422,
            "SharedSize": -1,
            "ParentId": "",
            "Size": 679374422,
            "RepoDigests": [
                "docker.elastic.co/kibana/kibana@sha256:1742ebbebde5b037ff53a0e4edefb11c75d3b9575c28ab84f5c68b272e4d3cb4"
            ],
            "Key": "sha256:8ff89f3e84fb7cbbe96dfd849851c304297d41f1ec3aadd10d05e597b2cde3c2",
            "Id": "sha256:8ff89f3e84fb7cbbe96dfd849851c304297d41f1ec3aadd10d05e597b2cde3c2",
            "Containers": -1,
            "RepoTags": [
                "docker.elastic.co/kibana/kibana:5.3.0"
            ]
        }
    ]

    r = perform_post('Image', json.dumps(Image))
    print "'Image' posted", r.status_code

    valids = []
    if r.status_code == 201:
        response = r.json()
        if response['_status'] == 'OK':
            for Image in response['_items']:
                if Image['_status'] == "OK":
                    valids.append(Image['_id'])

    return valids


def post_works(ids):
    works = []
    for i in range(28):
        works.append(
            {
                'title': 'Book Title #%d' % i,
                'description': 'Description #%d' % i,
                'owner': random.choice(ids),
            }
        )

    r = perform_post('works', json.dumps(works))
    print "'works' posted", r.status_code


def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    print(data)
    return requests.post(endpoint(resource), json.dumps(data), headers=headers)

def perform_get(resource, data=None):
    headers = {}
    return requests.get(endpoint(resource)+data,  headers=headers)

def delete():
    r = perform_delete('Image')
    print "'Image' deleted", r.status_code



def perform_delete(resource):
    print (resource)
    return requests.delete(endpoint(resource))


def endpoint(resource):
    ENTRY_POINT = 'localhost:5000'
    return 'http://%s/%s/' % (
        ENTRY_POINT , resource)


if __name__ == '__main__':
    #delete()
    #ids = post_Image()
    #post_works(ids)
    out = perform_get('Image',"sha256:8ff89f3e84fb7cbbe96dfd849851c304297d41f1ec3aadd10d05e597b2cde3c2")
    print (out.url,out.text)