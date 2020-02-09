#!/usr/bin/env python3

# coding: utf-8

"""Permit to obtain real ip when using cloudflare in front of nginx."""

import datetime
import json
import subprocess

import urllib3

CFG_FILE = '/etc/nginx/cloudflare.conf'

urllib3.disable_warnings()
HTTP = urllib3.PoolManager()
REQUEST = HTTP.urlopen(method='GET',
                       url='https://api.cloudflare.com/client/v4/ips',
                       preload_content=False)
DATA = REQUEST.data.decode('utf-8')

JSON_BODY = json.loads(DATA)

IPV4 = ';\n'.join('set_real_ip_from ' + str(x)
                  for x in JSON_BODY['result']['ipv4_cidrs'])
IPV6 = ';\n'.join('set_real_ip_from ' + str(y)
                  for y in JSON_BODY['result']['ipv6_cidrs'])

IPV4_NGINX = (IPV4 + ';')
IPV6_NGINX = (IPV6 + ';')

with open(CFG_FILE, 'w') as text_file:
    print('# Created : ' + str(datetime.datetime.now()) +
          '\n\n# IPv4\n' + IPV4_NGINX +
          '\n\n# IPv6\n' + IPV6_NGINX +
          '\nreal_ip_header CF-Connecting-IP;', file=text_file)

subprocess.call(['service', 'nginx', 'reload'])
