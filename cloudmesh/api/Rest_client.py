import sys

import json
import random
import requests

class Rest(object):
    @classmethod
    def post(cls,resource, data, filter=None):
        headers = {'Content-Type': 'application/json'}
        if filter:
            scode, datao = cls.get(resource, filter)
            if len(datao) > 0:
                return cls.put(resource, data, filter)
        datastr = json.dumps(data, indent=4).replace('.', '\uff0E')
        r = requests.post(cls.endpoint(resource), datastr, headers=headers)
        return r

    @classmethod
    def get(cls,resource, filter=None):
        if filter:
            url = cls.endpoint(resource) + "?where=" + json.dumps(filter).replace('\uff0e', '.')
        else:
            url = cls.endpoint(resource)
        headers = {'Content-Type': 'application/json'}
        out = requests.get(url, headers=headers)
        datastr = out.text.replace('\uff0e', '.')
        scode, datam = out.status_code, json.loads(datastr)['_items']
        return scode, datam

    @classmethod
    def delete(cls,resource, filter=None):
        if filter:
            url = cls.endpoint(resource) + "?where=" + json.dumps(filter).replace('\uff0e', '.')
            headers = {'Content-Type': 'application/json'}
            out = requests.get(url, headers=headers)
            if len(json.loads(out.text)['_items']) > 0:
                for item in json.loads(out.text)['_items']:
                    headers['If-Match'] = item['_etag']
                    url = cls.endpoint(resource)+item['_id']
                    out = requests.delete(url,headers=headers)

        else:
            url = cls.endpoint(resource)
            out = requests.delete(url)
        return out

    @classmethod
    def put(cls,resource, data, filter):
        if filter:
            url = cls.endpoint(resource) + "?where=" + json.dumps(filter).replace('\uff0e', '.')
        else:
            url = cls.endpoint(resource)
        headers = {'Content-Type': 'application/json'}
        out = requests.get(url, headers=headers)
        if len(json.loads(out.text)['_items']) > 0:
            headers['If-Match'] = json.loads(out.text)['_items'][0]['_etag']
            url = cls.endpoint(resource) + json.loads(out.text)['_items'][0]['_id']
            datastr = json.dumps(data, indent=4).replace('.', '\uff0E')
            out = requests.put(url, datastr, headers=headers)
        return out

    @classmethod
    def endpoint(cls,resource):
        ENTRY_POINT = 'localhost:5000'
        return 'http://%s/%s/' % (
            ENTRY_POINT, resource)


if __name__ == '__main__':
    with open('../../config/restjson/all.json') as data_file:
        data = json.load(data_file)
    for j in data:
        r = Rest.delete(j)
        '''
        print ('Delete : ' + str(j) + "-" + str(r.status_code))
        r = post(j, data[j])
        print ('Insert : ' + str(j) + "-" + str(r.status_code))
        status_code, data1 = get(j)
        print ('Get : ' + str(j) + "-" + str(status_code))
        print (data1)
        filter = {}
        print (data[j])
        if 'ID' in data[j].keys():
            key = 'ID'
        else:
            key = 'Id'
        filter[key] = data[j][key]
        status_code, data1 = get(j, filter)
        print ('Get Where : ' + str(j) + "-" + str(status_code))
        print (data1)
        r = put(j, data[j], filter)
        print ('Update : ' + str(j) + "-" + str(r.status_code))
        break
        '''
