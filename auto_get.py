import requests
import json
import warnings
import base64

import string

# warnings.filterwarnings('ignore')

def sendRequest():
    confUrl = "https://api.buliang0.cf/opconf.json"
    try:
        response = requests.get(confUrl)
    except Exception:
        print("网络请求出错了……")
    return response.json().get("data").get("items")[0].get("items")

def createSubscribe():
    list = sendRequest()
    result = ""
    for item in list:
        ovpnItem = item.get("ovpn")
        ovpn = base64.b64decode(ovpnItem)
        ovpn = str(ovpn,'utf8')
        # text = unquote(ovpn, 'utf-8')
        # text = quote(text, 'utf-8')
        result += _removeMarkName(ovpn) + "\n"

    # subscribe = result.strip('|')
    print(result)
    result = base64.b64encode(result.encode())
    result = str(result, 'utf8')
    print("\n")
    print(result)
    _write2File(result)

# 移除特定的名称标记
def _removeMarkName(node):
    print('原节点：' + node)
    newNode = ''
    if node.startswith('vmess://'):
        newNode = str(base64.b64decode(node[8:]), 'utf8')
        newNode = newNode.replace('(Youtube:不良林)', '')
        newNode = 'vmess://' + str(base64.b64encode(newNode.encode()), 'utf8')
    else:
        newNode = node.replace('%28Youtube%3A%E4%B8%8D%E8%89%AF%E6%9E%97%29', '')
    return newNode

def _write2File(subscribe):
    with open('sub.txt', 'w') as fobj:
        fobj.write(subscribe)
createSubscribe()