import requests
from requests_toolbelt.utils import dump
import json
from ceph_request_exceptions import *

def swift_auth(serverurl,subuser=None,secret_key=None):
    if subuser and secret_key:
        cmd = '/auth/1.0'
        url = 'http://%s%s' % (serverurl,cmd)
        headers = {'x-auth-key':secret_key,'x-auth-user':subuser}
        response = requests.get(url,headers=headers)
        return response.headers['X-Auth-Token']
    else:
        raise CEPH_REQUEST_SWIFT_TYPE_CONFIG_NOT_RIGHT

def swift_get(host='127.0.0.1', port='7480', cmd='/', subuser='', secret_key='',headers=None,show_dump = False,download_file =None):
    '''
    swift get
    '''
    url = 'http://%s:%s%s' % (host,port,cmd)
    serverurl = '%s:%s' % (host,port)
    X_Auth_Token = swift_auth(serverurl,subuser=subuser,secret_key=secret_key)

    if headers:
        headers = json.loads(headers)
        headers['x-auth-token'] = X_Auth_Token
    else:
        headers = {'x-auth-token': X_Auth_Token}

    if download_file:
        import shutil
        response = requests.get(url,stream=True,headers=headers)
        if response.status_code == 200 or response.status_code == 206:
            with open(download_file, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
    else:
        response = requests.get(url,headers=headers)

    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content


# TODO ADD POST METHOD
def swift_post(host='127.0.0.1', port='7480', cmd='/',subuser='', secret_key='',show_dump = False):
    '''
    swift post
    '''
    url = 'http://%s:%s%s' % (host, port, cmd)
    serverurl = '%s:%s' % (host, port)
    X_Auth_Token = swift_auth(serverurl, subuser=subuser, secret_key=secret_key)

    if headers:
        headers = json.loads(headers)
        headers['x-auth-token'] = X_Auth_Token
    else:
        headers = {'x-auth-token': X_Auth_Token}
    response = None
    if file:
        with open(file, 'rb') as fin:
            file_content = fin.read()
        # upload object from file
        response = requests.post(url, headers=headers, data=file_content)
    elif content:
        # upload object from content
        response = requests.post(url, headers=headers, data=content)
    else:
        # create bucket
        response = requests.post(url, headers=headers)
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content

# TODO ADD HEADER AND DATA SUPPORDED
def swift_put(host='127.0.0.1', port='7480', cmd='/', subuser='', secret_key='',headers=None,file=None,content=None,show_dump = False):
    '''
    swift put
    '''
    url = 'http://%s:%s%s' % (host, port, cmd)
    serverurl = '%s:%s' % (host, port)
    X_Auth_Token = swift_auth(serverurl, subuser=subuser, secret_key=secret_key)

    if headers:
        headers = json.loads(headers)
        headers['x-auth-token'] = X_Auth_Token
    else:
        headers = {'x-auth-token': X_Auth_Token}
    response =None
    if file:
        with open(file, 'rb') as fin:
            file_content = fin.read()
        #upload object from file
        response = requests.put(url, headers=headers, data=file_content)
    elif content:
        #upload object from content
        response = requests.put(url, headers=headers, data=content)
    else:
        # create bucket
        response = requests.put(url,headers=headers)
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content

def swift_delete(host='127.0.0.1', port='7480', cmd='/', subuser='', secret_key='',show_dump = False):
    '''
    swift delete
    '''
    url = 'http://%s:%s%s' % (host, port, cmd)
    serverurl = '%s:%s' % (host, port)
    X_Auth_Token = swift_auth(serverurl, subuser=subuser, secret_key=secret_key)
    headers = {'x-auth-token': X_Auth_Token}
    response = requests.delete(url, headers=headers)
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content

def swift_head(host='127.0.0.1', port='7480', cmd='/', subuser='', secret_key='',show_dump = False):
    '''
    swift head
    '''
    url = 'http://%s:%s%s' % (host, port, cmd)
    serverurl = '%s:%s' % (host, port)
    X_Auth_Token = swift_auth(serverurl, subuser=subuser, secret_key=secret_key)
    headers = {'x-auth-token': X_Auth_Token}
    response = requests.head(url, headers=headers)
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content