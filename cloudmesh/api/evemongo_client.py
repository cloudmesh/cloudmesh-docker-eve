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



def perform_post(resource, data,filter=None):
    headers = {'Content-Type': 'application/json'}
    print(json.dumps(data,indent=4))
    if filter:
        scode,datao = perform_get(resource, filter)
        if len(datao) > 0:
            return perform_put(resource,data,filter)
    r = requests.post(endpoint(resource), json=data, headers=headers)
    if r.status_code > 399:
        print(r.json)
    return r

def perform_get(resource,filter=None):
    if filter:
        url = endpoint(resource) + "?where=" + json.dumps(filter)
    else:
        url = endpoint(resource)
    headers = {'Content-Type': 'application/json'}
    out =  requests.get(url,  headers=headers)
    scode,datam = out.status_code, json.loads(out.text)['_items']
    return scode,datam

def perform_delete(resource,filter=None):
    if filter:
        url = endpoint(resource) + "?where=" + json.dumps(filter)
    else:
        url = endpoint(resource)
    r = requests.delete(url)
    print(r)
    return r

def perform_put(resource,data,filter):
    if filter:
        url = endpoint(resource) + "?where=" + json.dumps(filter)
    else:
        url = endpoint(resource)
    headers = {'Content-Type': 'application/json'}
    out =  requests.get(url,  headers=headers)
    print(out.text)
    if '_items' in json.loads(out.text).keys():
        headers['If-Match'] = json.loads(out.text)['_items'][0]['_etag']
        url = endpoint(resource)+json.loads(out.text)['_items'][0]['_id']
        out = requests.put(url,json.dumps(data),headers=headers)
    return out

def endpoint(resource):
    ENTRY_POINT = 'localhost:5000'
    return 'http://%s/%s/' % (
        ENTRY_POINT , resource)


if __name__ == '__main__':
    with open('../../config/restjson/all.json') as data_file:
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
        if 'ID' in data[j].keys():
            key = 'ID'
        else:
            key = 'Id'
        filter[key] = data[j][key]
        status_code, data1 = perform_get(j, filter)
        print ('Get Where : ' + str(j) + "-" + str(status_code))
        print (data1)
        r=perform_put(j,data[j],filter)
        print ('Update : ' + str(j) + "-" + str(r.status_code))
        break