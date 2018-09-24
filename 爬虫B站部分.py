# -*- coding: utf-8 -*-

import re
import requests
import os
import time
import datetime

messages = []
filebags = os.path.exists('E:/BiliBili')
if not filebags:
    os.makedirs('E:/BiliBili')
os.chdir('E:/BiliBili')
url = 'https://www.bilibili.com'
while(1):
    texts = requests.get(url)
    if(texts.status_code == 200):
        contents = texts.text
        pattern = re.compile('<div class="groom-module home-card"><a href="(.*?)" target="_blank" title="(.*?)"><img.*?src="(.*?)".*?</p><p class="author">(.*?)</p><p class="play">',re.S)
        results = re.findall(pattern,contents)
        if 'temp.txt' not in os.listdir(os.getcwd()):
            file = open('temp.txt','w',encoding='utf-8')
        for message in results:
            #print('地址是:' + url + message[0] + '\n标题是:' + message[1])
            if message[0] not in messages:
                print(datetime.datetime.now()) 
                messages.append(message[0])
                with open('temp.txt','a') as f:
                    f.write('\n地址是:' + url + message[0] + '\n标题是:' + message[1] + '\n' + message[3])
    time.sleep(600)




    