import base64
import requests
from fake_useragent import UserAgent
from contextlib import closing
from tools import ip
import random
bs64 = input("请输入迅雷下载地址：")
bs64.encode('utf-8')
# thunder://QUFodHRwOi8venVpZGEuZG93bnp1aWRhLmNvbS8xOTEyL1lXNO+8muWujOe7k+evhy5UQ+a4heaZsOeJiC5tcDRaWg==
while True:
    if bs64[0] == " ":
        bs64.replace(" ", "")
        continue
    else:
        break
bs64 = bs64[10:]
jiemi = base64.b64decode(bs64)
jiemi = jiemi.decode('utf-8')
jiemi = jiemi[2:len(jiemi)-2]
print("获取到迅雷原始连接为：" + jiemi)
ip.main()
c = []
with open('ip.txt', 'r') as fi:
    l = fi.read().split(" ")
    c.append(l)
c = c[0]
proxies = {
        'https': random.choice(c)
    }
ua = UserAgent()
headers = {
    "User-Agent": str(ua.random),
}
response = requests.get(jiemi, headers=headers, proxies=proxies)
print(response.status_code)
with open(jiemi, "wb") as mv:
    print(response.status_code)
    mv.write(response.content)


