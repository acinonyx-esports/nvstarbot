# -*- coding: utf-8 -*-
#Chucky_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile,wikipedia

cl = LINETCR.LINE()
#cl.login(qr=True)
cl.login(token='')
cl.loginResult()
print "Cl-Login Success\n"

#ki = LINETCR.LINE()
#ki.login(qr=True)
#ki.login(token='EpGZS5iZsTD2x1XBxhe6.qhdGUjjOYv72x/iJfAISHG.0PGQC7k8DEK/bcpFyP1wTpCGCn6WFGFKTp4XQhodCfY=')
#ki.loginResult()
print "Ki-Login Success\n"

#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.login(token='EpbbyPqtyQSvhI70W9v3.guHw1Zbg7+xYNC35a+kFGW.6SvBlonOoBL5+gRNmxDycC9qbEYLWJnIb1RW8tAkuqE=')
#kk.loginResult()
print "Kk-Login Success\n"

#kc = LINETCR.LINE()
#kc.login(qr=True)
#kc.login(token='Ep6YKWR3iBymU0rYfP96.lTTYCD5tXzg8tGB0dlYzrG.S2+RgzFu63GdLN7EBfExflfpepxDf6sIedDJN3k29m0=')
#kc.loginResult()
print "Kc-Login Success\n"

#kr = LINETCR.LINE()
#kr.login(qr=True)
#kr.login(token='EpGZS5iZsTD2x1XBxhe6.qhdGUjjOYv72x/iJfAISHG.0PGQC7k8DEK/bcpFyP1wTpCGCn6WFGFKTp4XQhodCfY=')
#kr.loginResult()
print "Kr-Login Success\n"

#km = LINETCR.LINE()
#km.login(qr=True)
#km.login(token='Token_Kamu_Di_Sini_Sayang')
#km.loginResult()
print "Km-Login Success\n\n=====[Sukses All Login]====="

km = kr = kc = kk = ki = cl

reload(sys)
sys.setdefaultencoding('utf-8')


helpMessage ="""
╔═════════════
║ NvStar Public
╠═════════════
║ PUBLIC COMMAND 
╠═════════════
║╔════════════
║╠❂➣ !me
║╠❂➣ !mymid
║╠❂➣ !gcreator
║╠❂➣ !ginfo
║╠❂➣ !memberlist
║╠❂➣ !searchid: 「Text」
║╠❂➣ !checkdate 「DD-MM-YYYY」
║╠❂➣ !kalender
║╠❂➣ !creator
║╠❂➣ !playstore 「namaAPP」
║╠❂➣ !musik 「judul-penyanyi」
║╠❂➣ !lirik 「judil-penyanyi」
║╠❂➣ !ig 「username」 
║╠❂➣ !wikipedia 「text」
║╠❂➣ !pp @
║╠❂➣ !cover @
║╠❂➣ !getbio @
║╠❂➣ !getinfo @
║╠❂➣ !getname @
║╠❂➣ !set ➣ !check
║╠❂➣ !speed
║╠❂➣ !tagall 
║╠❂➣ Apakah
║╠❂➣ Kapan
║╠❂➣ Hari
║╠❂➣ Berapa
║╠❂➣ Berapakah
║╠❂➣ Translate
║╠❂➣ !bye-bye
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""

nvstar="ua5f2cbc325816777be5ef529eb920c50"

helpTranslate ="""
╔═════════════
║ NvStar Public
╠═════════════
║ TRANSLATE 
╠═════════════
║╔════════════
║╠❂➣ Id@en
║╠❂➣ En@id
║╠❂➣ Id@jp
║╠❂➣ Jp@id
║╠❂➣ Id@th
║╠❂➣ Th@id
║╠❂➣ Id@ar
║╠❂➣ Ar@id
║╠❂➣ Id@ko
║╠❂➣ Ko@id
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""

helpCreator ="""
╔═════════════
║ NvStar Public
╠═════════════
║ CREATOR COMMAND 
╠═════════════
║╔════════════
║╠❂➣ !runtime
║╠❂➣ !bc: 「text」
║╠❂➣ !glist
║╠❂➣ !group id
║╠❂➣ Removechat
║╠❂➣ !reboot
║╠❂➣ !friendlist
║╚════════════
╠═════════════
║ Ketik commandnya
║ Harus sesuai yaa kak
║ (/*’-‘*)/
╚═════════════
"""


KAC=[cl,ki,kk,kc,kr]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kr.getProfile().mid
Emid = km.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid]
Creator=["ua5f2cbc325816777be5ef529eb920c50"]
admin=["ua5f2cbc325816777be5ef529eb920c50"]

contact = cl.getProfile()
backup1 = cl.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup2 = ki.getProfile()
backup2.displayName = contact.displayName
backup2.statusMessage = contact.statusMessage                        
backup2.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup3 = kk.getProfile()
backup3.displayName = contact.displayName
backup3.statusMessage = contact.statusMessage                        
backup3.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup4 = kc.getProfile()
backup4.displayName = contact.displayName
backup4.statusMessage = contact.statusMessage                        
backup4.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup5 = kr.getProfile()
backup5.displayName = contact.displayName
backup5.statusMessage = contact.statusMessage                        
backup5.pictureStatus = contact.pictureStatus

