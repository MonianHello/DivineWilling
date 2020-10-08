import os
import requests
import time
import hashlib
import getpass
import tkinter
import tkinter.messagebox

times = 0
# 一言最多条数
max = 100
# 一言API
hitokotourl = 'https://v1.hitokoto.cn/?encode=text'
'''
句子类型（参数）
参数	说明
a	动画
b	漫画
c	游戏
d	文学
e	原创
f	来自网络
g	其他
h	影视
i	诗词
j	网易云
k	哲学
l	抖机灵
其他	作为 动画 类型处理
可选择多个分类，例如： ?c=a&c=c

使用示例
https://v1.hitokoto.cn/ （从7种分类中随机抽取）
https://v1.hitokoto.cn/?c=b （请求获得一个分类是漫画的句子）
https://v1.hitokoto.cn/?c=f&encode=text （请求获得一个来自网络的句子，并以纯文本格式输出）

'''

os.system('color 07')
os.system('title Divine Willing')
os.system('cls')


# 判断是否为数字，返回布尔值

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 右上角打印时间

print(time.strftime("%m-%d %H:%M", time.localtime(time.time())).rjust(30))


# 一言函数

def hitokoto(num):
    try:
        for i in range(num):
            hitokoto = requests.get(hitokotourl)
            hitokoto = hitokoto.text
            print(hitokoto)

    except:
        print('无法与 ' + hitokotourl + ' 服务器通讯')
        print('请检查您的网络连接')
        hitokoto = 'Hello,World!'


print('''==============================

        Divine Willing.
       
==============================
''')
hitokoto(1)

# 管理员认证
while True:
    password = getpass.getpass('''
    
    现在开始进行管理员认证
    请键入管理员密码：''')
    passwordmd5 = hashlib.md5(password.encode(encoding='UTF-8')).hexdigest()
    # 失败次数
    times += 1
    if password == '114514':
        os.system('color 0c')
        print('这么臭的系统有存在的必要吗')
        # os.system('start explorer.exe')
        time.sleep(2.5)
        quit()
    if passwordmd5 == "37d1ecdcd4e31461bff763d27c0d6224":
        break
    # 认证失败
    if times >= 3:
        os.system('color 0c')
        print('''
    密码输入失败3次以上
    已拒绝管理员认证操作
    即将强制退出 Divine Willing System
    
        ''')
        # os.system('start explorer.exe')
        time.sleep(2.5)
        quit()

# 认证通过
print('''
已通过认证，欢迎您登入Divine Willing System
获取关于Divine Willing System的帮助，请键入[?]
''')
os.system('color 0b')
while True:
    choice = input('Admin>')
    if choice == 'e':
        os.system('start explorer.exe')
        continue
    if choice == 'c':
        os.system('start chrome.exe')
        continue
    if choice == 's':
        os.system('cmd')
        continue
    if choice == 'm':
        os.system('"E:\Minecraft\Minecraft.lnk"')
        continue
    if choice == 'q':
        os.system('"C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"')
        continue
    if choice == 'exit':
        os.system('color 0c')
        print('关闭Divine Willing System.')
        quit()
        break
    if choice == 'st':
        os.system('shutdown /t 1 /s /c "Divine Willing System" ')
        continue
    if choice == 'ip':
        os.system('ipconfig /all')
        continue
    if choice == 'yy':
        hitokoto(5)
        continue
    if choice == 'about':
        print('''
这里是MonianHello
E-mail:zhao17292@126.com
为防止cmd.exe(命令行)被禁用后无法使用大部分命令的情况
准备了天意系统
留了个小小的彩蛋
要知道彩蛋内容请输入我的生日~(YYYYMMDD)

2020.10
''')
        continue
    if choice == '?':
        print('''
以下是区别于 Microsoft Windows 命令提示符 的帮助内容
若寻求关于命令提示符的帮助，请键入 [help]

请注意:在天意系统中您无法更改本地目录
       如需使用 cmd.exe 请键入 [s]
       
[exit]:登出Divine Willing System
[s]:进入 命令提示符 界面 
    如需返回天意系统，在命令提示符中键入 [exit] 即可返回
[e]:启动资源管理器(start explorer.exe)
[c]:启动浏览器(start chrome.exe)
[m]:启动Minecraft(start "E:\Minecraft\Minecraft.lnk")
[q]:启动QQ(start "C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe")
[st]:关机(shutdown /t 1 /s /c "Divine Willing System" )
[ip]:查看网络配置(ipconfig /all)
[about]:关于天意Divine Willing系统
''')
        continue
    if choice == '20040515':
        print('''
第一个彩蛋是登录界面，输入"114514"
系统会不堪其臭自杀
第二个彩蛋是在系统内直接输入数字
可以得到相同数量的一言~(限制成100以内了)
调用的什么API?你断下网就行
        ''')
        continue
    if is_number(choice):
        if int(choice) > max:
            print('已经从' + str(choice) + '设置为' + str(max))
            time.sleep(0.75)
            choice = max
        hitokoto(int(choice))
        continue

    os.system(choice)
