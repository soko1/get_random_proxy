#!/usr/bin/env python3

import random

PROXY_LIST='/Users/user/git/proxy-list/proxies_geolocation/socks5.txt'

f = open(PROXY_LIST, 'r')
proxies = f.readlines()
lines = len(proxies)
line_number = random.randrange(0,lines)

(IP, port) = proxies[line_number].split(":")[0:2]

proxy = IP + ':' + port

print(proxy)


