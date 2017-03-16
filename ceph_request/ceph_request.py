#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
  ceph-request get    <uri>  [-c|--conf=<kn>] [--header=<kn>] [--download=<kn>] [--type=<kn>] [--verbose]
  ceph-request put    <uri>  [-c|--conf=<kn>] [--header=<kn>] [--file=<kn>] [--content=<kn>] [--type=<kn>] [--verbose]
  ceph-request post   <uri>  [-c|--conf=<kn>] [--header=<kn>] [--file=<kn>] [--content=<kn>] [--type=<kn>] [--verbose]
  ceph-request head   <uri>  [-c|--conf=<kn>] [--header=<kn>] [--type=<kn>] [--verbose]
  ceph-request delete <uri>  [-c|--conf=<kn>] [--type=<kn>] [--verbose]
  ceph-request (-h | --help)
  ceph-request --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  -c --conf=<kn>    Speed in knots [default: ~/ceph-request.cfg].
  --header=<kn>     Set header.
  --download=<kn>   Download.
  --file=<kn>       Upload file.
  --content=<kn>    Upload content
  --type=<kn>       Type;
  --verbose         More.

"""

from docopt import docopt
from os.path import expanduser
from http_s3_requests import s3_head, s3_delete, s3_get, s3_post, s3_put
from http_swift_requests import swift_head, swift_delete, swift_get, swift_post, swift_put

def get_configure(config_file):
    ceph_request_config = {}
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

def main(args):
    _configure_file =  expanduser("~") + '/ceph-request.cfg' if args['--conf'] is None else args['--conf'][0]
    _cmd = args['<uri>']
    _headers = args['--header']
    _file = args['--file']
    _content = args['--content']
    _show_dump = args['--verbose']
    _down_load_file = args['--download']
    _type = args['--type']

    print _configure_file,_cmd,_headers,_file,_content,_show_dump,_down_load_file,_type

    ceph_request_config = get_configure(_configure_file)
    if args['get']:
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
    if args['post']:
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
    if args['put']:
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
    if args['delete']:
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
    if args['head']:
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

if __name__ == '__main__':
    arguments = docopt(__doc__, version='ceph-request 2.0')
    main(arguments)