responsename = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName
responsename5 = kr.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "AutoJoinCancel":True,
    "memberscancel":10,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'likeOn':{},
    'Leave':{},    
    'detectMention':True,
    'kickMention':False,      
    'timeline':False,
    "Timeline":False,
    "comment1":"",
    "comment2":"",
    "comment3":"",
    "comment4":"",
    "comment5":"",    
    "commentOn":False,
    "commentBlack":{},
    "message":"Trimakasih telah menambahkan ku menjadi teman, silahkan masukan aku kedalam group kamu yaa kak\n\nKita senang senang disana",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":False,
    "Ghost":False,
    "inviteprotect":False,    
    "alwaysRead":True,    
    "Tag":False,
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Nah lhoo~ " + " " + nick[0] + " " + "\nNgintip Aja Niih. . .\nChat dulu sana sama yang lain   ")
                                    else:
                                        cl.sendText(op.param1, "Hayoo " + " " + nick[1] + " " + "\nChat bareng sini, baru buka HPnya kan   ")
                                else:
                                    cl.sendText(op.param1, "Ngintip~? " + " " + Name + " " + "\nBaru buka groupnya yaa, chat dulu sonoh")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    	      
	      

        if op.type == 22:
            cl.leaveRoom(op.param1)

        if op.type == 21:
            cl.leaveRoom(op.param1)
			
        if op.type == 13:
	    print op.param3
                      
	    if mid in op.param3:
                if wait["AutoJoinCancel"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendText(op.param1,"" + cl.getContact(op.param2).displayName + "\nMaav kaka... Membernya kurang dari 10 Orang.\nInvite aku lagi yahh kalo sudah lebih dari 10 orang\n\n༼ つ ಥ_ಥ ༽つ")
                        cl.leaveGroup(op.param1)                        
		    else:
                        cl.acceptGroupInvitation(op.param1)
			cl.sendText(op.param1,"Haloo kaka - kaka semua.\nSilahkan ketik 「Help」 untuk melihat command list.\nPakai dengan bijak yaahh\n(づ｡◕‿‿◕｡)づ")


        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo.. " + cl.getContact(op.param2).displayName + "\nSelamat datang di " + str(ginfo.name) + "\nSemoga betah yaa disini\n\n(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER GABUNG KE DALAM GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"Yahhh kok pergi sih kaka " + cl.getContact(op.param2).displayName + "\nAku kangen kamu kak (ू˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ू)")
            print "MEMBER KELUAR DARI GROUP"

        if op.type == 26:
            msg = op.message


            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     ki.like(url[25:58], url[66:], likeType=1002)
                     kk.like(url[25:58], url[66:], likeType=1004)
                     kc.like(url[25:58], url[66:], likeType=1003)
                     kr.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     ki.comment(url[25:58], url[66:], wait["comment2"])
                     kk.comment(url[25:58], url[66:], wait["comment3"])
                     kc.comment(url[25:58], url[66:], wait["comment4"])
                     kr.comment(url[25:58], url[66:], wait["comment5"])
                     cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False

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
                                cl.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Hallo kaka o(≧∇≦o)","˭̡̞(◞⁎˃ᆺ˂)◞*✰ " + cName + " Ada apa kaka?",cName + " Aku lagi males di tag kak (╬ﾟ◥益◤ﾟ) ╬ﾟ","(*⌒▽⌒*)θ～♪\n", cName + " Ketik 「Help」 yaa kak", "Kenapa kak ｢(ﾟ<ﾟ)ﾞ?? " + cName, "Sebentar kak " + cName + " Aku ngantuk nih (●´ω｀●)ゞ","KABURRR~~! kaka " + cName + " Genit panggil² Aku\nε=ε=ε=ε=ε” “(/*’-‘*)/"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  break 


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            random.choice(KAC).sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            random.choice(KAC).sendText(msg.to,"Ditambahkan")
		    else:
			cl.sendText(msg.to,"Tidak dapat banned sesama admin")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KAC).sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Black List")
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
#===========ginfo start=============
            elif msg.text == "!ginfo":
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
                        cl.sendText(msg.to,"[Nama group]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[Nama group]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
#===========ginfo finish============
                        

 
            elif msg.text is None:
                return
 
#===========creator Start====================
            elif msg.text in ["!creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': nvstar}
		cl.sendText(msg.to,"Hallo kak ini contact orang yang buat aku\n೭੧(❛▿❛✿)੭೨")
                cl.sendMessage(msg)
#===========creator Finish===================
		
#            elif msg.text in ["Admin","admin"]:
#                msg.contentType = 13
#                admin1 = "u4a361586c55ac4ef218a0a9b78b2f1b3"
#                admin2 = "u4fd239a77c16d1ea7853cd801f6c379d"
#                admin3 = "ud919c919e5d9c5ec30dff0d9bc58dde7"
#                msg.contentMetadata = {'mid': WIB}
#                random.choice(KAC).sendMessage(msg)
#                msg.contentMetadata = {'mid': admin1}
#                random.choice(KAC).sendMessage(msg)
#                msg.contentMetadata = {'mid': admin2}
#                random.choice(KAC).sendMessage(msg)
#                msg.contentMetadata = {'mid': admin3}
#                random.choice(KAC).sendMessage(msg)                
#		random.choice(KAC).sendText(msg.to,"Itu Admin Kami (^_^)")	
		
 
                
            elif "!admin add @" in msg.text:
              if msg.from_ in TidakAktiv:
                print "[Command]Admin add executing"
                _name = msg.text.replace("!admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin NvStar BOT Berhasil Ditambahkan")
                            cl.sendText(msg.to,"Admin Power Dapat Menggunakan Command Khusus Untuk Mengatur BOT ini")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Maav...\nCommand ini hanya untuk Owner kami")
                cl.sendText(msg.to,"Silahkan PM/PC contact dibawah ini")
                cl.sendMessage(msg)
                
            elif "!admin remove @" in msg.text:
              if msg.from_ in TidakAktiv:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("!admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin NvStar BOT Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
                
            elif msg.text in ["!adminlist"]:
              if msg.from_ in TidakAktiv:
                if admin == []:
                    cl.sendText(msg.to,"The Admin List Is Empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = "╔═════════════════════════\n║        ◄ADMIN NvStar BOT►\n╠═════════════════════════\n"
                    for mi_d in admin:
                        mc += "╠❂➣ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc + "╚═════════════════════════")
                    print "[Command]Admin List executed"
                 

 
#===========gcreator Start=============
	    elif msg.text in ["!gcreator"]:
		ginfo = nadya.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                nadya.sendMessage(msg)
		nadya.sendText(msg.to,"Tuhh kak yang buat group ini\n.+:｡(ﾉ･ω･)ﾉﾞ")
#===========gcreator Finish============
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                                cl.sendImageWithURL(msg.to,image)
                                cl.sendText(msg.to,"Cover " + contact.displayName)
                                cl.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                cl.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = cl.getGroup(msg.to)
                     groups = ki.getGroup(msg.to)                     
                     groups = kk.getGroup(msg.to)                     
                     groups = kc.getGroup(msg.to)                     
                     groups = kr.getGroup(msg.to)                     
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             random.choice(KAC).sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 cl.findAndAddContactsByMid(target)
                                 ki.findAndAddContactsByMid(target)                                 
                                 kk.findAndAddContactsByMid(target)                                 
                                 kc.findAndAddContactsByMid(target)                                 
                                 kr.findAndAddContactsByMid(target)                                 
                                 random.choice(KAC).inviteIntoGroup(msg.to,[target])
                                 random.choice(KAC).sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      random.choice(KAC).sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
#===========Help Key Start===========
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
				
            elif msg.text in ["Translate"]:
                cl.sendText(msg.to,helpTranslate)
				
            elif msg.text in ["Help creator"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to,helpCreator)
#===========Help Key Finish==========          
                

 
#            elif msg.text in ["List group"]:
#                    gid = cl.getGroupIdsJoined()
#                    h = ""
#		    jml = 0
#                    for i in gid:
#		        gn = cl.getGroup(i).name
#                        h += "♦【%s】\n" % (gn)
#		        jml += 1
#                    cl.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "!ban group: " in msg.text:
		grp = msg.text.replace("!ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in TidakAktiv:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
 
            elif msg.text in ["!List ban"]:
		if msg.from_ in TidakAktiv:
                    if wait["BlGroup"] == {}:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
 
	    elif msg.text in ["!del ban: "]:
		if msg.from_ in TidakAktiv:
		    ng = msg.text.replace("!del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass

 
            elif "!join group: " in msg.text:
		ng = msg.text.replace("!join group: ","")
		gid = cl.getGroupIdsJoined()
		gid = ki.getGroupIdsJoined()
		gid = kk.getGroupIdsJoined()
		gid = kc.getGroupIdsJoined()
		gid = kr.getGroupIdsJoined()
		try:
		    if msg.from_ in TidakAktiv:
                        for i in gid:
                            h = cl.getGroup(i).name
                            h = ki.getGroup(i).name
                            h = kk.getGroup(i).name
                            h = kc.getGroup(i).name
                            h = kr.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		except Exception as e:
		    cl.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in TidakAktiv:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    kr.leaveGroup(i)
			    cl.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
 
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in TidakAktiv:
		    for i in gid:
			cl.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        cl.leaveGroup(i)
			ki.leaveGroup(i)
			kk.leaveGroup(i)
			kc.leaveGroup(i)
			kr.leaveGroup(i)
		    cl.sendText(msg.to,"Success Leave All Group")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
              if msg.from_ in TidakAktiv:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    cl.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["Ourl","Url on"]:
                if msg.from_ in TidakAktiv:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        cl.sendText(msg.to,"Url Sudah Aktif")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar ")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
 
            elif msg.text in ["Curl","Url off"]:
                if msg.from_ in TidakAktiv:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        cl.sendText(msg.to,"Url Sudah Di Nonaktifkan")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in TidakAktiv:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in Creatpr:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in TidakAktiv:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in TidakAktiv:
                    wait["AutoJoinCancel"] = False
                    cl.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in TidakAktiv:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Respon off"]:
		if msg.from_ in TidakAktiv:
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in TidakAktiv:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Responkick off"]:
		if msg.from_ in TidakAktiv:
                    wait["kickMention"] = False                    
                    cl.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
 
            elif msg.text in ["Leave on"]:
		if msg.from_ in TidakAktiv:
                    wait["Leave"] = True
                    cl.sendText(msg.to,"Leave Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in TidakAktiv:	        
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in TidakAktiv:	        
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in TidakAktiv:	        
                wait["inviteprotect"] = True
                cl.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

	    elif msg.text in ["Invitepro off"]:
	     if msg.from_ in TidakAktiv:	        
                wait["inviteprotect"] = False
                cl.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
		print wait["inviteprotect"]
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg) 

	    elif "Qr on" in msg.text:
	     if msg.from_ in TidakAktiv:	        
	        wait["Qr"] = True
	    	cl.sendText(msg.to,"QR Protect Sudah Aktif")
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg) 

	    elif "Qr off" in msg.text:
	     if msg.from_ in TidakAktiv:	        
	    	wait["Qr"] = False
	    	cl.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
	     else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg) 

            elif msg.text in ["Tag on"]:
		if msg.from_ in TidakAktiv:
                    wait["Tag"] = True
                    cl.sendText(msg.to,"Auto Tag Sudah Aktif")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg) 

            elif msg.text in ["Tag off"]:
		if msg.from_ in TidakAktiv:
                    wait["Tag"] = False
                    cl.sendText(msg.to,"Auto Tag Sudah Di Nonaktifkan")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg) 
                        

	    elif "Autokick on" in msg.text:
	     if msg.from_ in TidakAktiv:	 	        
		     wait["AutoKick"] = True
		     cl.sendText(msg.to,"Auto Kick Sudah Aktif")
	     else:
	        msg.contentType = 13
	        msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
	        cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
	        cl.sendMessage(msg)     

	    elif "Autokick off" in msg.text:
	     if msg.from_ in TidakAktiv:	 	        
		     wait["AutoKick"] = False
		     cl.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
	     else:
	        msg.contentType = 13
	        msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
	        cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
	        cl.sendMessage(msg)      

	    elif "Ghost on" in msg.text:
	     if msg.from_ in TidakAktiv:	 	        
		     wait["Ghost"] = True
		     cl.sendText(msg.to,"Ghost Sudah Aktif")
	     else:
	        msg.contentType = 13
	        msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
	        cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
	        cl.sendMessage(msg)    

	    elif "Ghost off" in msg.text:
	     if msg.from_ in TidakAktiv:	 	        
		     wait["Ghost"] = False
		     cl.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
	     else:
	        msg.contentType = 13
	        msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
	        cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
	        cl.sendMessage(msg)      

            elif msg.text in ["Allprotect on"]:
		if msg.from_ in TidakAktiv:
                    wait["AutoCancel"] = True
                    wait["inviteprotect"] = True                   
                    wait["AutoKick"] = True
                    wait["Qr"] = True
                    wait["Ghost"] = True                     
                    cl.sendText(msg.to,"All Protect Sudah Aktif Semua")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Allprotect off"]:
		if msg.from_ in TidakAktiv:
                    wait["AutoCancel"] = False
                    wait["inviteprotect"] = False                    
                    wait["AutoKick"] = False
                    wait["Qr"] = False
                    wait["Ghost"] = False                    
                    cl.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)


            elif msg.text in ["K on","Contact on"]:
                if msg.from_ in TidakAktiv:
                    wait["Contact"] = True
                    cl.sendText(msg.to,"Contact Sudah Aktif")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)

            elif msg.text in ["K off","Contact off"]:
                if msg.from_ in TidakAktiv:
                    wait["Contact"] = False
                    cl.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
               
            elif msg.text in ["Alwaysread on"]:
                if msg.from_ in TidakAktiv:
                    wait["alwaysRead"] = True
                    cl.sendText(msg.to,"Always Read Sudah Aktif")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk admin dan owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)

            elif msg.text in ["Alwaysread off"]:
                if msg.from_ in TidakAktiv:
                    wait["alwaysRead"] = False
                    cl.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)               


            elif msg.text in ["Sambutan on"]:
                if msg.from_ in TidakAktiv:
                    if wait["Sambutan"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sambutan Di Aktifkan")
                    else:
                        wait["Sambutan"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sudah On")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)

            elif msg.text in ["Sambutan off"]:
                if msg.from_ in TidakAktiv:
                    if wait["Sambutan"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sambutan Di Nonaktifkan")
                    else:
                        wait["Sambutan"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Sudah Off")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
                        
                        
            elif "Check on" in msg.text:
                if msg.from_ in TidakAktiv:
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                    wait["Sider"] = True
                    cl.sendText(msg.to,"Check sider one by one")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
                
            elif "Check off" in msg.text:
                if msg.from_ in TidakAktiv:
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        wait["Sider"] = False
                        cl.sendText(msg.to, "Cek Sider Off")
                    else:
                        cl.sendText(msg.to, "[Check on] Belum aktiv")  
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)                       


            elif msg.text in ["Set view"]:
              if msg.from_ in TidakAktiv:
                md = ""
		if wait["Sambutan"] == True: md+="╠❂➣✔️ Sambutan : On\n"
		else:md+="╠❂➣❌ Sambutan : Off\n"
		if wait["AutoJoin"] == True: md+="╠❂➣✔️ Auto Join : On\n"
                else: md +="╠❂➣❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠❂➣✔️ Auto Join Cancel : On\n"
                else: md +="╠❂➣❌ Auto Join Cancel : Off\n"                
		if wait["Leave"] == True: md+="╠❂➣✔️ Leave : On\n"
                else: md +="╠❂➣❌ Leave : Off\n"                
		if wait["Contact"] == True: md+="╠❂➣✔️ Info Contact : On\n"
		else: md+="╠❂➣❌ Info Contact : Off\n"
                if wait["AutoCancel"] == True:md+="╠❂➣✔️ Auto Cancel : On\n"
                else: md+= "╠❂➣❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠❂➣✔️ Invite Protect : On\n"
                else: md+= "╠❂➣❌ Invite Protect : Off\n"                
		if wait["Qr"] == True: md+="╠❂➣✔️ Qr Protect : On\n"
		else:md+="╠❂➣❌ Qr Protect : Off\n"
		if wait["AutoKick"] == True: md+="╠❂➣✔️ Auto Kick : On\n"
		else:md+="╠❂➣❌ Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠❂➣✔️ Ghost : On\n"
		else:md+="╠❂➣❌ Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠❂➣✔️ Always Read : On\n"
		else:md+="╠❂➣❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠❂➣✔️ Auto Respon : On\n"
		else:md+="╠❂➣❌ Auto Respon : Off\n"		
		if wait["kickMention"] == True: md+="╠❂➣✔️ Auto Respon Kick : On\n"
		else:md+="╠❂➣❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠❂➣✔️ Auto Sider : On\n"
		else:md+="╠❂➣❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠❂➣✔️ Simisimi : On\n"
		else:md+="╠❂➣❌ Simisimi: Off\n"		
		if wait["Tag"] == True: md+="╠❂➣✔️ Auto Tag : On\n"
		else:md+="╠❂➣❌ Auto Tag : Off\n"
                cl.sendText(msg.to,"╔═════════════════════════\n""║           ◄STATUS NvStar BOT►\n""╠═════════════════════════\n"+md+"╚═════════════════════════")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner kami\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)


#            elif msg.text in ["Gift","gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '5'}
#                msg.text = None
#                cl.sendMessage(msg)

 #           elif msg.text in ["All gift"]:
 #               msg.contentType = 9
 #               msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
 #                                   'PRDTYPE': 'THEME',
 #                                   'MSGTPL': '5'}
 #               msg.text = None
 #               ki.sendMessage(msg)
 #               kk.sendMessage(msg)
 #               kc.sendMessage(msg)

#            elif msg.text in ["TC1 Gift","TC1 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '6'}
#                msg.text = None
#                ki.sendMessage(msg)

#            elif msg.text in ["TC2 Gift","TC2 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '7'}
#                msg.text = None
#                kk.sendMessage(msg)

#            elif msg.text in ["TC3 Gift","TC3 gift"]:
#                msg.contentType = 9
#                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
#                                    'PRDTYPE': 'THEME',
#                                    'MSGTPL': '8'}
#                msg.text = None
#                kc.sendMessage(msg)
                
                
#            elif "Gift1 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift1 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '1',
#                                                         'STKPKGID': '1380280'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift2 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift2 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '2',
#                                                         'STKPKGID': '1360738'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift3 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift3 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       for s in gs.members:
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '3',
#                                                         'STKPKGID': '1395389'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift4 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift4 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                       if targets == []:
#                              targets.append(s.mid)
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '4',
#                                                         'STKPKGID': '1329191'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift5 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift5 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '1',
#                                                         'STKPKGID': '9057'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift6 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift6 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '2',
#                                                         'STKPKGID': '9167'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift7 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift7 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '3',
#                                                         'STKPKGID': '7334'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift8 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift8 ","")
#                       nk2 = nk1.replace("@","")
#                       nk1 = nk0.lstrip()
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '1',
#                                                         'STKPKGID': '1380280'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift9 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift9 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '4',
#                                                         'STKPKGID': '1405277'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}

#            elif "Gift10 " in msg.text:
#                       msg.contentType = 13
#                       nk0 = msg.text.replace("Gift10 ","")
#                       nk1 = nk0.lstrip()
#                       nk2 = nk1.replace("@","")
#                       nk3 = nk2.rstrip()
#                       _name = nk3
#                       gs = cl.getGroup(msg.to)
#                       targets = []
#                       for s in gs.members:
#                           if _name in s.displayName:
#                              targets.append(s.mid)
#                       if targets == []:
#                           sendMessage(msg.to,"user does not exist")
#                           pass
#                       else:
#                           for target in targets:
#                                try:
#                                    cl.sendText(msg.to,_name + " Check Your Gift")
#                                    msg.contentType = 9
#                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
#                                                         'STKVER': '1',
#                                                         'MSGTPL': '1',
#                                                         'STKPKGID': '1296261'}
#                                    msg.to = target
#                                    msg.text = None
#                                    cl.sendMessage(msg)
#                                except:
#                                    msg.contentMetadata = {'mid': target}


#            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '100',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["hehehe","hehe"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '10',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

 #           elif msg.text.lower() in ["galau"]:
 #               msg.contentType = 7
 #               msg.contentMetadata={'STKID': '9',
 #                                   'STKPKGID': '1',
 #                                   'STKVER': '100'}
 #               msg.text = None
 #               cl.sendMessage(msg)

#            elif msg.text.lower() in ["you","kau","kamu"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '7',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '6',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '4',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["haa","haaa","kaget"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '3',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["lucu","ngakak","lol"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '110',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["hmm","hmmm"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '101',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["tidur"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '1',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["gemes"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '2',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["cantik","imut"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '5',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["nyanyi","lalala"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '11',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["gugup"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '8',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '13',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '14',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["ngejek"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '15',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["nangis","sedih"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '16',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["woi","kampret"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '102',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#            elif msg.text.lower() in ["huft"]:
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '104',
#                                    'STKPKGID': '1',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)
                
        


#===========Tagall Start=================
            elif msg.text in ["!tagall"]:
                if msg.from_ in TidakAktiv:
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
                      cl.sendText(msg.to,"Cilukbaa~~ (≧д≦ヾ)")
                  except Exception as error:
                      print error
#===========Tagall Finish================


#===========Set > Check Start==================
            elif msg.text in ["!set"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Ketik 「!check」 lihat yang ngintip kak\n!(•̀ᴗ•́)و ̑̑")
                print "Setpoint"

            elif msg.text in ["!check"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║ Ini kak yang ngintip (*ﾟﾛﾟ)\n╠═════════════════════════\n╠❂➣"
                        grp = '\n╠❂➣ '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠❂➣ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                    else:
                        cl.sendText(msg.to, "Belum ada yang ngintip kak (•̥́_•ૅू˳)")
                    print "Ceksider"
#===========Set > Check Finish==================


	    elif "Kick " in msg.text:
		if msg.from_ in TidakAktiv:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ki.kickoutFromGroup(msg.to,[mention['M']])
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

	    elif "Set member: " in msg.text:
		if msg.from_ in TidakAktiv:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

	    elif "Add all" in msg.text:
		if msg.from_ in TidakAktiv:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Invite"]:
                if msg.from_ in TidakAktiv:
                    wait["invite"] = True
                    cl.sendText(msg.to,"Send Contact")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                    cl.sendMessage(msg)
                
                

#            elif msg.text in ["Auto like"]:
#                wait["likeOn"] = True
#                cl.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                if msg.from_ in TidakAktiv:
                    wait["steal"] = True
                    cl.sendText(msg.to,"Send Contact")

                

#            elif msg.text in ["Giftbycontact"]:
#                wait["gift"] = True
#                cl.sendText(msg.to,"Send Contact") 
                

	    elif "Recover" in msg.text:
	      if msg.from_ in TidakAktiv:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")


            elif ("Gn: " in msg.text):
              if msg.from_ in TidakAktiv:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Tidak dapat dilakukan diluar group")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif "Kick: " in msg.text:
              if msg.from_ in TidakAktiv:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki,kk,kc]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    cl.sendText(msg.to,"Tidak dapat kick admin BOT ini")

            elif "Invite: " in msg.text:
              if msg.from_ in TidakAktiv:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                ki.findAndAddContactsByMid(midd)
                kk.findAndAddContactsByMid(midd)
                kc.findAndAddContactsByMid(midd)
                kr.findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

            elif "Invite creator" in msg.text:
              if msg.from_ in TidakAktiv:
                midd = "ua5f2cbc325816777be5ef529eb920c50"
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])

#            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
#                gs = cl.getGroup(msg.to)
#                cl.sendText(msg.to,"Selamat Datang Di "+ gs.name)
#                msg.contentType = 7
#                msg.contentMetadata={'STKID': '247',
#                                    'STKPKGID': '3',
#                                    'STKVER': '100'}
#                msg.text = None
#                cl.sendMessage(msg)

#===========BROADCAST START==========
	    elif "!bc " in msg.text:
		bc = msg.text.replace("!bc ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Ada Broadcast dari majikan ku kak\n☆*:.｡.o(≧▽≦)o.｡.:*☆\n\n"+bc+"\n\nContact Me : line.me/ti/p/~KazeReborn")
		    cl.sendText(msg.to,"Broadcast Success")
#===========BROADCAST FINISH=========

            elif msg.text in ["Cancel"]:
              if msg.from_ in TidakAktiv:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["TC1 Cancel"]:
              if msg.from_ in TidakAktiv:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                ki.sendText(msg.to,"All invitations have been refused")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["TC2 Cancel"]:
              if msg.from_ in TidakAktiv:
                gid = kk.getGroupIdsInvited()
                for i in gid:
                    kk.rejectGroupInvitation(i)
                kk.sendText(msg.to,"All invitations have been refused")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["TC3 Cancel"]:
              if msg.from_ in TidakAktiv:
                gid = kc.getGroupIdsInvited()
                for i in gid:
                    kc.rejectGroupInvitation(i)
                kc.sendText(msg.to,"All invitations have been refused")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["Gurl"]:
              if msg.from_ in TidakAktiv:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                    cl.sendText(msg.to,"Berhati hatilah saat menyebarkan link group")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak dapat digunakan diluar group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

            elif msg.text in ["All join","Join all"]:
		if msg.from_ in TidakAktiv:
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
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    G.preventJoinByTicket(G)
                    ki.updateGroup(G)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Nv1 join"]:
		if msg.from_ in TidakAktiv:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Nv2 join"]:
		if msg.from_ in TidakAktiv:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kk.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ki.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Nv3 join"]:
		if msg.from_ in TidakAktiv:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)

            elif msg.text in ["Nv4 join"]:
		if msg.from_ in TidakAktiv:
                    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
		    cl.sendMessage(msg)



#            elif msg.text in ["timeline"]:
#		try:
#                    url = cl.activity(limit=5)
#		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
#		except Exception as E:
#		    print E

            elif msg.text in ["Bye all"]:
              if msg.from_ in TidakAktiv:
                if wait["Leave"] == True:		    
                    ki.leaveGroup(msg.to)
                    kk.leaveGroup(msg.to)
                    kc.leaveGroup(msg.to)
                    kr.leaveGroup(msg.to)
                else:
		              cl.sendText(msg.to,"Status: Leave off")   
		              cl.sendText(msg.to,"Ketik [Leave on] terlebih dahulu")
              else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Perintah ditolak..\nCommand ini privasi hanya untuk owner BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")
                  cl.sendMessage(msg)

#===========KELUAR START============
            elif msg.text in ["!bye-bye"]:
		    cl.sendText(msg.to, "Kaka jahat aku di usir\n˚‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·˚")
		    cl.leaveGroup(msg.to)
#===========KELUAR FINISH===========

            elif msg.text in ["!sp","!speed","!speed"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		cl.sendText(msg.to, "Progress...")
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["!speedbot"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))                 


            elif "Nk: " in msg.text:
		if msg.from_ in TidakAktiv:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = kk.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                kr.kickoutFromGroup(msg.to,[target])
                                kr.leaveGroup(msg.to)
                                ki.sendText(msg.to,"Kasihan deh kena kick")
                                kk.sendText(msg.to,"Pakyu~")
			    else:
			        cl.sendText(msg.to,"Tidak dapat kick admin BOT ini")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")    
		    cl.sendMessage(msg)
 
            elif msg.text in ["Ban"]:
                if msg.from_ in TidakAktiv:
                    wait["wblacklist"] = True
                    ki.sendText(msg.to,"send contact")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")    
                    cl.sendMessage(msg)

            elif msg.text in ["Unban"]:
                if msg.from_ in TidakAktiv:
                    wait["dblacklist"] = True
                    ki.sendText(msg.to,"send contact")
                else:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                    cl.sendText(msg.to,"Perintah ditolak..\nCommand ini hanya untuk admin BOT\nUntuk informasi lebih lanjut hubungi owner kami dibawah ini")    
                    cl.sendMessage(msg)
 
            elif "Ban @" in msg.text:
                if msg.from_ in TidakAktiv:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes BosQ")
                                except:
                                    ki.sendText(msg.to,"Error")
			    else:
				cl.sendText(msg.to,"Sesama admin BOT ini tidak dapat saling banned")
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)
 
            elif msg.text in ["Banlist","Ban list"]:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    random.choice(KAC).sendText(msg.to,"◄BLACKLIST USER NvStar BOT►\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in TidakAktiv:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kk.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ki.sendText(msg.to,"Succes BosQ")
                            except:
                                ki.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in TidakAktiv:
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"Blacklist di bersihkan") 
                    cl.sendText(msg.to,"Semua akun telah dibersihkan") 
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member tidak dapat menggunakan perintah ini.\nJika salah satu teman mu masuk daftar Blacklist")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

#            elif msg.text.lower() in ["bot"]:
#                cl.sendText(msg.to,"Apa Manggil~Manggil Aku!?") 
#                cl.sendText(msg.to,"Lagi kangen yaaa 😄😄😄") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in TidakAktiv:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist keluar aja yaa")
		else:
		    msg.contentType = 13
		    msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
		    cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
		    cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
		    cl.sendMessage(msg)
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in TidakAktiv:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kk.sendText(msg.to,"Fuck You")
                            kc.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
                      else:
                          msg.contentType = 13
                          msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                          cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                          cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                          cl.sendMessage(msg)

 
 #            elif "Kickall" == msg.text:
#		    if msg.from_ in TidakAktiv:
#                     if msg.toType == 2:
#                        print "Kick all member"
#                        _name = msg.text.replace("Kickall","")
#                        gs = ki.getGroup(msg.to)
#                        gs = kk.getGroup(msg.to)
#                        gs = kc.getGroup(msg.to)
#                        ki.sendText(msg.to,"Sampai jumpaa~")
#                        kc.sendText(msg.to,"Dadaaah~")
#                        targets = []
#                        for g in gs.members:
#                            if _name in g.displayName:
#                                targets.append(g.mid)
#                        if targets == []:
#                            ki.sendText(msg.to,"Not found.")
#                        else:
#                            for target in targets:
#				if target not in admin:
#                                    try:
#                                        klist=[ki,kk,kc]
#                                        kicker=random.choice(klist)
#                                        kicker.kickoutFromGroup(msg.to,[target])
#                                        print (msg.to,[g.mid])
#                                    except Exception as e:
#                                        cl.sendText(msg.to,str(e))
#			    cl.inviteIntoGroup(msg.to, targets)
 

#===========REBOOOT START===========
	    elif msg.text in ["!reboot"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Sebentar kak robotnya ku restart dulu\n(๑>ᴗ<๑)")
		    restart_program()
		    print "@Restart"
#===========REBOOOT FINISH==========
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in TidakAktiv:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		 
	        else:
	            cl.sendText(msg.to, "Perintah ini sangat dilarang untuk Member dan juga Admin")


            elif 'Crash' in msg.text:
              if msg.from_ in TidakAktiv:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uce3f3af0c36f4bf099972c0a5687ed42"}
                cl.sendText(msg.to, "Cem cem'an owner gw tuh 􀜁􀅔haha􏿿")
                cl.sendMessage(msg)
              else:
	            cl.sendText(msg.to, "Mau ape lu!!??\nItu kontak cem cem'an owner gw 􀜁􀅔Har Har􏿿")

            elif "!midcheck " in msg.text:
                mmid = msg.text.replace("!midcheck ","")
                msg.contentType = 13
                msg.contentMetadata = {'mid': mmid}
                cl.sendMessage(msg)

            elif "Nvcaptain copy @" in msg.text:
              if msg.from_ in TidakAktiv:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Kapten copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif "Nv1 copy @" in msg.text:
              if msg.from_ in TidakAktiv:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC1 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif "Nv2 copy @" in msg.text:
              if msg.from_ in TidakAktiv:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC2 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kk.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kk.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kk.CloneContactProfile(target)
                               kk.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e
                                
            elif "Nv3 copy @" in msg.text:
              if msg.from_ in TidakAktiv:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC3 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kc.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kc.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kc.CloneContactProfile(target)
                               kc.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e                                

            elif "Nv4 copy @" in msg.text:
              if msg.from_ in TidakAktiv:
                   print "[COPY] Ok"
                   _name = msg.text.replace("TC4 copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kr.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kr.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kr.CloneContactProfile(target)
                               kr.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup all"]:
              if msg.from_ in TidakAktiv:
                try:
                    ki.updateDisplayPicture(backup2.pictureStatus)
                    ki.updateProfile(backup2)

                    kk.updateDisplayPicture(backup3.pictureStatus)
                    kk.updateProfile(backup3)

                    kc.updateDisplayPicture(backup4.pictureStatus)
                    kc.updateProfile(backup4)

                    kr.updateDisplayPicture(backup5.pictureStatus)
                    kr.updateProfile(backup5)
                    
                    cl.updateDisplayPicture(backup1.pictureStatus)
                    cl.updateProfile(backup1)
                    cl.sendText(msg.to, "All Done (^_^)")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
                    
                    

                                


 
#===========musik Start=====================
	    elif "!musik " in msg.text:
					songname = msg.text.replace("!musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Judul : " + song[0] + "\nDurasi : " + song[1] + "\nLink download : " + song[4] + "\n\nSebentar yaa kak lagunya ku proses dulu")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Sudah selsai kak lagu " + song[0] + " Bisa langsung di play musiknya\n\n(◦′ᆺ‵◦)♬°✧❥✧¸.•*¨*✧♡✧ℒℴѵℯ✧♡✧*¨*•.❥")
#===========musik Finish===================)
	
            elif '.lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('.lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
#===========lirik Start===================
            elif '!lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('!lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
#===========lirik Finish===================
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    cl.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


#===========cover @ start=================
            elif "!cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("!cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar cover si doi gagal kak\n(๑◕︵◕๑)")
#===========cover @ finish================
                                
                                
#===========Pp @ start================
            elif "!pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("!pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Nggak ketemu kak (๑◕︵◕๑)\nMungkin nama doi pakai unicode")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload gambar profile si doi gagal kak\n(๑◕︵◕๑)")
#===========Pp @ finish===============


            elif msg.text.lower() == 'ifconfig':
                  if msg.from_ in TidakAktiv:
                      botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                  if msg.from_ in TidakAktiv:
                      botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                  if msg.from_ in TidakAktiv:
                      botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                  if msg.from_ in TidakAktiv:
                      botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                      cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")


            elif "Scbc " in msg.text:
              if msg.from_ in TidakAktiv:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = cl.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      cl.sendText(manusia, (bctxt))
                      t-=1
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Command ini hanya digunakan owner untuk Broadcast")
                cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                cl.sendMessage(msg)

            elif "Cbc " in msg.text:
              if msg.from_ in TidakAktiv:
                  broadcasttxt = msg.text.replace("Cbc ", "") 
                  orang = cl.getAllContactIds()
                  for manusia in orang:
                    cl.sendText(manusia, (broadcasttxt))
              else:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Command ini hanya digunakan owner untuk Broadcast")
                cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                cl.sendMessage(msg)

#===========wikipedia Start===================
            elif '!wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("!wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Judul ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Maav kak... Textnya terlalu banyak\n(っ◞‸◟c)\n\nKlik link dibawah ini kak untuk membacanya\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
#===========wikipedia Finish==================

#===========Ig Start===================
            elif '!ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("!ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "(╭☞´ิ∀´ิ)╭☞ Ini kak Instagramnya\n"
                    details = ""
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#===========Ig Finish===================
                	
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                cl.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                cl.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
                    
                    
            elif 'Youtubevideo: ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubevideo: ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        cl.sendVideoWithURL(msg.to,'https://www.youtube.com' + results['href'])
                    except:
                        cl.sendText(msg.to, "Could not find it")                    

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

            elif ".welcome" in msg.text:
                gs = cl.getGroup(msg.to)
                say = msg.text.replace(".welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

 
            elif "@NvStar Captain" in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                cl.sendText(msg.to,"Hallo, jika membutuhkan sesuatu")
                cl.sendText(msg.to,"Silahkan PM/PC contact owner dibawah ini")
                cl.sendMessage(msg)


            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +cl.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    kr.sendText(msg.to,beb)



#===========playstore Start=====================
            elif "!playstore " in msg.text.lower():
                tob = msg.text.lower().replace("!playstore ","")
                cl.sendText(msg.to,"Sedang Mencari...")
                cl.sendText(msg.to,"Nama App : "+tob+"\nSumber : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                cl.sendText(msg.to,"Ituu~ kak link appnya.\no(〃＾▽＾〃)o")
#===========playstore Finish====================


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass


            elif ".bio " in msg.text:
                if msg.from_ in TidakAktiv:
                    string = msg.text.replace(".bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        ki.updateProfile(profile)
                        kk.updateProfile(profile)
                        kc.updateProfile(profile)
                        kr.updateProfile(profile)
                        cl.sendText(msg.to,"All Done")
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"Member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)

            elif "Namecaptain" in msg.text:
		if msg.from_ in TidakAktiv:
                    string = msg.text.replace("Namecaptain ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + " done")

            elif "Namenv1 " in msg.text:
		if msg.from_ in TidakAktiv:
                    string = msg.text.replace("Namenv1 ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ki.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"name " + string + " done")

            elif "Namenv2" in msg.text:
		if msg.from_ in TidakAktiv:
                    string = msg.text.replace("Namenv2 ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kk.getProfile()
                        profile.displayName = string
                        kk.updateProfile(profile)
                        kk.sendText(msg.to,"name " + string + " done")

            elif "Namenv3" in msg.text:
		if msg.from_ in TidakAktiv:
                    string = msg.text.replace("Namenv3 ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = kc.getProfile()
                        profile.displayName = string
                        kc.updateProfile(profile)
                        kc.sendText(msg.to,"name " + string + " done")

            elif "Namenv4" in msg.text:
		if msg.from_ in TidakAktiv:
                    string = msg.text.replace("Namenv4 ","")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = cl.getProfile()
                        profile.displayName = string
                        kr.updateProfile(profile)
                        kr.sendText(msg.to,"name " + string + " done")


#            elif "Ulti " in msg.text:
#              if msg.from_ in TidakAktiv:
#                ulti0 = msg.text.replace("Ulti ","")
#                ulti1 = ulti0.rstrip()
#                ulti2 = ulti1.replace("@","")
#                ulti3 = ulti2.rstrip()
#                _name = ulti3
#                gs = cl.getGroup(msg.to)
#                ginfo = cl.getGroup(msg.to)
#                gs.preventJoinByTicket = False
#                cl.updateGroup(gs)
#                invsend = 0
#                Ticket = cl.reissueGroupTicket(msg.to)
#                km.acceptGroupInvitationByTicket(msg.to,Ticket)
#                time.sleep(0.2)
#                targets = []
#                for s in gs.members:
#                        if _name in s.displayName:
#                                targets.append(s.mid)
#                if targets ==[]:
#                        sendMessage(msg.to,"user does not exist")
#                        pass
#                else:
#                        for target in targets:
#                                try:
#                                        km.kickoutFromGroup(msg.to,[target])
#                                        km.leaveGroup(msg.to)
#                                        print (msg.to,[g.mid])
#                                except:
#                                        km.sendText(msg.t,"Ter ELIMINASI....")
#                                        km.sendText(msg.to,"WOLES brooo....!!!")
#                                        km.leaveGroup(msg.to)
#                                        gs = cl.getGroup(msg.to)
#                                        gs.preventJoinByTicket = True
#                                        cl.updateGroup(gs)
#                                        gs.preventJoinByTicket(gs)
#                                        cl.updateGroup(gs)


#===========Mymid Start============
            elif msg.text.lower() in ["!mymid"]:
                middd = "Name : " +cl.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                kr.sendText(msg.to,middd)
#===========Mymid Finish===========

#===========Me Start============
            elif msg.text.lower() in ["!me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
#===========Me Finish===========             


            elif "Apakah " in msg.text:
                apk = msg.text.replace("Apakah ","")
                rnd = ["Ya","Tidak","Mungkin","Bacot","Gue capek ditanya terus"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Hari " in msg.text:
                apk = msg.text.replace("Hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                


            elif "Berapa " in msg.text:
                apk = msg.text.replace("Berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Berapakah " in msg.text:
                apk = msg.text.replace("Berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")                

            elif "Kapan " in msg.text:
                apk = msg.text.replace("Kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah","Tidak tau"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
              if msg.from_ in TidakAktiv:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                cl.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
              if msg.from_ in TidakAktiv:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                cl.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'


 
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
                
            elif "Tr-th " in msg.text:
                isi = msg.text.replace("Tr-th ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)                

            
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
                cl.sendText(msg.to,"==[FROM AR]==\n" + "" + kata + "\n\n==[TO IDN]==\n" + "" + result + "\n\n==[SUKSES]==")


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
 
#===========FRIEND LIST START===========
            elif msg.text in ["!friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="Ini kak teman teman aku (✿◠‿◠)"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════[FRIEND LIST]═════════\n\nTotalnya : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
#===========FRIEND LIST FINISH==========

#===========member list start=============
            elif msg.text in ["!memberlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="[LIST MEMBER]"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n[LIST MEMBER]\n\nTotal Membernya ada : %i kak \nΣ(*ﾉ´>ω<｡`)ﾉ" % len(group)
                cl.sendText(msg.to, msgs)
#===========member list finish============

 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
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
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendText(msg.to,path)
 
#===========getname @ Start===================
            elif "!getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "Ini kak nama copy'an si doi\n°˖✧◝(⁰▿⁰)◜✧˖°\n\n" + contact.displayName)
                except:
                    cl.sendText(msg.to, "Ini kak nama copy'an si doi\n°˖✧◝(⁰▿⁰)◜✧˖°\n\n" + contact.displayName)
#===========getname @ Finish===================


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)

#===========getinfo @ Start===================
            elif "getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid Maav kak nomor MIDnya si doi harus ketik 「!mymid」 :\n" + "\n\nBio :\n" + contact.statusMessage + "\n\nGambar Profile :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\nMaav kak nomor MIDnya si doi harus ketik 「!mymid」 " + "\n\nBio :\n" + contact.statusMessage + "\n\nGambar Profile :\n" + str(cu))
#===========getinfo @ Finish==================


#===========getbio @ Start==================
            elif "!getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "Ini kak bionya （＊〇□〇）……！\n\n" + contact.statusMessage)
                except:
                    cl.sendText(msg.to, "Ini kak bionya （＊〇□〇）……！\n\n" + contact.statusMessage)
#===========getbio @ Finish=================


#==========RUNTIME START============
            elif msg.text.lower() == '!runtime':
                eltime = time.time() - mulai
                van = "Aku sudah aktiv selama :\n\n"+waktu(eltime)+"\nItu Kak\n☆ミヾ(∇≦((ヾ(≧∇≦)〃))≧∇)ノ彡☆"
                cl.sendText(msg.to,van)
#==========RUNTIME FINISH===========
                
                 

#===========Checkdate start==============
            elif "!checkdate " in msg.text:
                tanggal = msg.text.replace("!checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                cl.sendText(msg.to,"Ini kak informasi tanggal lahirnya\n\n"+"Tanggal lahir : "+lahir+"\nUmur : "+usia+"\nUlang tahun : "+ultah+"\nZodiak : "+zodiak+"\n(((o(*ﾟ▽ﾟ*)o)))")
#===========Checkdate finish=============
                
   
#===========Kalender start===============
            elif msg.text in ["!kalender"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst ="Kaka tanya kalender?\nSekarang Hari " + hasil + "" + inihari.strftime('%d') + " Bulan " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst) 
#===========Kalender Finish==============               
                 
                
#===========searchid start=============
            elif "!searchid: " in msg.text:
                userid = msg.text.replace("!searchid: ","")
                contact = cl.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                cl.sendMessage(msg) 
#===========searchid finish============     
                
                
#===========REMOVE CHAT START============
            elif "removechat" in msg.text.lower():
                if msg.from_ in Creator:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Chatnya sudah bersih\nd=(´▽｀)=b")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")  
#===========REMOVE CHAT FINISH===========     
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in TidakAktiv:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            ki.findAndAddContactsByMid(msg.from_)
                            kk.findAndAddContactsByMid(msg.from_)
                            kc.findAndAddContactsByMid(msg.from_)
                            kr.findAndAddContactsByMid(msg.from_)
                            random.choice(KAC).inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")
                else:
                  msg.contentType = 13
                  msg.contentMetadata = {'mid': "ua5f2cbc325816777be5ef529eb920c50"}
                  cl.sendText(msg.to,"member atau admin tidak dapat menggunakan perintah ini")
                  cl.sendText(msg.to,"Hubungi owner dibawah ini untuk mendapatkan informasi lebih lanjut")
                  cl.sendMessage(msg)


#===========GROUP LIST START==========
            elif msg.text in ["!glist"]:
              if msg.from_ in Creator:
                cl.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠❂➣ " + "%s\n" % (cl.getGroup(i).name +" ~> ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╔═════════════════════════\n║ Ini kak group listnya ☚(ﾟヮﾟ☚)\n╠═════════════════════════\n" + h + "╠═════════════════════════" + "\n║ Totalnya =" +" ["+str(len(gid))+"]\n╚═════════════════════════")
#===========GROUP LIST FINISH=========

#===========GROUP ID LIST START============
            elif msg.text in ["!group id"]:
                if msg.from_ in Creator:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                    cl.sendText(msg.to,h)
#===========GROUP ID LIST FINISH===========

            elif "Google: " in msg.text:
                if msg.from_ in TidakAktiv:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"Sedang Mencari...")
                    cl.sendText(msg.to, "https://www.google.com/" + b)
                    cl.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in TidakAktiv:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in TidakAktiv:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Acc invite"]:
                if msg.from_ in TidakAktiv:
                    gid = cl.getGroupIdsInvited()
                    gid = ki.getGroupIdsInvited()
                    gid = kk.getGroupIdsInvited()
                    gid = kc.getGroupIdsInvited()
                    gid = kr.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            gids = ki.getGroup(i)
                            gids = kk.getGroup(i)
                            gids = kc.getGroup(i)
                            gids = kr.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                            ki.acceptGroupInvitation(i)
                            kk.acceptGroupInvitation(i)
                            kc.acceptGroupInvitation(i)
                            kr.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")           


        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

