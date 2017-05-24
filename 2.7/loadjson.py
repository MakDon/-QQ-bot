# -*- coding: utf-8 -*-
import io
import sys
import shutil
import json
import requests
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')
        
def tuling(content):
    toPost = { "key" : "your_key_here" , "info" : content,"loc":"your_location","userid":"qqqun"}
    r = requests.post("http://www.tuling123.com/openapi/api", data=toPost)
    replydata = r.json()
    #if r[code] == 100000 : return r[text]
    #else : return r[text]
    return replydata["text"]

def adminhelp():
    reply = """--tulingoff  关闭图灵机器人(关键字检索仍有效） 
--tulingon      开启图灵机器人
--stop              关闭QQ机器人
--sleep             机器人休眠5分钟
--on                开启机器人
--restart           重启机器人
--addhelp key value 增加新的help项
"""
    return reply
    
def add_help(content,buddy=False):
    addflag = True
    data = {}
    lines = content.split(' ',4)
    print lines
    if (lines[0] == '[@ME]' and lines[2] == '--addhelp' and len(lines)==5) or buddy:
        with io.open('help.json','r',encoding='utf-8') as json_file:
            data =json.load(json_file)
            for key in data : 
               if lines [3]  == key: addflag = False
        if addflag == True :
            with codecs.open('help.json','w','utf-8') as json_filew:
               data.update({lines[3]:lines[4]})
               print data
               data_con=dict([(k.encode('utf-8'), v.encode('utf-8')) for k, v in data.items()])
               print data_con
               data_str=json.dumps(data,ensure_ascii=False).encode('utf8')
               print data_str
               print type(data_str)
               json_filew.write(data_str)
               reply = 'add help \"'+format(lines[3])+'\" : \"'+format(lines[4])+'\"'
               return reply
        return 'Key already exists'
    return '语法错误'
    

def reply(content,tulingbot = True):
    #content.encode('utf8')
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
    if tulingbot :return tuling(content)

#else
#========================================
    return None
    
if __name__ == '__main__':
    re=add_help('--admin 0 --addhelp key value',True)
    print(re)