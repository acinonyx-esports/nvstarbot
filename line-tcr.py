# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator
#JANGAN LUPA =>  sudo pip install bs4 => sudo pip install BeautifulSoup => sudo pip install urllib

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token="Eoq5bhRLcexWIHM3vnz8.XiDURzmtJIEdrCTkAatqIa.CaCAUcvVyGgVjj5k2zD8dbzZUxqe7xdg5PGobBZ4h5o=")
cl.loginResult()

ku = LINETCR.LINE()
#ku.login(qr=True)
ku.login(token="Eoy7zfNN4uPF9TxBbvZ8.Av5v4LB9FM0/tRXjC4Nuga.jZFPAZSsQfc9A63V7Yddo8ROh2md4X+0gjosh5rkwbA=")
ku.loginResult()

ke = LINETCR.LINE()
#ke.login(qr=True)
ke.login(token="Eo2SIRuyC7iZ9tUfpj76.lTTYCD5tXzg8tGB0dlYzrG.FY6+yU73O6ypCCKR6Z7Ekdh20Sxil4w9nPhxcLhNFnw=")
ke.loginResult()

ko = LINETCR.LINE()
#ko.login(qr=True)
ko.login(token="EoNQiaySYF9bDKecFbi3.guHw1Zbg7+xYNC35a+kFGW.AV/55/bCalKiON6Ko2pMFEEOhwDKWunc1X/BhicFqEQ=")
ko.loginResult()

kb = LINETCR.LINE()
#kb.login(qr=True)
kb.login(token="EovTl8t2qlJWdAtPWLo6.qhdGUjjOYv72x/iJfAISHG.lAwW5BqiCg0YdskEokWc07DfRnD7N8YjT3gBMvsroo0=")
kb.loginResult()

ki = kk = kc = ks = ka = cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf+7')

helpMessage =""" 
╔═════════════
║ NvStar BOT v2.5.8
╠═════════════
║ MEMBER COMMAND 
╠═════════════
║╔════════════
║╠❂➣ What's new
║╠❂➣ Help
║╠❂➣ Me
║╠❂➣ My mid
║╠❂➣ Ginfo
║╠❂➣ Creator
║╠❂➣ Gcreator
║╠❂➣ Apakah
║╠❂➣ Rate
║╠❂➣ .apakah on/off
║╠❂➣ .rate on/off
║╠❂➣ Simisimi on/off
║╠❂➣ Cctv on
║╠❂➣ Cctv off
║╠❂➣ Check
║╠❂➣ .yt
║╠❂➣ Translate
║╚════════════
╠═════════════
║ ADMIN COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Respon
║╠❂➣ Speedbot
║╠❂➣ Tagall
║╠❂➣ Banlist
║╠❂➣ Gn (Nama)
║╠❂➣ Cn (Nama)
║╠❂➣ Cancel
║╠❂➣ Open Url
║╠❂➣ Close Url
║╠❂➣ Set Group
║╠❂➣ Banned @
║╠❂➣ Unban @
║╠❂➣ Kill ban
║╠❂➣ Nk @
║╠❂➣ Invite (MID)
║╠❂➣ Kick (Mid)
║╠❂➣ .Masuk bro
║╠❂➣ Bye all
║╚════════════
╠═════════════
║ OWNER COMMAND 
╠═════════════
║╔════════════
║╠❂➣ Adminlist
║╠❂➣ Glist
║╠❂➣ Group id
║╠❂➣ Cn (Nama) 
║╠❂➣ Kernel
║╠❂➣ System
║╠❂➣ Cpu
║╠❂➣ ifconfig
║╠❂➣ Bc
║╠❂➣ Mc
║╠❂➣ Mid @
║╠❂➣ Admadd @
║╠❂➣ Admrem @
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

Setgroup ="""
╔═════════════
║ PRIVATE COMMAND
╠═════════════
║╔════════════
║╠❂➣ Gr on/off
║╠❂➣ Contact on/off
║╠❂➣ Cancl on/off
║╠❂➣ Joinn on/off
║╠❂➣ Join on/off
║╠❂➣ .apakah on/off
║╠❂➣ .rate on/off
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

