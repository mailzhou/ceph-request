def s3_get(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key=''):
    '''
    get request use aws2
    '''
    import requests
    from requests_toolbelt.utils import dump
    from awsauth import S3Auth
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.get(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    data = dump.dump_all(response)
    print(data.decode('utf-8'))


# TODO ADD POST METHOD
def s3_post(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key=''):
    pass

# TODO ADD HEADER AND DATA SUPPORDED
def s3_put(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key='',headers=None,file=None,content=None):
    '''
    put request use aws2
    '''
    import requests
    from requests_toolbelt.utils import dump
    from awsauth import S3Auth
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
    data = dump.dump_all(response)
    print(data.decode('utf-8'))


def s3_delete(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key=''):
    '''
    delete request use aws2
    '''
    import requests
    from requests_toolbelt.utils import dump
    from awsauth import S3Auth
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.delete(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    data = dump.dump_all(response)
    print(data.decode('utf-8'))

def s3_head(host='127.0.0.1', port='7480', cmd='/', access_key='', secret_key=''):
    '''
    head request use aws2
    '''
    import requests
    from requests_toolbelt.utils import dump
    from awsauth import S3Auth
    url = 'http://%s:%s%s' % (host,port,cmd)
    response = requests.head(url, auth=S3Auth(access_key, secret_key, service_url=host+":"+port))
    data = dump.dump_all(response)
    print(data.decode('utf-8'))