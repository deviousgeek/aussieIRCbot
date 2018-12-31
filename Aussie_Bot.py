#!/usr/local/bin/python
import re
import socket
import ssl
import time
import string
import random
import weatherdefine
import timelookup
import sys
import BotDefines
import webtitle
import insult
## Settings
### IRC
server = "chat.freenode.net"
port = 6697
channel = BotDefines.channel
botnick = BotDefines.botnick
password = BotDefines.password
admin = BotDefines.admin

#connecting to IRC

irc_C = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
irc = ssl.wrap_socket(irc_C)

print "Establishing connection to [%s]" % (server)
# Connect
irc.connect((server, port))
irc.setblocking(False)
#irc.send("PASS %s\n" % (password))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :meLon-Test\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :identify %s %s\r\n" % (botnick, password))
time.sleep(10)
irc.send("JOIN "+ channel +"\n")

def webhooks(data):
    irc.send("PRIVMSG "+ channel +" :" + data + '\r\n')

while True:
    
    reload(timelookup)
    reload(weatherdefine)
    try:
        text=irc.recv(2040)#get irc output
        chance = random.randint(1,200)
        chance1 = random.randint(1,200)

        #find strange char in text string and remove them
        text = filter(lambda x: x in string.printable, text)


        
        print text
        #find user name in text
        user = text.split("!")
        user = user[0].strip(":")
        #testing for key words and sending to def's
        if text.find('my place') != -1:
            
             
            irc.send("PRIVMSG "+ channel +" :" + weatherdefine.weather(user, text) + '\r\n')
        if text.find('mcspud') != -1:
            print user
            user = 'spuds'
            print user
            
            irc.send("PRIVMSG "+ channel +" :" + weatherdefine.weather(user, text) + '\r\n')

        if text.find('!t') != -1:
            city = text.split("!t ")
            city = city[1]
            print (city)
            irc.send("PRIVMSG "+ channel +" :" + timelookup.get_localized_time(city) + '\r\n')

        if text.find('santa') != -1:
            irc.send("PRIVMSG "+ channel +" :" + "HO  HO HO!" + '\r\n')
        
        if chance1 <= 1:
            irc.send("PRIVMSG "+ channel +" :" + insult.random_line() + '\r\n')
        
        if chance <= 1:
            irc.send("PRIVMSG "+ channel +" :" + insult.random_text() + '\r\n')

        if text.find('!rules') != -1 or text.find('!r') != -1:
            irc.send("PRIVMSG "+ channel +" :\x02\x034 Rule one:  \x035  No Banninating!\r\n")
            irc.send("PRIVMSG "+ channel +" :\x02\x034 Rule two:  \x035  See rule one\r\n")
            irc.send("PRIVMSG "+ channel +" :\x02\x034 Rule three: \x035 It's against the rules to enforce em\r\n")
            
        '''if text.find(":hi") !=-1:
            user = text.split("!")
            user = user[0].strip(":")
            print user
            irc.send("PRIVMSG "+ channel +" :Hello!\r\n")'''
            
         
            



            

        # Prevent Timeout
        if text.find('PING') != -1:
            irc.send('PONG ' + text.split() [1] + '\r\n')
            print("PONG")

    except Exception:
        continue