helptranslate ="""
╔═════════════
║ NvStar BOT v2.5.8
╠═════════════
║ TRANSLATE
╠═════════════
║╔════════════
║╠❂➣Id@en
║╠❂➣En@id
║╠❂➣Id@jp
║╠❂➣Jp@id
║╠❂➣Id@th
║╠❂➣Th@id
║╠❂➣Id@ar
║╠❂➣Ar@id
║╠❂➣Id@ko
║╠❂➣Ko@id
║╚════════════
╠═════════════
║ Hubungi owner jika
║ memerlukan sesuatu
║ line.me/ti/p/~KazeReborn
╚═════════════
"""

Whatsnew ="""
=================
  WHAT'S NEW?
=================
=> Update BOT dari versi 2.5.0 menjadi 2.5.8
=> Fixed some BUG
=> Stability Improvement
=> Perubahan command lebih detail
=> Sekarang member dapat mengecek kecepatan bot melalui command "Speedbot"
=> Group ID pada command "Ginfo" sekarang di rahasiakan

==================
  PERUBAHAN COMMAND
    MEMBER COMMAND 
==================
=> Speedbot

=================
  NEW OWNER COMMAND
=================
=> Mc (Mid check)

==================
  PERUBAHAN COMMAND
    KHUSUS OWNER 
==================
=> Adminlist
=> Kernel
=> System
=> Cpu
=> Glist
=> Group id
=> Cn
=> Mid @
"""

Botrule ="""
=================
  WHAT IS THIS BOT?
=================

Ini adalah bot gratis, jika group anda
ingin terhindar dari kicker silahkan invite
BOT ini ke dalam group mu

=================
  BOT RULE
=================

BOT ini akan menolak group
jika member kurang dari 20 orang

Dilarang kick member maka bot
mengusir orang tersebut

Seseorang yang merubah nama atau gambar
group akan langsung di usir

Seseorang yang membuka Link atau QR group
akan langsung diusir

=================
RULE DIATAS TIDAK BERLAKU
UNTUK OWNER (PEMILIK) GROUP
=================
"""



KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF=[ka,kb,ko,ke,ku]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid
Hmid = ke.getProfile().mid
Imid = ku.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,"ua5f2cbc325816777be5ef529eb920c50","u354838cfb35216ada4dcfc789de6f205","uc33e556c10279d1ba84669b303da74dd","u6f1809a9977fc0e6de0ae8f740e03922","uce3f3af0c36f4bf099972c0a5687ed42","u15a96ad4cce3ed4f4a03513cad7ad822","u529ed08e968ba9d107784186eb66b76a","uaa81f36f1d8d1c9105aa347d3fee442b","u2d7040967b3413bc7e0c47800f0b71b5","u04ed2796b2b055f6ee910fe11f4592a4","u1592572d68b3f7bf057e28bd01334651","u467aea8464c96bd16b09a43ea9adb70e"]
admin=["ua5f2cbc325816777be5ef529eb920c50","u354838cfb35216ada4dcfc789de6f205","uc33e556c10279d1ba84669b303da74dd","u6f1809a9977fc0e6de0ae8f740e03922","uce3f3af0c36f4bf099972c0a5687ed42","u15a96ad4cce3ed4f4a03513cad7ad822","u529ed08e968ba9d107784186eb66b76a","uaa81f36f1d8d1c9105aa347d3fee442b","u2d7040967b3413bc7e0c47800f0b71b5","u04ed2796b2b055f6ee910fe11f4592a4","u1592572d68b3f7bf057e28bd01334651","u467aea8464c96bd16b09a43ea9adb70e"]
creator=["ua5f2cbc325816777be5ef529eb920c50"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"NvStar Protection 1 ",
    "cName2":"NvStar Protection 2 ",
    "cName3":"NvStar Protection 3 ",
    "cName4":"NvStar Protection 4 ",
    "cName5":"NvStar Protection 5 ",
    "cName6":"NvStar Protection 6 ",
    "cName7":"NvStar Protection 7 ",
    "cName8":"NvStar Protection 8 ",
    "cName9":"NvStar Protection 9 ",
    "cName10":"NvStar Protection 10 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    "apakah":True,
    "rate":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

settings = {
    "simiSimi":{}
    }

setTime = {}
setTime = wait2['setTime']

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                   G = ka.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in Bots:
                  group = ka.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        
        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param3 in admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True        
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)

        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Translate"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helptranslate)
                else:
                    cl.sendText(msg.to,helptranslate)
            elif msg.text in ["Set group"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif msg.text in ["What's new"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Whatsnew)
                else:
                    cl.sendText(msg.to,Sett)
            elif msg.text in ["Botrule"]:
              if msg.from_ in creator:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Botrule)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
              else:
                  cl.sendText(msg.to,"Silahkan hubungi pemilik group untuk merubah nama group")
            elif ("Cv1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
                cl.kickoutFromGroup(msg.to,[midd])
            elif "_second kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "_third kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "_fourth kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "sinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "tinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "finvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Bot?"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '5'}
#                msg.text = None
#                cl.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '6'}
#                msg.text = None
#                ki.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '8'}
#                msg.text = None
#                kk.sendMessage(msg)
#            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '10'}
#                msg.text = None
#                kc.sendMessage(msg)
#           elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '12'}
#                msg.text = None
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Tidak ada satu orang pun yang masuk dalam daftar pending group")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan untuk menghubungi admin dalam masing masing group untuk membatalkan seluruh pending group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open url","open url"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invite by link dibuka")
                        else:
                            cl.sendText(msg.to,"Sudah terbuka")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan menghubungi admin dalam masing masing group untuk membuka Url/QR code")
                    cl.sendText(msg.to,"Dan dimohon untuk tidak membuka Url/QR code tanpa seizin admin group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Chivas")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 ourl","Cv2 link on"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = kk.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"Done Chivas")
                        else:
                            kk.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            kk.sendText(msg.to,"Can not be used outside the group")
                        else:
                            kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Chivas")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close url","close url"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invite by link ditutup")
                        else:
                            cl.sendText(msg.to,"Sudah tertutup")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan untuk menghubungi admin group untuk menutup Link/QR code")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Chivas")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 curl","Cv2 link off"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Chivas")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 curl","Cv3 link off"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Chivas")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
                rplace=msg.text.lower().replace("jointicket ")
                if rplace == "on":
                    wait["atjointicket"]=True
                elif rplace == "off":
                    wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group=cl.findGroupByTicket(ticket_id)
                        cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[Group ID] DIRAHASIAKAN\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[Group ID] DIRAHASIAKAN\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id group" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,msg.to)
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Untuk mengetahui id group perlu izin dari masing masing admin dalam group untuk melihat id group")      
            elif "My mid" == msg.text:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid RA" == msg.text:
                if msg.from_ in admin:
                    cl.sendText(msg.to,mid)
                    ki.sendText(msg.to,Amid)
                    kk.sendText(msg.to,Bmid)
                    kc.sendText(msg.to,Cmid)
                    ks.sendText(msg.to,Dmid)
                    ka.sendText(msg.to,Emid)
                    kb.sendText(msg.to,Fmid)
                    ko.sendText(msg.to,Gmid)
                    ke.sendText(msg.to,Hmid)
            elif "RA 1" == msg.text:
                cl.sendText(msg.to,mid)
            elif "RA 2" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "RA 3" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "RA 4" == msg.text:
                kc.sendText(msg.to,Cmid)
#            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "100",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                cl.sendMessage(msg)
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "10",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Galau"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "9",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["You"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "7",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hadeuh"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "6",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Please"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "4",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Haaa"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "3",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Lol"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "110",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
#            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "101",
#                                     "STKPKGID": "1",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#            elif msg.text in ["Welcome"]:
#                msg.contentType = 7
#                msg.text = None
#                msg.contentMetadata = {
#                                     "STKID": "247",
#                                     "STKPKGID": "3",
#                                     "STKVER": "100" }
#                ki.sendMessage(msg)
#                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Cn " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Cn ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + " done")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan menghubungi admin dari masing masing group untuk merubah nama group")
                    cl.sendText(msg.to,"Dan dimohon untuk tidak merubah nama group oleh diri mu sendiri")
            elif msg.text in ["Cv1 rename "]:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
