import sys

import json
import random
import requests





def post_Image():
    Image=[]
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



def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(resource), json.dumps(data), headers=headers)

def perform_get(resource):
    headers = {'Content-Type': 'application/json'}
    out =  requests.get(endpoint(resource),  headers=headers)
    return out.status_code,json.loads(out.text)['_items']

def perform_get_where(resource,filter):
    headers = {'Content-Type': 'application/json'}
    url = endpoint(resource) + "?where="+json.dumps(filter)
    out =  requests.get(url,  headers=headers)
    return out.status_code,json.loads(out.text)['_items']

def perform_delete(resource):
    return requests.delete(endpoint(resource))


def endpoint(resource):
    ENTRY_POINT = 'localhost:5000'
    return 'http://%s/%s/' % (
        ENTRY_POINT , resource)


if __name__ == '__main__':
    with open('../../restjson/all.json') as data_file:
        data = json.load(data_file)
    for j in data:
        r = perform_delete(j)
        print ('Delete : ' + str(j) + "-" + str(r.status_code))
        r = perform_post(j,data[j])
        print ('Insert : ' + str(j) + "-" + str(r.status_code))
        status_code,data1 = perform_get(j)
        print ('Get : ' + str(j) + "-" + str(status_code))
        print (data1)
        filter ={}
        print (data[j])
        filter['ID'] = data[j]["ID"]
        status_code, data1 = perform_get_where(j, filter)
        print ('Get Where : ' + str(j) + "-" + str(status_code))
        print (data1)