# -*- coding: utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import sys
import urllib
import loadjson
import time

availtime = time.time()

@qqbotslot
def onQQMessage(bot, contact, member, content):
    global availtime
    #group admin control
    if contact.ctype == 'group':    
        if member.role_id ==0 or member.role_id ==1 :
            if 'stop' in content : 
                bot.SendTo(contact, 'QQ机器人已关闭')
                bot.Stop()
            if 'sleep' in content :
                bot.SendTo(contact,'QQ机器人已暂停5分钟')
                availtime = time.time() + 300
            if 'restart' in content :
                bot.Restart()
    
    #buddy control
    if contact.ctype == 'buddy' and content == 'stopadmin':
            bot.SendTo(contact, 'QQ机器人已关闭')
            bot.Stop()
    if contact.ctype == 'buddy' and content == 'restartadmin':
            bot.SendTo(contact, 'QQ机器人重启')
            bot.Restart()
            
    #normal reply        
    if contact.ctype == 'buddy' or (contact.ctype == 'group' and '@ME' in content): 
        if time.time() > availtime :
            reply = loadjson.reply(content)
            if reply is not None:
                bot.SendTo(contact,reply)
            
        
    # if '@ME' in content:
    #     bot.SendTo(contact, '%s， 想我了吧？' % member.name)
    '''
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    '''
if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
