#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from os.path import expanduser
from ceph_request_exceptions import *
from http_requests import s3_head,s3_delete,s3_get,s3_post,s3_put
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import getopt


def set_configure(config_file):
    ceph_rquest_config = {}
    if not os.path.exists(config_file):
        raise CEPH_REQUEST_CONFIG_FILE_NOT_EXIST
    try:
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read(config_file)
        ceph_rquest_config['s3_host'] = config.get('s3', 'host')
        ceph_rquest_config['s3_port'] = config.get('s3', 'port')
        ceph_rquest_config['s3_access_key'] = config.get('s3', 'access_key')
        ceph_rquest_config['s3_secret_key'] = config.get('s3', 'secret_key')
    except ConfigParser.NoSectionError, err:
        print 'Error Config File:', err
    return ceph_rquest_config


def usage():
    print '''配置文件示例:
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
secret_key = admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-c 指定配置文件，默认使用用户home下的ceph-request.cfg文件
--version 版本
-v 显示详细请求
-m --method 指定发送请求类型：[GET PUT POST DETELE HEAD]
-h --header 设置请求头
-r --request 发送的url  /   /bucket   /admin   /bucket/object
--file 指定上传文件
--content 设置body体用使用字符串内容
'''

def main():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hc:vm:r:", ["help","version","config=", "version","method=","request=","header=","file=","content="])
    except getopt.GetoptError as e:
        usage()
    _configure_file = expanduser("~") + '/ceph-request.cfg'
    _cmd = ''
    _method = ''
    _header = {}
    _file = None
    _content = None
    _show_dump = False
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
            print str(a)
        elif o in ("--header",):
            _header = a
        elif o in ("--file",):
            _file = a
        elif o in ("--content",):
            _content = a
        else:
            assert False, "未知的选项"

    try:
        ceph_rquest_config = set_configure(_configure_file)
    except CEPH_REQUEST_CONFIG_FILE_NOT_EXIST:
        print "请设置好配置文件"

    if str(_method).lower() == 'get':
        s3_get(
            host=ceph_rquest_config['s3_host'],
            port=ceph_rquest_config['s3_port'],
            cmd=_cmd,
            access_key=ceph_rquest_config['s3_access_key'],
            secret_key=ceph_rquest_config['s3_secret_key'],
            show_dump=_show_dump
        )

        # if str(_method).lower() == 'post':
        #     s3_post()
        #

    if str(_method).lower() == 'put':
        s3_put(
            host=ceph_rquest_config['s3_host'],
            port=ceph_rquest_config['s3_port'],
            cmd=_cmd,
            access_key=ceph_rquest_config['s3_access_key'],
            secret_key=ceph_rquest_config['s3_secret_key'],
            headers=_header,
            file = _file,
            content= _content,
            show_dump=_show_dump
        )


    if str(_method).lower() == 'delete':
        s3_delete(
            host=ceph_rquest_config['s3_host'],
            port=ceph_rquest_config['s3_port'],
            cmd=_cmd,
            access_key=ceph_rquest_config['s3_access_key'],
            secret_key=ceph_rquest_config['s3_secret_key'],
            show_dump=_show_dump
        )

    if str(_method).lower() == 'head':
        s3_head(
            host=ceph_rquest_config['s3_host'],
            port=ceph_rquest_config['s3_port'],
            cmd=_cmd,
            access_key=ceph_rquest_config['s3_access_key'],
            secret_key=ceph_rquest_config['s3_secret_key'],
            show_dump=_show_dump
        )


if __name__ == "__main__":
    main()
