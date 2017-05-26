此QQ机器人基于[此项目](https://github.com/pandolia/qqbot)扩展

## 使用场景
原意是用于高考后招新答疑，对于重复的问题可以直接调用机器人回答避免反复的键入。实际上emmmmmmmm

## 功能
- 提供管理员及群主对机器人的控制
- 通过关键字识别回复语句，若语句没有现有关键字，则交由图灵机器人处理
- 提供通过@机器人输入指令，添加关键字及对应回复的语句
- 可以选择让机器人忽视制定用户的消息，达到ban人的作用（主要是某位emmmmmmmm）


## 返回消息流程
- 先处理消息发送者是否被封禁，若是，则丢弃消息
- 然后识别是否管理员发送的命令。（命令的权限可以在permission数组设置，顺序对应command里面的语句）
- 然后识别是否普通用户发送的命令。（命令权限设置同上）
- 然后识别是否好友对话发送的命令
- 若都不是命令语句，这作为一般语句交由loadjson处理


## 一般语句的处理流程
- 先在帮助字典（helpdict）里寻找关键字，若语句含有关键字，则回复对应的value，value是设定的回复的语句
- 若helpdict里面没有，这寻找chatdict，处理流程同上
- 若两个字典都没有，则提交给图灵机器人处理。图灵机器人需要去官网申请一个APPID
- 群内所有人可以通过--help获取helpdict字典里面的所有key，这个作为一个帮助菜单使用
- 分开helpdict和chatdict的原因是，若只有一个字典，没有chatdict，不能起到活跃气氛的作用emmmmmmmm
- 所有群、好友共享同两个字典。


## 群管理员及群主可以通关@机器人并输入相应指令来控制机器人，目前支持的指令有
- --tulingoff         关闭图灵机器人(关键字检索仍有效） 
- --tulingon          开启图灵机器人
- --stop              关闭QQ机器人
- --sleep             机器人休眠5分钟
- --on                开启机器人
- --restart           重启机器人
- --addchat key value 增加新的chat项
- --addhelp key value 增加新的help项
- --deletechat key    删除key
- --deletehelp key    删除key


## 部署方法
详情请看[原项目](https://github.com/pandolia/qqbot)
搭建好python环境并更新，若是部署在无图形界面的服务器上，需要设定登录方式为邮件网页或者文本。
将四个文件放在同一目录下
若需要使用图灵机器人，在loadjson内的tuling函数的key内，输入申请到的key
```bash
sample1.py
```
建议第一次登录时使用，可以看是否出错
若是远程服务器使用ssh登录，应设定后台运行否在登出ssh后，会被结束进程
```bash
nohup python sample1.py &
exit
```
后台运行并使用nohup把输出控制台的信息输入到同目录下的文本，并且在登出后继续运行

