# -*- coding: utf-8 -*-
import io
import sys
import shutil
import json
import requests
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')

    
#Use the Tuling API to get the reply
def tuling(content):
    toPost = { "key" : "YourAPIKey" , "info" : content,"loc":"YourCity","userid":"qqqun"}
    r = requests.post("http://www.tuling123.com/openapi/api", data=toPost)
    replydata = r.json()
    #if r[code] == 100000 : return r[text]
    #else : return r[text]
    return replydata["text"]


    

    

    
class Roader:
    def __init__(self):
        with io.open("chat.json","r",encoding='utf8') as json_file:
            self.chatdict = json.load(json_file)
        with io.open("help.json","r",encoding='utf8') as json_file:
            self.helpdict = json.load(json_file)
    
    #return normal reply
    def reply(self,content,tulingbot = True):
        if "--help_all" in content:
            reply = ''
            for key in self.helpdict:
                reply = reply + '--' + key + '\t' + self.helpdict[key] + '\n'
            return reply 
        elif "--help" in content:
            reply = '--help_all\n'
            for key in self.helpdict:
                reply = reply + '--' + key + '\n'
            return reply                       
        for key in self.helpdict:
            if key in content:
                return self.helpdict[key]
        for key in self.chatdict:
            if key in content:
                return self.chatdict[key]
        if tulingbot :return tuling(content)
        return None
    
    #refresh two dict
    def refresh(self):
        with io.open("chat.json","r",encoding='utf8') as json_file:
            self.chatdict = json.load(json_file)
        with io.open("help.json","r",encoding='utf8') as json_file:
            self.helpdict = json.load(json_file)
        return "refresh done"
    

    #add rule into chat dict
    def add_chat(self,content,buddy=False):
        addflag = True
        data = {}
        lines = content.split(' ',4)
        print lines
        print lines
        if (lines[0] == '[@ME]' and lines[2] == '--addchat' and len(lines)==5) or buddy:
            for key in self.chatdict : 
                if lines[3]  == key: addflag = False
            if addflag == True :
                with codecs.open('chat.json','w','utf-8') as json_filew:
                    data =self.chatdict
                    data.update({lines[3]:lines[4]})
                    self.chatdict = data
                    data_con=dict([(k.encode('utf-8'), v.encode('utf-8')) for k, v in data.items()])
                    data_str=json.dumps(data,ensure_ascii=False).encode('utf8')
                    json_filew.write(data_str)
                    reply = 'add chat \"'+format(lines[3])+'\" : \"'+format(lines[4])+'\"'
                    return reply
            return 'Key already exists'
        return '语法错误'
    
    #add rule into help dict
    def add_help(self,content,buddy=False):
        addflag = True
        data = {}
        lines = content.split(' ',4)
        print lines
        print lines            
        if (lines[0] == '[@ME]' and lines[2] == '--addhelp' and len(lines)==5) or buddy:
            for key in self.helpdict : 
                if lines [3]  == key: addflag = False
            if addflag == True :
                with codecs.open('help.json','w','utf-8') as json_filew:
                    data = self.helpdict
                    data.update({lines[3]:lines[4]})
                    self.helpdict = data
                    data_con=dict([(k.encode('utf-8'), v.encode('utf-8')) for k, v in data.items()])
                    data_str=json.dumps(data,ensure_ascii=False).encode('utf8')
                    json_filew.write(data_str)
                    reply = 'add help \"'+format(lines[3])+'\" : \"'+format(lines[4])+'\"'
                    return reply
            return 'Key already exists'
        return '语法错误'
    
    #delete rule from help dict
    def delete_help(self,content):
        delete_flag = False
        keys_ = content.split(' ')
        keys = keys_[2:]
        for key in keys:
            if self.helpdict.has_key(key):
                del self.helpdict[key]
                delete_flag = True
        if delete_flag:
            with codecs.open('help.json','w','utf-8') as json_filew:
                data = self.helpdict
                data_con=dict([(k.encode('utf-8'), v.encode('utf-8')) for k, v in data.items()])
                data_str=json.dumps(data,ensure_ascii=False).encode('utf8')
                json_filew.write(data_str)
                reply = 'deletehelp done'
                return reply
        return 'delete nothing'
    
    #delete rule from chat dict
    def delete_chat(self,content):
        delete_flag = False
        keys_ = content.split(' ')
        keys = keys_[2:]
        for key in keys:
            if self.chatdict.has_key(key):
                del self.chatdict[key]
                delete_flag = True
        if delete_flag:
            with codecs.open('chat.json','w','utf-8') as json_filew:
                data = self.chatdict
                data_con=dict([(k.encode('utf-8'), v.encode('utf-8')) for k, v in data.items()])
                data_str=json.dumps(data,ensure_ascii=False).encode('utf8')
                json_filew.write(data_str)
                reply = 'deletechat done'
                return reply
        return 'delete nothing'


    #return the help list for the admin
    def adminhelp(self):
        reply = """--tulingoff  关闭图灵机器人(关键字检索仍有效） 
--tulingon      开启图灵机器人
--stop              关闭QQ机器人
--sleep             机器人休眠5分钟
--on                开启机器人
--restart           重启机器人
--addchat key value 增加新的chat项
--addhelp key value 增加新的help项
"""
        return reply    
          
if __name__ == '__main__':
    roader = Roader()
    re=roader.add_help('--admin 0 --addhelp key value',True)
    print(re)