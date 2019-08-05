# coding: utf-8
import json
import requests


def ipapi(ip):
    url = 'http://api.map.baidu.com/location/ip?ip=139.214.254.47&ak=W6n6g2u9DG0RRjfqGsXZxsfnGyiYZETk&coor=bd09ll'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    r = requests.get(url, headers=headers, timeout=6)
    jsdic = json.loads(r.content)
    if jsdic.has_key('content'):
        city = jsdic['content']['address']
        pointx = jsdic['content']['point']['x']
        pointy = jsdic['content']['point']['y']
    return city, pointx, pointy


def getmap(x, y):
    im = 'http://api.map.baidu.com/staticimage/v2?ak=W6n6g2u9DG0RRjfqGsXZxsfnGyiYZETk&mcode=666666&center=' + x + ',' + y + '&width=300&height=200&zoom=11'

    return im