#==============================================================================#
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO ENG]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM ENG]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO JPN]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM JPN]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO THA]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM THA]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO ARG]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM ARG]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM IDN]==\n" + "" + kata + "\n\n==[TO KOR]==\n" + "" + result + "\n\n==[SUKSES]==")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"==[FROM KOR]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")
#==============================================================================#
            elif "Mc " in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in creator:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in creator:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in creator:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in creator:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in creator:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join on"]:
                if msg.from_ in creator:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"sudah menyala")
                        else:
                            cl.sendText(msg.to,"selesai")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"sudah menyala")
                        else:
                            cl.sendText(msg.to,"Selesai")
            elif msg.text in ["Join off"]:
                if msg.from_ in creator:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Dimatikan")
                        else:
                            cl.sendText(msg.to,"Selesai")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Dimatikan")
                        else:
                            cl.sendText(msg.to,"Selesai")
            elif msg.text in ["Gcancel:"]:
                if msg.from_ in creator:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Leave on"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Leave off"]:
                if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set View"]:
                if msg.from_ in admin:
                    md = ""
                    if wait["Protectjoin"] == True: md+="╔═════════════\n╠❂➣ 􀔃􀆑lock􏿿  Block Join\n"
                    else: md+=" ╔═════════════\n╠❂➣ Block Join Off\n"
                    if wait["Protectgr"] == True: md+="╠❂➣ 􀔃􀆑lock􏿿   Block Group\n"
                    else: md+=" ╠❂➣ Block Group Off\n"
                    if wait["Protectcancl"] == True: md+="╠❂➣ 􀔃􀆑lock􏿿 Cancel All Invited\n"
                    else: md+=" ╠❂➣ Cancel All Invited Off\n"
                    if wait["contact"] == True: md+=" ╠❂➣ Contact    : on\n"
                    else: md+=" ╠❂➣ Contact    : off\n"
                    if wait["autoJoin"] == True: md+=" ╠❂➣ Auto join : on\n"
                    else: md +=" ╠❂➣ Auto join : off\n"
                    if wait["autoCancel"]["on"] == True:md+=" ╠❂➣ Group cancel : " + str(wait["autoCancel"]["members"]) + "\n"
                    else: md+= " ╠❂➣ Group cancel : off\n"
                    if wait["leaveRoom"] == True: md+=" ╠❂➣ Auto leave    : on\n"
                    else: md+=" ╠❂➣ Auto leave : off\n"
                    if wait["timeline"] == True: md+=" ╠❂➣ Share   : on\n"
                    else:md+=" ╠❂➣ Share   : off\n"
                    if wait["autoAdd"] == True: md+=" ╠❂➣ Auto add : on\n"
                    else:md+=" ╠❂➣ Auto add : off\n"
                    if wait["commentOn"] == True: md+=" ╠❂➣ Comment : on\n"
                    else:md+=" ╠❂➣ Comment : off\n"
                    if wait["apakah"] == True: md+=" ╠❂➣ Apakah : on\n"
                    else:md+=" ╠❂➣ Apakah : off\n"
                    if wait["rate"] == True: md+=" ╠❂➣ Rate : on\n╚════════════"
                    else:md+=" ╠❂➣ Rate : off\n╚════════════"
                    cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        kc.sendText(msg.to,"Bot 4 jam on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = kc.getProfile()
                        profile.displayName = wait["cName4"] + nowT
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Jam Selalu On")
                elif msg.text in ["Jam off"]:
                    if wait["clock"] == False:
                        kc.sendText(msg.to,"Bot 4 jam off")
                    else:
                        wait["clock"] = False
                        kc.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                if msg.from_ in admin:
                    n = msg.text.replace("Change clock","")
                    if len(n.decode("utc+7")) > 13:
                        cl.sendText(msg.to,"changed")
                    else:
                        wait["cName"] = n
                        cl.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------# 


         #---------------Fungsi Cek Group Creator Start------------------#
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
          #---------------Fungsi Cek Group Creator Finish-------------------#


          #---------------Fungsi youtube Start-------------------#
            elif ".yt " in msg.text:
                query = msg.text.replace(".yt ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
          #---------------Fungsi youtube Finish-------------------#


          #---------------Fungsi Creator Start-------------------#
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"jika membutuhkan sesuatu")
                cl.sendText(msg.to,"Silahkan PM/PC contact dibawah ini")
                cl.sendMessage(msg)
          #---------------Fungsi Creator Finish-------------------#



	 
         #-------------Fungsi Menambahkan / menghapus Admin Start-------------#
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                                ki.sendText(msg.to,"Selamat Kamu Admin Baru")
                                kk.sendText(msg.to,"Selamat Ya Selamat")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)
            elif "Admrem @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                                cl.sendText(msg.to,"Kamu DiPecat Jadi Admin :(")
                                cl.sendText(msg.to,"Yang Sabar Ya Boss..")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)
		 #-------------Fungsi Menambahkan / menghapus Admin Finish-------------#
		
		 #-------------Fungsi Music start---------------#
