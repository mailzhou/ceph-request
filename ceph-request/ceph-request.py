#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from os.path import expanduser
from ceph_request_exceptions import *
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import getopt


def set_configure(config_file):
    ceph_rquest_config = {}
    logger.info('START CHECK IF CONFIGURE FILE EXIST')
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
    print '''
    usage: -c --config  : default ~/ceph-request.cfg

    '''



def main():
    try:
        options, args = getopt.getopt(sys.argv[1:],"hc:v", ["help","config=","version"])
    except getopt.GetoptError as e:
        usage()
    _configure_file = expanduser("~") + '/ceph-request.cfg'
    for o, a in options:
        if o == "-v":
            print "version 1.0.0"
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", "--config"):
            _configure_file = a
        else:
            assert False, "unhandled option"
    print args

    try:
        ceph_rquest_config = set_configure(_configure_file)
        print '__host__', ceph_rquest_config['s3_host']
    except CEPH_REQUEST_CONFIG_FILE_NOT_EXIST:
        print "please configure your file"



if __name__ == "__main__":
    main()
