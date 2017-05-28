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
contenttype = 0
roader = loadjson.Roader()

#the Commands
def commands(bot,contact,member,content,permit,type=99):
    global availtime
    global bot_avil 
    global tulingbot
    global contenttype    if not permit[0]:reply = "permission denied"
        else : reply = roader.refresh()
        bot.SendTo(contact,reply)
        contenttype = type
        
    #add rule into chat dict
    if '--addchat' in content:
        if not permit[0]:reply = "permission denied"
        else : reply = roader.add_chat(content)
        bot.SendTo(contact,reply)
        contenttype = type
    
    #add rule into help dict
    if '--addhelp' in content:
        if not permit[1]:reply = "permission denied"
        else : reply = roader.add_help(content)
        bot.SendTo(contact,reply)
        contenttype = type
    
    #delete rule from chat dict by key
    if '--deletechat' in content:
        if not permit[2]:reply = "permission denied"
        else : reply = roader.delete_chat(content)
        bot.SendTo(contact,reply)
        contenttype = type
    
    #delete rule from help dict by key
    if '--deletehelp' in content:
        if not permit[3]:reply = "permission denied"
        else : reply = roader.delete_help(content)
        bot.SendTo(contact,reply)
        contenttype = type
    
    #show the help list for admin
    if '--adminhelp' in content:
        if not permit[4]:reply = "permission denied"
        else : reply = roader.adminhelp()
        bot.SendTo(contact,reply)
        contenttype = type
    
    #turn off the Tuling bot(help and chat rules still available
    if '--tulingoff' in content:
        if not permit[5]:reply = "permission denied"
        else : bot.SendTo(contact,'图灵聊天机器人已关闭')
        tulingbot = False
        contenttype = type
    
    #turn on the Tuling bot
    if '--tulingon' in content : 
        if not permit[6]:reply = "permission denied"
        else : bot.SendTo(contact,'图灵聊天机器人已开启')
        tulingbot = True
        contenttype = type
    
    #Let the bot temperary unavailable
    if '--stop' in content : 
        if not permit[7]:reply = "permission denied"
        else : bot.SendTo(contact, 'QQ机器人已关闭')
        bot_avil = False
        contenttype = type
        
    #Let the bot sleep for 5 minutes
    if '--sleep' in content :
        if not permit[8]:reply = "permission denied"
        else : bot.SendTo(contact,'QQ机器人已暂停5分钟')
        availtime = time.time() + 300
        contenttype = type
        
    #wait up the bot from --stop or --sleep
    if '--on' in content:
        if not permit[9]:reply = "permission denied"
        else : availtime = time.time()
        bot_avil = True
        contenttype = type
    
    #restart the bot
    if '--restart' in content :
        if not permit[10]:reply = "permission denied"
        else : bot.SendTo(contact,'正在重启')
        bot.Restart()
        contenttype = type
    
    #kill the qqbot process,if you want to start again you might use the shell
    if '--kill' in content : 
        if not permit[11]:reply = "permission denied"
        else : bot.SendTo(contact, 'QQ机器人已退出')
        bot.Stop()






@qqbotslot
def onQQMessage(bot, contact, member, content):
    global availtime#record the time after which the bot can work
    global bot_avil #record if the bot is avail(record if the bot is not stopped)
    global tulingbot#record if the TulingBot is on
    global contenttype#record the content type to avoid a message be processed twice
    contenttype = 0#reset type every roop
    
    #record the permission of the commands
    permission = (True,True,True,True,True,True,True,True,True,True,True,True)
    permission2 = (False,False,False,False,False,False,False,False,False,False,False,False)
    
    
    #ban user
    if contact.ctype == 'group': 
        if member.qq == '123456789':#QQ number to ban
            contenttype = 99
    
    #group admin control
    if contact.ctype == 'group':    
        if (member.role_id ==0 or member.role_id ==1) and '@ME' in content and contenttype < 4:
            commands(bot, contact, member, content,permission,type=3)
    
    #group normal members control
    if  contact.ctype == 'group' and '@ME' in content and member.role_id ==2 and contenttype <3: 
        commands(bot, contact, member, content,permission2,type=2)
    
    
    #buddy control
    if contact.ctype == 'buddy' and '--admin' in content and contenttype < 3 :
        commands(bot, contact, member, content,permission,type=2)
    
    #normal reply        
    if contact.ctype == 'buddy' or (contact.ctype == 'group' and '@ME' in content): 
        if time.time() > availtime and bot_avil and contenttype <2 :
            reply = roader.reply(content,tulingbot)
            if reply is not None:
                if contact.ctype == 'group':reply = ' @'+member.name +" " + reply                
                bot.SendTo(contact,reply)
            
        
    # if '@ME' in content:
    #     bot.SendTo(contact, '%s， 想我了吧？' % member.name)

if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