#            elif ".Music" in msg.text:
#	            songname = msg.text.lower().replace(".music","")
#	            params = {"songname":" songname"}
#	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
#	            data = r.text
#	            data = json.loads(data)
#	            for song in data:
#		            cl.sendMessage(msg.to, song[4])

#            elif ".Youtube " in msg.text:
#                 query = msg.text.replace(".Youtube ","")
#                 with requests.session() as s:
#                     s.headers['user-agent'] = 'Mozilla/5.0'
#                     url    = 'http://www.youtube.com/results'
#                     params = {'search_query': query}
#                     r    = s.get(url, params=params)
#                     soup = BeautifulSoup(r.content, 'html5lib')
#                     for a in soup.select('.yt-lockup-title > a[title]'):
#                         if '&List' not in a['href']:
#                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
		 #-------------Fungsi Music finish---------------#
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = kc.getProfile()
                        profile.displayName = wait["cName4"] + nowT
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"Sukses update")
                    else:
                        kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#

            elif "set on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Cctv sudah menyala silahkan masukan command [Check]")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Memasang reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     cl.sendText(msg.to,"Jangan lupa untuk di hapus jika sudah selesai menggunakannya")
                     print wait2

                    
            elif "set off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Set Reading point tidak di temukan")
                    cl.sendText(msg.to,"Silahkan masukan Command [Set on] untuk set point")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Menghapus reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
#            elif msg.text in ["toong","Toong"]:
#                 if msg.toType == 2:
#                    print "\nRead aktif..."
#                    if msg.to in wait2['readPoint']:
#                        if wait2["ROM"][msg.to].items() == []:
#                            chiya = ""
#                        else:
#                            chiya = ""
#                            for rom in wait2["ROM"][msg.to].items():
#                                print rom
#                                chiya += rom[1] + "\n"
#                        cl.sendText(msg.to, "╔═════════════ \n╠❂➣Sider :\n╠═════════════ %s\n╠\n╠═════════════\n╠❂➣Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
#                        print "\nReading Point Set..."
#                        try:
#                            del wait2['readPoint'][msg.to]
#                            del wait2['readMember'][msg.to]
#                        except:
#                            pass
#                        wait2['readPoint'][msg.to] = msg.id
#                        wait2['readMember'][msg.to] = ""
#                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#                        wait2['ROM'][msg.to] = {}
#                        print "toong ready"
#                        cl.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
#                    else:
#                        cl.sendText(msg.to, "Ketik [Cctv on] dulu, baru ketik [Toong]")


                    
            elif "check" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Ketik [Set on] terlebih dahulu ")
