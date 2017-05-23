# -*- coding: utf-8 -*-
import io
import shutil
import json
import requests

def tuling(content):
    toPost = { "key" : "87c0a2ff1e76486db23151c6d4174ac6" , "info" : content,"loc":"广州市","userid":"qqqun"}
    r = requests.post("http://www.tuling123.com/openapi/api", data=toPost)
    replydata = r.json()
    #if r[code] == 100000 : return r[text]
    #else : return r[text]
    return replydata["text"]



def reply(content):
    content.encode('utf8')
#help here ,--help would return the help list
#===========================================
    with io.open("help.json","r",encoding='utf8') as json_file:
        data = json.load(json_file)
        if "--help" in content:
            reply = ''
            for key in data:
                reply = '--' + key + '\n'
            return reply
        for key in data:
            if key in content:
                return data[key]         
#chat here,--help would not return the list
#====================================                
    with io.open("chat.json","r",encoding='utf8') as json_file:
        data = json.load(json_file)
        for key in data:
            if key in content:
                return data[key]
        
#tuling here
#=========================================
    return tuling(content)

#else
#========================================
    return None
    
if __name__ == '__main__':
    #re=reply('今天的天气')
    print(re)