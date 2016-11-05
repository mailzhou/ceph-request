import requests
from requests_toolbelt.utils import dump
from .awsauth import S3Auth
def s3_get(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',show_dump = False):
    '''
    get request use aws2
    '''
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.get(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content


# TODO ADD POST METHOD
def s3_post(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',show_dump = False):
    pass

# TODO ADD HEADER AND DATA SUPPORDED
def s3_put(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',headers=None,file=None,content=None,show_dump = False):
    '''
    put request use aws2
    '''
    url = 'http://%s:%s%s' % (host, port, cmd)
    response =None
    if file:
        with open(file, 'rb') as fin:
            file_content = fin.read()

        response = requests.put(url, auth=S3Auth(access_key, secret_key, service_url=host + ":" + port),
                                    headers=headers, data=file_content)

    elif content:
        print url
        print content
        response = requests.put(url, auth=S3Auth(access_key, secret_key, service_url=host + ":" + port),
                                headers=headers, data=content)
    else:
        response = requests.put(url, auth=S3Auth(access_key, secret_key, service_url=host + ":" + port),
                                headers=headers)
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content


def s3_delete(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',show_dump = False):
    '''
    delete request use aws2
    '''
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.delete(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content

def s3_head(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',show_dump = False):
    '''
    head request use aws2
    '''
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.head(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    if show_dump:
        data = dump.dump_all(response)
        print(data.decode('utf-8'))
    else:
        print response.content