#-----------------------------------------------
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in creator:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to,"===SERVER INFO NetStat===\n\n" + botKernel )
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

            elif msg.text.lower() == 'system':
              if msg.from_ in creator:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to,"===SERVER INFO SYSTEM===\n\n" + botKernel )
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

            elif msg.text.lower() == 'kernel':
              if msg.from_ in creator:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to,"===SERVER INFO KERNEL===\n\n" + botKernel )
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

            elif msg.text.lower() == 'cpu':
              if msg.from_ in Creator:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to,"===SERVER INFO CPU===\n\n" + botKernel )
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in [".Masuk bro"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Bot Complete"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text in ["_First join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["_Second join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["_Third join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["_Fourth join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#

    #-------------------Fungsi BOT Kerang Ajaib & Cocoklogi Start-------------------#
            elif "Apakah " in msg.text:
              if wait["apakah"] == True:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bacod")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
            elif "Rate " in msg.text:
              if wait["rate"] == True:
                tanya = msg.text.replace("Rate","")
                jawab = ("1%","2%","3%","4%","5%","6%","7%","9%","10%","11%","12%","13%","""""""""""","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                cl.sendText(msg.to,jawaban)
    #-------------------Fungsi BOT Kerang Ajaib & Cocoklogi Finish------------------#	
	

    #-------------------Fungsi Nyala/Matikan BOT cocoklogi Start-------------------------#            
            elif msg.text in [".apakah on"]:
                if wait["apakah"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kerang Ajaib on")
                    else:
                        cl.sendText(msg.to,"Sudah nyala kok kerangnya")
                else:
                    wait["apakah"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kerang Ajaib on")
                    else:
                        cl.sendText(msg.to,"Sudah nyala kok kerangnya")

            elif msg.text in [".apakah off"]:
                if wait["apakah"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kerang Ajaib off")
                    else:
                        cl.sendText(msg.to,"Sudah dimatikan kok kerangnya")
                else:
                    wait["apakah"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kerang Ajaib Off")
                    else:
                        cl.sendText(msg.to,"Sudah dimatikan kok kerangnya")
    #-------------------Fungsi Nyala/Matikan BOT kerang apakah Finish-------------------------#
		

    #-------------------Fungsi Nyala/Matikan BOT cocoklogi Start-------------------------#            
            elif msg.text in [".rate on"]:
                if wait["rate"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rate cocoklogi aktiv")
                    else:
                        cl.sendText(msg.to,"Sudah nyala kok Rate cocokloginya")
                else:
                    wait["rate"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rate cocoklogi aktiv")
                    else:
                        cl.sendText(msg.to,"Sudah nyala kok Rate cocokloginya")



            elif msg.text in [".rate off"]:
                if wait["rate"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rate cocoklogi dimatikan")
                    else:
                        cl.sendText(msg.to,"Sudah dimatikan kok Rate cocokloginya")
                else:
                    wait["rate"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rate cocoklogi dimatikan")
                    else:
                        cl.sendText(msg.to,"Sudah dimatikan kok Rate cocokloginya")
    #-------------------Fungsi Nyala/Matikan BOT cocoklogi Finish-------------------------#

    #-------------------Fungsi Nyala/Matikan BOT Simisimi start-------------------------#
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Simi mode Off")
    #-------------------Fungsi Nyala/Matikan BOT Simisimi finish-------------------------#

    #-------------Fungsi Leave Group Start---------------#

            elif msg.text in ["Bye all"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye _Second"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye _Third"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye _Fourth"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["Cv1 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv2 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv3 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tagall"]:
                if msg.from_ in admin:
                     group = cl.getGroup(msg.to)
                     nama = [contact.mid for contact in group.members]

                     cb = ""
                     cb2 = ""
                     strt = int(0)
                     akh = int(0)
                     for md in nama:
                          akh = akh + int(6)

                          cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                          strt = strt + int(7)
                          akh = akh + 1
                          cb2 += "@nrik \n"

                     cb = (cb[:int(len(cb)-1)])
                     msg.contentType = 0
                     msg.text = cb2
                     msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                     try:
                        cl.sendMessage(msg)
                     except Exception as error:
                        print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

           # elif "Greet" in msg.text:
            #  if msg.from_ in Bots:
            #    if msg.toType == 2:
            #        print "ok"
            #        _name = msg.text.replace("","")
            #        gs = ki.getGroup(msg.to)
            #        gs = kk.getGroup(msg.to)
            #        gs = kc.getGroup(msg.to)
            #        ki.sendText(msg.to,"maaf kalo gak sopan")
            #        kk.sendText(msg.to,"makasih semuanya..")
            #        kc.sendText(msg.to,"hehehhehe")
            #        msg.contentType = 13
            #        msg.contentMetadata = {'mid': mid}
            #        ks.sendMessage(msg)
            #        targets = []
            #        for g in gs.members:
            #            if _name in g.displayName:
            #                targets.append(g.mid)
            #        if targets == []:
            #            ki.sendText(msg.to,"Not found")
            #        else:
            #            for target in targets:
            #              if target not in Bots:
            #                try:
            #                    klist=[ki,kk,kc,ks,ka]
            #                    kicker=random.choice(klist)
            #                    kicker.kickoutFromGroup(msg.to,[target])
            #                    print (msg.to,[g.mid])
            #                except:
            #                    ki.sendText(msg.to,"Group cleanse")
            #                    kk.sendText(msg.to,"Group cleanse")
            #                    kc.sendText(msg.to,"Group cleanse")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Kasian Di Kick....")
                                    kc.sendText(msg.to,"Hehehe")
                  else:
                      cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                      cl.sendText(msg.to,"Silahkan menghubungi admin dalam group masing masing untuk mengeluarkan member")
                      cl.sendText(msg.to,"Dan dimohon untuk tidak mengeluarkan member tanpa seizin admin/pemilik group ")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Blacklist @ ","")
                    _kicktarget = _name.rstrip(' ')
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"Not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        k3.sendText(msg.to,"Succes Cv")
                                    except:
                                        ki.sendText(msg.to,"error")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan menghubungi admin group jika menemukan member yang melakukan tindakan negative dalam group")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                ki.sendText(msg.to,"Error")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan menghubungi admin group jika menemukan member yang melakukan tindakan negative dalam group")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
                else:
                    cl.sendText(msg.to,"Perintah ini hanya untuk admin group")
                    cl.sendText(msg.to,"Silahkan menghubungi admin untuk melepaskan target dari daftar blacklist")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["...Up Up"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                    kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast all group Start------------#
            elif "Bc " in msg.text:
                if msg.from_ in creator:
                    bctxt = msg.text.replace("Bc ","")
                    a = cl.getGroupIdsJoined()
                    for taf in a:
                        cl.sendText(taf, (bctxt))
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ini digunakan owner untuk broadcast pengumuman ke semua group")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)
       #--------------Fungsi Broadcast Finish-----------#

#            elif msg.text in ["Cv say hi"]:
#                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
#                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
#                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
#
#            elif msg.text in ["Cv say hinata pekok"]:
#                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
#                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
#                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
#            elif msg.text in ["Cv say didik pekok"]:
#                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
#                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
#                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
#            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
#                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
#                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
#                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
#            elif msg.text in ["Cv say chomel pekok"]:
#                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
#                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
#                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
#            elif msg.text in ["#welcome"]:
#                if msg.from_ in admin:
#                    ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
#                    kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                    ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

#--------------------------------------------------------
#Restart_Program
            elif msg.text in ["Bot restart"]:
                if msg.from_ in creator:
                    cl.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
                else:
                    cl.sendText(msg.to, "Maaf command ini sangat dilarang\nuntuk member dan juga admin")
#--------------------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Respon","respon","Respon Dong","respon dong"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"Loading...")
                    ki.sendText(msg.to,"█▒▒▒▒▒▒▒▒▒")
                    kk.sendText(msg.to,"███▒▒▒▒▒▒▒ 10%")
                    kc.sendText(msg.to,"█████▒▒▒▒▒ 30%")
                    ks.sendText(msg.to,"███████▒▒▒ 50%")
                    ka.sendText(msg.to,"██████████ 100%")
                    ke.sendText(msg.to,"Complete")
      #-------------Fungsi Respon Finish---------------------#

            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "➣ %s  \n║" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "╔═════════════\n║ LIST GROUP\n╠═════════════\n║"+ h +"\n║ Total Group : " +"[ "+str(len(gid))+"]\n╚══════════════")
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

      #-------------Fungsi Adminlist START---------------------#
            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Informasi Admin list ini bersifat private")
                cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                cl.sendMessage(msg)
      #-------------Fungsi Adminlist TUTUP---------------------#

      #-------------Fungsi Adminlist TUTUP---------------------#

            elif "Mid @" in msg.text:
                if msg.from_ in creator:
                    _name = msg.text.replace("Mid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                        else:
                            pass
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Untuk mendapatkan MID orang lain membutuhkan izin dari orang tersebut\n\n dengan cara mengetik command [Me] ")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)
	
	    #-------------Fungsi Adminlist TUTUP---------------------#

        #-----------Fungsi mematikan BOT-------------------------#
#            elif msg.text in ["Shut Down"]:
#                if msg.from_ in Admin:
#                    ki.sendText(msg.to,"Shutting Down...")
      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speedbot","speedbot"]:
                start = time.time()
                cl.sendText(msg.to, "Waiting...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
                elif msg.text in ["Unban"]:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                    else:
                        ki.sendText(msg.to,"Blacklist user")
                        mc = ""
                        for mi_d in wait["blacklist"]:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        cocoa = ""
                        for mm in matched_list:
                            cocoa += mm + "\n"
                        cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"Tidak ada seorangpun dalam blacklist")

                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            kk.kickoutFromGroup(msg.to,[jj])
                            kc.kickoutFromGroup(msg.to,[jj])
                        cl.sendText(msg.to,"Blacklist keluar aja yaa...")

            elif msg.text in ["Clear"]:
                    if msg.from_ in creator:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                cl.cancelGroupInvitation(msg.to,[_mid])
                            cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)


#-----------------------------------------------------#
#import datetime
#import time
#
#def main():
#    print "System time:" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#
#if __name__ == '__main__':
#    while True:
#        main()
#        time.sleep(5)
#	
#-----------------------------------------------------#

#!/usr/bin/env python
 
import sys, os, time, atexit
from signal import SIGTERM
 
class Daemon:
        """
        A generic daemon class.
       
        Usage: subclass the Daemon class and override the run() method
        """
        def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
                self.stdin = stdin
                self.stdout = stdout
                self.stderr = stderr
                self.pidfile = pidfile
       
        def daemonize(self):
                """
                do the UNIX double-fork magic, see Stevens' "Advanced
                Programming in the UNIX Environment" for details (ISBN 0201563177)
                http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
                """
                try:
                        pid = os.fork()
                        if pid > 0:
                                # exit first parent
                                sys.exit(0)
                except OSError, e:
                        sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
                        sys.exit(1)
       
                # decouple from parent environment
                os.chdir("/")
                os.setsid()
                os.umask(0)
       
                # do second fork
                try:
                        pid = os.fork()
                        if pid > 0:
                                # exit from second parent
                                sys.exit(0)
                except OSError, e:
                        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
                        sys.exit(1)
       
                # redirect standard file descriptors
                sys.stdout.flush()
                sys.stderr.flush()
                si = file(self.stdin, 'r')
                so = file(self.stdout, 'a+')
                se = file(self.stderr, 'a+', 0)
                os.dup2(si.fileno(), sys.stdin.fileno())
                os.dup2(so.fileno(), sys.stdout.fileno())
                os.dup2(se.fileno(), sys.stderr.fileno())
       
                # write pidfile
                atexit.register(self.delpid)
                pid = str(os.getpid())
                file(self.pidfile,'w+').write("%s\n" % pid)
       
        def delpid(self):
                os.remove(self.pidfile)
 
        def start(self):
                """
                Start the daemon
                """
                # Check for a pidfile to see if the daemon already runs
                try:
                        pf = file(self.pidfile,'r')
                        pid = int(pf.read().strip())
                        pf.close()
                except IOError:
                        pid = None
       
                if pid:
                        message = "pidfile %s already exist. Daemon already running?\n"
                        sys.stderr.write(message % self.pidfile)
                        sys.exit(1)
               
                # Start the daemon
                self.daemonize()
                self.run()
 
        def stop(self):
                """
                Stop the daemon
                """
                # Get the pid from the pidfile
                try:
                        pf = file(self.pidfile,'r')
                        pid = int(pf.read().strip())
                        pf.close()
                except IOError:
                        pid = None
       
                if not pid:
                        message = "pidfile %s does not exist. Daemon not running?\n"
                        sys.stderr.write(message % self.pidfile)
                        return # not an error in a restart
 
                # Try killing the daemon process       
                try:
                        while 1:
                                os.kill(pid, SIGTERM)
                                time.sleep(0.1)
                except OSError, err:
                        err = str(err)
                        if err.find("No such process") > 0:
                                if os.path.exists(self.pidfile):
                                        os.remove(self.pidfile)
                        else:
                                print str(err)
                                sys.exit(1)
 
        def restart(self):
                """
                Restart the daemon
                """
                self.stop()
                self.start()
 
        def run(self):
                """
                You should override this method when you subclass Daemon. It will be called after the process has been
                daemonized by start() or restart().
                """
		

from socket import error as SocketError
import errno

try:
    response = urllib2.urlopen(request).read()
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise # Not error we are looking for
    pass # Handle error here.

