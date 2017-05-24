# -*- coding: utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot
import json
import sys
import urllib
import loadjson
import time

availtime = time.time()
bot_avil = True
tulingbot = True

@qqbotslot
def onQQMessage(bot, contact, member, content):
    global availtime
    global bot_avil
    global tulingbot
    contenttype = 0
    #bot.SendTo(contact,content)
    #group admin control
    if contact.ctype == 'group':    
        if (member.role_id ==0 or member.role_id ==1) and '@ME' in content :
            if '--addhelp' in content:
                reply = loadjson.add_help(content)
                bot.SendTo(contact,reply)
                contenttype = 3
            if '--adminhelp' in content:
                reply = loadjson.adminhelp()
                bot.SendTo(contact,reply)
                contenttype = 3
            if '--tulingoff' in content:
                bot.SendTo(contact,'图灵聊天机器人已关闭')
                tulingbot = False
                contenttype = 3
            if '--tulingon' in content : 
                bot.SendTo(contact,'图灵聊天机器人已开启')
                tulingbot = True
                contenttype = 3
            if '--stop' in content : 
                bot.SendTo(contact, 'QQ机器人已关闭')
                bot_avil = False
                contenttype = 3
            if '--sleep' in content :
                bot.SendTo(contact,'QQ机器人已暂停5分钟')
                availtime = time.time() + 300
                contenttype = 3
            if '--on' in content:
                availtime = time.time()
                bot_avil = True
                contenttype = 3
            if '--restart' in content :
                bot.SendTo(contact,'正在重启')
                bot.Restart()
                contenttype = 3
            if '--kill' in content : 
                bot.SendTo(contact, 'QQ机器人已退出')
                bot.Stop()
    
    #buddy control
    if contact.ctype == 'buddy' and '--admin' in content and contenttype < 3 :
        if '--addhelp' in content:
            reply = loadjson.add_help(content,buddy=True)
            bot.SendTo(contact,reply)
            contenttype = 2
        if '--adminhelp' in content:
            reply = loadjson.adminhelp()
            bot.SendTo(contact,reply)
            contenttype = 2
        if '--tulingoff' in content:
            bot.SendTo(contact,'图灵聊天机器人已关闭')
            tulingbot = False
            contenttype = 2
        if '--tulingon' in content : 
            bot.SendTo(contact,'图灵聊天机器人已开启')
            tulingbot = True
            contenttype = 2
        if '--stop' in content : 
            bot.SendTo(contact, 'QQ机器人已关闭')
            bot_avil = False
            contenttype = 2
        if '--sleep' in content :
            bot.SendTo(contact,'QQ机器人已暂停5分钟')
            availtime = time.time() + 300
            contenttype = 2
        if '--on' in content:
            bot.SendTo(contact,'emmmmmmmm可以回来扯蛋了')
            availtime = time.time()
            bot_avil = True
            contenttype = 2
        if '--restart' in content :
            bot.SendTo(contact,'正在重启')
            bot.Restart()
            contenttype = 2
        if '--kill' in content : 
            bot.SendTo(contact, 'QQ机器人已退出')
            bot.Stop()
            
    #normal reply        
    if contact.ctype == 'buddy' or (contact.ctype == 'group' and '@ME' in content): 
        if time.time() > availtime and bot_avil and contenttype <2 :
            reply = loadjson.reply(content,tulingbot)
            if reply is not None:
                if contact.ctype == 'group':reply = '@'+member.name +" " + reply                
                bot.SendTo(contact,reply)
            
        
    # if '@ME' in content:
    #     bot.SendTo(contact, '%s， 想我了吧？' % member.name)

if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
