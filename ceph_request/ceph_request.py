#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys,json,getopt
from os.path import expanduser
from ceph_request_exceptions import *
from http_s3_requests import s3_head, s3_delete, s3_get, s3_post, s3_put
from http_swift_requests import swift_head, swift_delete, swift_get, swift_post, swift_put

def set_configure(config_file):
    '''
    set configure
    '''
    ceph_request_config = {}
    if not os.path.exists(config_file):
        raise CEPH_REQUEST_CONFIG_FILE_NOT_EXIST
    try:
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read(config_file)
        ceph_request_config['s3_host'] = config.get('s3', 'host')
        ceph_request_config['s3_port'] = config.get('s3', 'port')
        ceph_request_config['s3_access_key'] = config.get('s3', 'access_key')
        ceph_request_config['s3_secret_key'] = config.get('s3', 'secret_key')
        ceph_request_config['swift_host'] = config.get('swift', 'host')
        ceph_request_config['swift_port'] = config.get('swift', 'port')
        ceph_request_config['swift_subuser'] = config.get('swift', 'subuser')
        ceph_request_config['swift_secret_key'] = config.get('swift', 'secret_key')
    except ConfigParser.NoSectionError, err:
        print 'Error Config File:', err
    return ceph_request_config

def usage():
    '''
    show usage
    '''
    print '''CONFIGURE FILE EXP.:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[s3]
host = 192.168.10.147
port = 8081
access_key = admin
secret_key = admin
[swift]
host = 192.168.10.147
port = 8081
subuser = admin:admin
secret_key = gA2BrFTKD3GyDd9b3FIOxDih0PRZBFda13f92GxP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-c                       set configure file. the default configure file is ~/ceph-request.cfg.
--version                get the version of ceph-request tool.
-v                       show more info of request.
-m --method              the http method. one type of [GET PUT POST DETELE HEAD]
-h --headers             set request header.   exp. --headers '{"Range": "bytes=0-10"}'
-r --request             set http request url. exp. '/' '/bucket' '/admin' '/bucket/object'
--file                   set upload file
--content                set http request body content
--download               set loal file name for download
--type                   default type is s3, you can use --type swift to sent swift request to radosgw
'''


def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hc:vm:r:",
                                      ["help", "version", "config=", "version", "method=", "request=", "headers=",
                                       "file=", "content=", "download=", "type="])
    except getopt.GetoptError as e:
        usage()
    _configure_file = expanduser("~") + '/ceph-request.cfg'
    _cmd = ''
    _method = ''
    _headers = None
    _file = None
    _content = None
    _show_dump = False
    _down_load_file = None
    _type = None
    for o, a in options:
        if o == "-v":
            _show_dump = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("--version",):
            print "version 1.0.0"
            sys.exit()
        elif o in ("-c", "--config"):
            _configure_file = a
        elif o in ("-m", "--method"):
            _method = a
        elif o in ("-r", "--request"):
            _cmd = a
        elif o in ("--headers",):
            _headers = a
        elif o in ("--file",):
            _file = a
        elif o in ("--content",):
            _content = a
        elif o in ("--download",):
            _down_load_file = a
        elif o in ("--type",):
            _type = a
        else:
            assert False, "unknow"
    try:
        ceph_request_config = set_configure(_configure_file)
    except CEPH_REQUEST_CONFIG_FILE_NOT_EXIST:
        print "PLEASE PREPARE YOUR CONFIGURE FILE"

    if str(_method).lower() == 'get':
        if str(_type).lower() == 'swift':
            swift_get(
                host=ceph_request_config['swift_host'],
                port=ceph_request_config['swift_port'],
                cmd=_cmd,
                subuser=ceph_request_config['swift_subuser'],
                secret_key=ceph_request_config['swift_secret_key'],
                headers=_headers,
                show_dump=_show_dump,
                download_file=_down_load_file
            )
        else:
            s3_get(
                host=ceph_request_config['s3_host'],
                port=ceph_request_config['s3_port'],
                cmd=_cmd,
                access_key=ceph_request_config['s3_access_key'],
                secret_key=ceph_request_config['s3_secret_key'],
                headers=_headers,
                show_dump=_show_dump,
                download_file=_down_load_file
            )

    if str(_method).lower() == 'post':
        if str(_type).lower() == 'swift':
            swift_post(
                host=ceph_request_config['swift_host'],
                port=ceph_request_config['swift_port'],
                cmd=_cmd,
                subuser=ceph_request_config['swift_subuser'],
                secret_key=ceph_request_config['swift_secret_key'],
                headers=_headers,
                file=_file,
                content=_content,
                show_dump=_show_dump
            )
        else:
            s3_post(
                host=ceph_request_config['s3_host'],
                port=ceph_request_config['s3_port'],
                cmd=_cmd,
                access_key=ceph_request_config['s3_access_key'],
                secret_key=ceph_request_config['s3_secret_key'],
                headers=_headers,
                file=_file,
                content=_content,
                show_dump=_show_dump
            )

    if str(_method).lower() == 'put':
        if str(_type).lower() == 'swift':
            swift_put(
                host=ceph_request_config['swift_host'],
                port=ceph_request_config['swift_port'],
                cmd=_cmd,
                subuser=ceph_request_config['swift_subuser'],
                secret_key=ceph_request_config['swift_secret_key'],
                headers=_headers,
                file=_file,
                content=_content,
                show_dump=_show_dump
            )
        else:
            s3_put(
                host=ceph_request_config['s3_host'],
                port=ceph_request_config['s3_port'],
                cmd=_cmd,
                access_key=ceph_request_config['s3_access_key'],
                secret_key=ceph_request_config['s3_secret_key'],
                headers=_headers,
                file=_file,
                content=_content,
                show_dump=_show_dump
            )
    if str(_method).lower() == 'delete':
        if str(_type).lower() == 'swift':
            swift_delete(
                host=ceph_request_config['swift_host'],
                port=ceph_request_config['swift_port'],
                cmd=_cmd,
                subuser=ceph_request_config['swift_subuser'],
                secret_key=ceph_request_config['swift_secret_key'],
                show_dump=_show_dump
            )
        else:
            s3_delete(
                host=ceph_request_config['s3_host'],
                port=ceph_request_config['s3_port'],
                cmd=_cmd,
                access_key=ceph_request_config['s3_access_key'],
                secret_key=ceph_request_config['s3_secret_key'],
                show_dump=_show_dump
            )
    if str(_method).lower() == 'head':
        if str(_type).lower() == 'swift':
            swift_head(
                host=ceph_request_config['swift_host'],
                port=ceph_request_config['swift_port'],
                cmd=_cmd,
                subuser=ceph_request_config['swift_subuser'],
                secret_key=ceph_request_config['swift_secret_key'],
                show_dump=_show_dump
            )
        else:
            s3_head(
                host=ceph_request_config['s3_host'],
                port=ceph_request_config['s3_port'],
                cmd=_cmd,
                access_key=ceph_request_config['s3_access_key'],
                secret_key=ceph_request_config['s3_secret_key'],
                show_dump=_show_dump
            )


if __name__ == "__main__":
    main()
