"""try to stop user spamming bot"""
import time


def message_text(name_timers, user, text):
    try:
        gap = time.time() - name_timers[user]
    except:
        gap = 6
    name_timers.update({user: time.time()})
    if gap <= 5:
        text=""
    
    return text, name_timers

def make_user_list(text, NICK, CHANNEL):
    if text.find('{} = {} :'.format(NICK, CHANNEL)) != -1:
        listnames = text.split('{} = {} :'.format(NICK, CHANNEL))
        listnames = listnames[1].split(':')
        listnames = listnames[0].strip("\r\n")
        listnames = listnames.split()
        name_timers = {}
        for item in listnames:
            name_timers.update({item: time.time()})
        return name_timers
