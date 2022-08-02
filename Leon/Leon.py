import pythoncom
import os
import numpy as np
import cv2
from PIL import ImageGrab
#from playsound import playsound
import speech_recognition as sr
#from gtts import gTTS
import time
import pyaudio
import datetime
import subprocess
import pyttsx3
import webbrowser
import wikipedia
import datetime
from random import seed
from random import random
import os,random
from tkinter.filedialog import askdirectory
import tkinter
import sys
import pygame
from os import listdir
from os.path import isfile, join
import random
from pygame.locals import *
import pygame as pg
from pygame import mixer
import pygame.mixer
from pathlib import Path
import socket
import platform
import requests
import pyautogui

listOfSongs = list()

randSong = 0

directory = ""

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
mach = platform.machine() # x64 or x86
version = platform.version() # version
plat = platform.platform() # Windows surumu
cpu = str(os.cpu_count()) #  CPU number
arch = str(platform.architecture()) # Processor

ye = "For yes please enter 1"

na = "For no please enter 2"
def setDirectory(): #set directory of folder containing .mp3 files.
    global directory
    window = tkinter.Tk()
    window.withdraw()
    directory = askdirectory()

def ToTime():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<4:
        speak("Good afternoon")
    else:
        speak("Good Evening")

def speak(text): # We have to  put a text into speak whenever we call it for example speak("Say hello to the world")
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

def screenrecorder():
	home = str(Path.home())
	path = os.path.join(home, "Desktop\MyRecord.avi")
	screen_size=(1920,1080)
	fourcc= cv2.VideoWriter_fourcc(*"XVID")
	out = cv2.VideoWriter(path, fourcc,20.0,(screen_size))

	while True:
		img = pyautogui.screenshot()
		frame = np.array(img)
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		out.write(frame)
		cv2.imshow("show", frame)
		if cv2.waitKey(1) == ord("q"):
			break
def Assistant():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		audiotext = ""

		try:
			audiotext = r.recognize_google(audio)
			print("You said : " + audiotext)
		except Exception as e:
			speak("")

	return audiotext

def notepad(text):
	date = datetime.datetime.now()
	file_name = str(date).replace(":", "-") + "-note.txt"
	with open(file_name, "w") as f:
		f.write(text)
	
	subprocess.Popen(["notepad.exe", file_name])

WAKE_UP = "hey core"

ToTime()

speak("Hello my name is Leon," + "\nHow may I help you today?")

while True:
	letm = Assistant().lower()

	if "exit" in letm or "quit" in letm:
			quit()

	elif "my pc information" in letm:
		mhome = str(Path.home())
		mpath = os.path.join(mhome, "Desktop\MyPcInfo.txt")
		with open(mpath, "w+") as f:
			f.write("\nHostname: " + hostname)
			#f.write("\nIp: " + IP)
			f.write("\nMachine: " + mach)
			f.write("\nVersion: " + version)
			f.write("\nPlatform: " + plat)
			f.write("\nCPU: " + cpu)
			f.write("\nArchitecture: " + arch)
			f.close()
		speak("I saved you computer's informations to your Desktop")
	NOTE_MAKER = ["make a note", "write this down","make note", "write down"] # Whenever you say one of these words it is going to make note
	for phrase in NOTE_MAKER:
		if phrase in letm:
			homee = str(Path.home())
			ppath = os.path.join(homee, "Desktop\YourNote.txt")
			speak("What would you want me to write down?")
			mk = sr.Recognizer()
			with sr.Microphone() as soouurce:
				auuddio = mk.listen(soouurce)
				try:
					tteext = mk.recognize_google(auuddio)
				except:
					speak("Sorry, I could not understand it")
			with open(ppath, "w+") as f:
				my_note = str(tteext)
				f.write(my_note)
				f.close()
			speak("Your note is:" + my_note)
			#notepad(tteext)
			speak("I've done it for you...")
	
	OPEN_BROWSER = ["open browser","surf on Google","Google"] # Whenever you say one of these words it is going to open you main browser
	for phrase in OPEN_BROWSER:
		if phrase in letm:
			webbrowser.open("www.google.com")

	OPEN_YT = ["open youtube", "i want to watch video", "i am bored","watch video","open YouTube","YouTube"] # Whenever you say one of these words it is going to open YouTube
	for phrase in OPEN_YT:
		if phrase in letm:
			webbrowser.open("www.youtube.com")

	OPEN_FCBK = ["open facebook","open Facebook"] # Whenever you say one of these words it is going to open Facebook
	OPEN_INSTA = ["open Instagram","open instagram"] # Whenever you say one of these words it is going to open Instagram
	for phrase in OPEN_FCBK:
		if phrase in letm:
			webbrowser.open("www.facebook.com")
	for phrase in  OPEN_INSTA:
		if phrase in letm:
			webbrowser.open("www.instagram.com")
	if "wikipedia" in letm:
			speak("searching in wikipedia")
			letm = letm.replace("wikipedia", "")
			results = wikipedia.summary(letm, sentences = 2)
			speak("According to wikipedia")
			print(results)
			speak(results)

	OPEN_TWTR = ["open twitter", "open Twitter"]
	for phrase in OPEN_TWTR:
		if phrase in letm:
			webbrowser.open("https://twitter.com/explore")

	if "thank you" in letm:
		speak("Your welcome")

	elif "how are you" in letm:
		speak("I am good. Thanks for asking. How about you?")

	elif "i am good" in letm or "i'm good" in letm:
		speak("I am happy for you")

	elif "I'm good" in letm:
		speak("I am happy for you")

	elif "i am bad" in letm or "i'm bad" in letm:
		speak("I am feeling sorry for you")

	elif "start recording" in letm:
		screenrecorder()

	elif"take screenshot" in letm:
		home = str(Path.home())
		path = os.path.join(home, "Desktop\Screenshot.png")
		shot = pyautogui.screenshot()
		shot.save(path)
		speak("I took screenshot")

	elif "what is my ip" in letm:
		speak("Your IP address is on your screen.")
		os.system("ipconfig")

	elif "cmd color options" in letm:
		message = """
		0 = Black   ,    8 = Gray
		1 = Blue    ,    9 = Light Blue
		2 = Green   ,    A = Light Green
		3 = Aqua    ,    B = Light Aqua
		4 = Red     ,    C = Light Red
		5 = Purple  ,    D = Light Purple
		6 = Yellow  ,    E = Light Yellow
		7 = White   ,    F = Bright White
		"""
		print(message)
		speak(message)

	elif "create html" in letm:
		speak("Ok I am creating an HTMl file")
		home = str(Path.home())
		path = os.path.join(home, "Desktop\sample.html")
		with open(path, "w+") as f:
			code = """

<html>
<head>
	<link rel="stylesheet" type="text/css" href="sample.css">
	<title>Sample Site</title>
</head>
<body>
    <h1 style="text-align: center"><span style="color: #117A65">Welcome to Sample HTML</span></h1>
    <b><p style="text-align: center"><span style="color: #3498DB">You can edit this website if you order Leon to</span><span style="color: firebrick">"create CSS"</span><span style="color: #3498DB"> you can make this website look better</span></p></b>
    <a href="Leon\Image\image.jpg" width="500" height="500" style="align-content: center">
        <img src= "Leon\Image\image.jpg">
    </a>
    <h2 style="text-align: center"><span style="color: #3498DB">For More Help</span></h2>
    <b><p style="text-align: center"><a href="https://www.simpleappsinc.com">simpleappsinc.com</a></p></b>
</body>
</html>
		"""
			f.write(str(code))
			f.close()
		webbrowser.open_new_tab('file:///C:/Users/12162/Desktop/sample.html')

	elif "create css" in letm:
		speak("Ok I am creating CSS file")
		home = str(Path.home())
		path = os.path.join(home, "Desktop\sample.css") 
		with open(path, "w+") as f:
			code = """
html {
    background: #1D2429;
    background-image: linear-gradient(270deg, rgb(29, 36, 41) 0%, rgb(29, 36, 41) 100%);
    -webkit-font-smoothing: antialiased;
}

body {
    background: #fff;
    box-shadow: 0 0 2px rgba(0, 0, 0, 0.06);
    color: #545454;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 16px;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 800px;
    padding: 2em 2em 4em;
}

h1, h2, h3, h4, h5, h6 {
    color: #222;
    font-weight: 600;
    line-height: 1.3;
}

h2 {
    margin-top: 1.3em;
}

a {
    color: black;
}

b, strong {
    font-weight: 600;
}

samp {
    display: none;
}

img {
    animation: colorize 2s cubic-bezier(0, 0, .78, .36) 1;
    background: transparent;
    border: 10px solid rgba(0, 0, 0, 0.12);
    border-radius: 4px;
    display: block;
    margin: 1.3em auto;
    max-width: 95%;
}

@keyframes colorize {
    0% {
        -webkit-filter: grayscale(100%);
        filter: grayscale(100%);
    }
    100% {
        -webkit-filter: grayscale(0%);
        filter: grayscale(0%);
    }
}
			"""
			f.write(str(code))
			f.close()
	
	CLEAN_CMDP = ["clean"]
	for phrase in CLEAN_CMDP:
		if phrase in letm:
			os.system("cls")
	
	INSTL_PCKG = ["install packages"]
	for phrase in INSTL_PCKG:
		if phrase in letm:
			speak("Please enter the package name below")
			package = input(">>>> ")
			speak("Is it" + package)
			speak(ye)
			speak(na)
			answer = int(input(">>>> "))
			if answer == 1:
				os.system("pip install " + package)
				speak("Packages installed succesfully")
			elif answer == 2:
				speak("Please try later")

	if 'open gmail' in letm:
            webbrowser.open("https://mail.google.com/")
            speak("gmail is opened")

	elif "open simple apps" in letm:
		webbrowser.open("https://simpleappsinc.com")
		speak("Simple Apps Inc is opened")

	elif "open outlook" in letm:
		webbrowser.open("https://outlook.live.com/owa/")

	elif 'open apple' in letm:
            webbrowser.open("https://www.apple.com/")
            speak("apple.com is opened")
	
	elif 'play music' in letm:
		#music_dir = '\\Music'
		home = str(Path.home())
		path = os.path.join(home, "Music")
		songs = os.listdir(path)
		print(songs)
		speak("music is being played")
		n = random.randint(0,int(len(songs)-1))
		#for x in range(0,10):
		os.startfile(os.path.join(path, songs[n]))

	elif "create dork list" in letm:
		home = str(Path.home())
		patth = os.path.join(home, "Desktop\Dorks_2020.txt")
		speak("Dork list is being created")
		with open(patth, "w+") as f:
			list_of_dorks_2020 = """
components/com_simpleboard/image_upload.php?sbp=
Computer Science.php?id=
confidential site:mil
config.php
config.php?_CCFG[_PKG_PATH_DBSE]=
ConnectionTest.java filetype:html
constructies/product.php?id=
contact.php?cartId=
contacts ext:wml
contenido.php?sec=
content.php?arti_id=
content.php?categoryId=
content.php?cID=
content.php?cid=
content.php?cont_title=
content.php?id
content.php?id=
content.php?ID=
content.php?p=
content.php?page=
content.php?PID=
content/conference_register.php?ID=
content/detail.php?id=
content/index.php?id=
content/pages/index.php?id_cat=
content/programme.php?ID=
content/view.php?id=
coppercop/theme.php?THEME_DIR=
corporate/newsreleases_more.php?id=
county-facts/diary/vcsgen.php?id=
cps/rde/xchg/tm/hs.xsl/liens_detail.html?lnkId=
cryolab/content.php?cid=
csc/news-details.php?cat=
customer/board.htm?mode=
customer/home.php?cat=
customerService.php?****ID1=
CuteNews" "2003..2005 CutePHP"
data filetype:mdb -site:gov -site:mil
db.php?path_local=
db/CART/product_details.php?product_id=
de/content.php?page_id=
deal_coupon.php?cat_id=
debate-detail.php?id=
declaration_more.php?decl_id=
default.php?*root*=
default.php?abre=
default.php?base_dir=
default.php?basepath=
default.php?body=
default.php?catID=
default.php?channel=
default.php?chapter=
default.php?choix=
default.php?cmd=
default.php?cont=
default.php?cPath=
default.php?destino=
default.php?e=
default.php?eval=
default.php?f=
default.php?goto=
default.php?header=
default.php?inc=
default.php?incl=
default.php?include=
default.php?index=
default.php?ir=
default.php?itemnav=
default.php?k=
default.php?ki=
default.php?l=
default.php?left=
default.php?load=
default.php?loader=
default.php?loc=
default.php?m=
default.php?menu=
default.php?menue=
default.php?mid=
default.php?mod=
default.php?module=
default.php?n=
default.php?name=
default.php?nivel=
default.php?oldal=
default.php?opcion=
default.php?option=
default.php?p=
default.php?pa=
default.php?pag=
default.php?page=
default.php?pageweb=
default.php?panel=
default.php?param=
default.php?play=
default.php?pr=
default.php?pre=
default.php?read=
default.php?ref=
default.php?rub=
default.php?secao=
default.php?secc=
default.php?seccion=
default.php?seite=
default.php?showpage=
default.php?sivu=
default.php?sp=
default.php?str=
default.php?strona=
default.php?t=
default.php?thispage=
default.php?TID=
default.php?tipo=
default.php?to=
default.php?type=
default.php?v=
default.php?var=
default.php?x=
default.php?y=
description.php?bookid=
designcenter/item.php?id=
detail.php?id=
detail.php?ID=
detail.php?item_id=
detail.php?prodid=
detail.php?prodID=
detail.php?siteid=
detailedbook.php?isbn=
details.php?BookID=
details.php?id=
details.php?Press_Release_ID=
details.php?prodId=
details.php?ProdID=
details.php?prodID=
details.php?Product_ID=
details.php?Service_ID=
directory/contenu.php?id_cat=
discussions/10/9/?CategoryID=
display_item.php?id=
display_page.php?id=
display.php?ID=
displayArticleB.php?id=
displayproducts.php
displayrange.php?rangeid=
docDetail.aspx?chnum=
down*.php?action=
down*.php?addr=
down*.php?channel=
down*.php?choix=
down*.php?cmd=
down*.php?corpo=
down*.php?disp=
down*.php?doshow=
down*.php?ev=
down*.php?filepath=
down*.php?goFile=
down*.php?home=
down*.php?in=
down*.php?inc=
down*.php?incl=
down*.php?include=
down*.php?ir=
down*.php?lang=
down*.php?left=
down*.php?nivel=
down*.php?oldal=
down*.php?open=
down*.php?OpenPage=
down*.php?pa=
down*.php?pag=
down*.php?pageweb=
down*.php?param=
down*.php?path=
down*.php?pg=
down*.php?phpbb_root_path=
down*.php?pollname=
down*.php?pr=
down*.php?pre=
down*.php?qry=
down*.php?r=
down*.php?read=
down*.php?s=
down*.php?second=
down*.php?section=
down*.php?seite=
down*.php?showpage=
down*.php?sp=
down*.php?strona=
down*.php?subject=
down*.php?t=
down*.php?texto=
down*.php?to=
down*.php?u=
down*.php?url=
down*.php?v=
down*.php?where=
down*.php?x=
down*.php?z=
download.php?id=
downloads_info.php?id=
downloads.php?id=
downloads/category.php?c=
downloads/shambler.php?id=
downloadTrial.php?intProdID=
Duclassified" -site:duware.com "DUware All Rights reserved"
duclassmate" -site:duware.com
Dudirectory" -site:duware.com
dudownload" -site:duware.com
DUpaypal" -site:duware.com
DWMail" password intitle:dwmail
e_board/modifyform.html?code=
edatabase/home.php?cat=
edition.php?area_id=
education/content.php?page=
eggdrop filetype:user user
Elite Forum Version *.*"
els_/product/product.php?id=
emailproduct.php?itemid=
emailToFriend.php?idProduct=
en/main.php?id=
en/news/fullnews.php?newsid=
en/publications.php?id=
enable password | secret "current configuration" -intext:the
enc/content.php?Home_Path=
eng_board/view.php?T****=
eng/rgboard/view.php?&bbs_id=
english/board/view****.php?code=
english/fonction/print.php?id=
english/print.php?id=
english/publicproducts.php?groupid=
enter.php?a=
enter.php?abre=
enter.php?addr=
enter.php?b=
enter.php?base_dir=
enter.php?body=
enter.php?chapter=
enter.php?cmd=
enter.php?content=
enter.php?e=
enter.php?ev=
enter.php?get=
enter.php?go=
enter.php?goto=
enter.php?home=
enter.php?id=
enter.php?incl=
enter.php?include=
enter.php?index=
enter.php?ir=
enter.php?itemnav=
enter.php?lang=
enter.php?left=
enter.php?link=
enter.php?loader=
enter.php?menue=
enter.php?mid=
enter.php?middle=
enter.php?mod=
enter.php?module=
enter.php?name=
enter.php?numero=
enter.php?open=
enter.php?pa=
enter.php?page=
enter.php?pagina=
enter.php?panel=
enter.php?path=
enter.php?pg=
enter.php?phpbb_root_path=
enter.php?play=
enter.php?pname=
enter.php?pr=
enter.php?pref=
enter.php?qry=
enter.php?r=
enter.php?read=
enter.php?ref=
enter.php?s=
enter.php?sec=
enter.php?second=
enter.php?seite=
enter.php?sivu=
enter.php?sp=
enter.php?start=
enter.php?str=
enter.php?strona=
enter.php?subject=
enter.php?texto=
enter.php?thispage=
enter.php?type=
enter.php?viewpage=
enter.php?w=
enter.php?y=
etc (index.of)
event_details.php?id=
event_info.php?p=
event.php?id=
events?id=
events.php?ID=
events/detail.php?ID=
events/event_detail.php?id=
events/event.php?id=
events/event.php?ID=
events/index.php?id=
events/unique_event.php?ID=
exhibition_overview.php?id=
exhibitions/detail.php?id=
exported email addresses
ext:txt inurl:dxdiag
ext:txt inurl:unattend.txt
ext:vmdk vmdk
ext:vmx vmx
ext:yml database inurl:config
ez Publish administration
faq_list.php?id=
faq.php?cartID=
faq2.php?id=
faqs.php?id=
fatcat/home.php?view=
feature.php?id=
features/view.php?id=
feedback.php?title=
fellows.php?id=
FernandFaerie/index.php?c=
fiche_spectacle.php?id=
Fichier contenant des informations sur le r?seau :
file.php?action=
file.php?basepath=
file.php?body=
file.php?channel=
file.php?chapter=
file.php?choix=
file.php?cmd=
file.php?cont=
file.php?corpo=
file.php?disp=
file.php?doshow=
file.php?ev=
file.php?eval=
file.php?get=
file.php?id=
file.php?inc=
file.php?incl=
file.php?include=
file.php?index=
file.php?ir=
file.php?ki=
file.php?left=
file.php?load=
file.php?loader=
file.php?middle=
file.php?modo=
file.php?n=
file.php?nivel=
file.php?numero=
file.php?oldal=
file.php?pagina=
file.php?param=
file.php?pg=
file.php?play=
file.php?pollname=
file.php?pref=
file.php?q=
file.php?qry=
file.php?ref=
file.php?seccion=
file.php?second=
file.php?showpage=
file.php?sivu=
file.php?sp=
file.php?start=
file.php?strona=
file.php?texto=
file.php?to=
file.php?type=
file.php?url=
file.php?var=
file.php?viewpage=
file.php?where=
file.php?y=
filemanager.php?delete=
filetype:asp "Custom Error Message" Category Source
filetype:asp + "[ODBC SQL"
filetype:ASP ASP
filetype:asp DBQ=" * Server.MapPath("*.mdb")
filetype:ASPX ASPX
filetype:bak createobject sa
filetype:bak inurl:"htaccess|passwd|shadow|htusers"
filetype:bkf bkf
filetype:blt "buddylist"
filetype:blt blt +intext:screenname
filetype:BML BML
filetype:cfg auto_inst.cfg
filetype:cfg ks intext:rootpw -sample -test -howto
filetype:cfg mrtg "target
filetype:cfm "cfapplication name" password
filetype:CFM CFM
filetype:CGI CGI
filetype:cgi inurl:"fileman.cgi"
filetype:cgi inurl:"Web_Store.cgi"
filetype:cnf inurl:_vti_pvt access.cnf
filetype:conf inurl:firewall -intitle:cvs
filetype:conf inurl:psybnc.conf "USER.PASS="
filetype:conf oekakibbs
filetype:conf slapd.conf
filetype:config config intext:appSettings "User ID"
filetype:config web.config -CVS
filetype:ctt Contact
filetype:ctt ctt messenger
filetype:dat "password.dat
filetype:dat "password.dat"
filetype:dat inurl:Sites.dat
filetype:dat wand.dat
filetype:DIFF DIFF
filetype:DLL DLL
filetype:DOC DOC
filetype:eml eml +intext:"Subject" +intext:"From" +intext:"To"
filetype:FCGI FCGI
filetype:fp3 fp3
filetype:fp5 fp5 -site:gov -site:mil -"cvs log"
filetype:fp7 fp7
filetype:HTM HTM
filetype:HTML HTML
filetype:inc dbconn
filetype:inc intext:mysql_connect
filetype:inc mysql_connect OR mysql_pconnect
filetype:inf inurl:capolicy.inf
filetype:inf sysprep
filetype:ini inurl:"serv-u.ini"
filetype:ini inurl:flashFXP.ini
filetype:ini ServUDaemon
filetype:ini wcx_ftp
filetype:ini ws_ftp pwd
filetype:JHTML JHTML
filetype:JSP JSP
filetype:ldb admin
filetype:lic lic intext:key
filetype:log "PHP Parse error" | "PHP Warning" | "PHP Error"
filetype:log "See `ipsec --copyright"
filetype:log access.log -CVS
filetype:log cron.log
filetype:log intext:"ConnectionManager2"
filetype:log inurl:"password.log"
filetype:log inurl:password.log
filetype:mbx mbx intext:Subject
filetype:mdb inurl:users.mdb
filetype:mdb wwforum
filetype:MV MV
filetype:myd myd -CVS
filetype:netrc password
filetype:ns1 ns1
filetype:ora ora
filetype:ora tnsnames
filetype:pass pass intext:userid
filetype:pdb pdb backup (Pilot | Pluckerdb)
filetype:pdf "Assessment Report" nessus
filetype:PDF PDF
filetype:pem intext:private
filetype:php inurl:"logging.php" "Discuz" error
filetype:php inurl:"webeditor.php"
filetype:STM STM
filetype:SWF SWF
filetype:TXT TXT
filetype:url +inurl:"ftp://" +inurl:";@"
filetype:vcs vcs
filetype:vsd vsd network -samples -examples
filetype:wab wab
filetype:xls -site:gov inurl:contact
filetype:xls inurl:"email.xls"
filetype:xls username password email
filetype:XLS XLS
Financial spreadsheets: finance.xls
Financial spreadsheets: finances.xls
folder.php?id=
forum_bds.php?num=
forum.php?act=
forum/profile.php?id=
forum/showProfile.php?id=
fr/commande-liste-categorie.php?panier=
free_board/board_view.html?page=
freedownload.php?bookid=
front/bin/forumview.phtml?bbcode=
frontend/category.php?id_category=
fshstatistic/index.php?PID=
fullDisplay.php?item=
FullStory.php?Id=
galerie.php?cid=
Gallery in configuration mode
gallery.php?*[*]*=
gallery.php?abre=
gallery.php?action=
gallery.php?addr=
gallery.php?base_dir=
gallery.php?basepath=
gallery.php?chapter=
gallery.php?cont=
gallery.php?corpo=
gallery.php?disp=
gallery.php?ev=
gallery.php?eval=
gallery.php?filepath=
gallery.php?get=
gallery.php?go=
gallery.php?h=
gallery.php?id=
gallery.php?index=
gallery.php?itemnav=
gallery.php?ki=
gallery.php?left=
gallery.php?loader=
gallery.php?menu=
gallery.php?menue=
gallery.php?mid=
gallery.php?mod=
gallery.php?module=
gallery.php?my=
gallery.php?name=
gallery.php?nivel=
gallery.php?oldal=
gallery.php?open=
gallery.php?option=
gallery.php?pag=
gallery.php?page=
gallery.php?pageweb=
gallery.php?panel=
gallery.php?param=
gallery.php?pg=
gallery.php?phpbb_root_path=
gallery.php?pname=
gallery.php?pollname=
gallery.php?pre=
gallery.php?pref=
gallery.php?qry=
gallery.php?redirect=
gallery.php?ref=
gallery.php?rub=
gallery.php?sec=
gallery.php?secao=
gallery.php?seccion=
gallery.php?seite=
gallery.php?showpage=
gallery.php?sivu=
gallery.php?sp=
gallery.php?strona=
gallery.php?thispage=
gallery.php?tipo=
gallery.php?to=
gallery.php?url=
gallery.php?var=
gallery.php?viewpage=
gallery.php?where=
gallery.php?xlink=
gallery.php?y=
gallery/detail.php?ID=
gallery/gallery.php?id=
gallerysort.php?iid=
game.php?id=
games.php?id=
Ganglia Cluster Reports
garden_equipment/Fruit-Cage/product.php?pr=
garden_equipment/pest-weed-control/product.php?pr=
gb/comment.php?gb_id=
general.php?abre=
general.php?addr=
general.php?adresa=
general.php?b=
general.php?base_dir=
general.php?body=
general.php?channel=
general.php?chapter=
general.php?choix=
general.php?cmd=
general.php?content=
general.php?doshow=
general.php?e=
general.php?f=
general.php?get=
general.php?goto=
general.php?header=
general.php?id=
general.php?inc=
general.php?include=
general.php?ir=
general.php?itemnav=
general.php?left=
general.php?link=
general.php?menu=
general.php?menue=
general.php?mid=
general.php?middle=
general.php?modo=
general.php?module=
general.php?my=
general.php?name=
general.php?nivel=
general.php?opcion=
general.php?p=
general.php?page=
general.php?pageweb=
general.php?pollname=
general.php?pr=
general.php?pre=
general.php?qry=
general.php?read=
general.php?redirect=
general.php?ref=
general.php?rub=
general.php?secao=
general.php?seccion=
general.php?second=
general.php?section=
general.php?seite=
general.php?sekce=
general.php?sivu=
general.php?strona=
general.php?subject=
general.php?texto=
general.php?thispage=
general.php?tipo=
general.php?to=
general.php?type=
general.php?var=
general.php?w=
general.php?where=
general.php?xlink=
getbook.php?bookid=
GetItems.php?itemid=
giftDetail.php?id=
gig.php?id=
global_projects.php?cid=
global/product/product.php?gubun=
gnu/?doc=
goboard/front/board_view.php?code=
goods_detail.php?data=
haccess.ctl (one way)
haccess.ctl (VERY reliable)
hall.php?file=
hall.php?page=
Hassan Consulting's Shopping Cart Version 1.18
head.php?*[*]*=
head.php?abre=
head.php?adresa=
head.php?b=
head.php?base_dir=
head.php?c=
head.php?choix=
head.php?cmd=
head.php?content=
head.php?corpo=
head.php?d=
head.php?dir=
head.php?disp=
head.php?ev=
head.php?filepath=
head.php?g=
head.php?goto=
head.php?inc=
head.php?incl=
head.php?include=
head.php?index=
head.php?ir=
head.php?ki=
head.php?lang=
head.php?left=
head.php?load=
head.php?loader=
head.php?loc=
head.php?middle=
head.php?middlePart=
head.php?mod=
head.php?modo=
head.php?module=
head.php?numero=
head.php?oldal=
head.php?opcion=
head.php?pag=
head.php?pageweb=
head.php?play=
head.php?pname=
head.php?pollname=
head.php?read=
head.php?ref=
head.php?rub=
head.php?sec=
head.php?sekce=
head.php?sivu=
head.php?start=
head.php?str=
head.php?strona=
head.php?tipo=
head.php?viewpage=
head.php?where=
head.php?y=
help.php?CartId=
help.php?css_path=
help/com_view.html?code=
historialeer.php?num=
HistoryStore/pages/item.php?itemID=
hm/inside.php?id=
home.php?a=
home.php?action=
home.php?addr=
home.php?base_dir=
home.php?basepath=
home.php?body=
home.php?cat=
home.php?category=
home.php?channel=
home.php?chapter=
home.php?choix=
home.php?cmd=
home.php?content=
home.php?disp=
home.php?doshow=
home.php?e=
home.php?ev=
home.php?eval=
home.php?g=
home.php?h=
home.php?id=
home.php?ID=
home.php?in=
home.php?include=
home.php?index=
home.php?ir=
home.php?itemnav=
home.php?k=
home.php?link=
home.php?loader=
home.php?loc=
home.php?menu=
home.php?middle=
home.php?middlePart=
home.php?module=
home.php?my=
home.php?oldal=
home.php?opcion=
home.php?pa=
home.php?page=
home.php?pageweb=
home.php?pagina=
home.php?panel=
home.php?path=
home.php?play=
home.php?pollname=
home.php?pr=
home.php?pre=
home.php?qry=
home.php?read=
home.php?recipe=
home.php?redirect=
home.php?ref=
home.php?rub=
home.php?sec=
home.php?secao=
home.php?section=
home.php?seite=
home.php?sekce=
home.php?showpage=
home.php?sp=
home.php?str=
home.php?thispage=
home.php?tipo=
home.php?w=
home.php?where=
home.php?x=
home.php?z=
homepage.php?sel=
hosting_info.php?id=
ht://Dig htsearch error
html/print.php?sid=
html/scoutnew.php?prodid=
htmlpage.php?id=
htmltonuke.php?filnavn=
htpasswd
htpasswd / htgroup
htpasswd / htpasswd.bak
humor.php?id=
i-know/content.php?page=
ibp.php?ISBN=
ICQ chat logs, please...
idlechat/message.php?id=
ihm.php?p=
IIS 4.0 error messages
IIS web server error messages
IlohaMail"
impex/ImpExData.php?systempath=
			"""
			f.write(str(list_of_dorks_2020))
			f.close()
		speak("Dorks are ready to use.")

	FIRST_SAY = ["hi", "hello"]
	for phrase in FIRST_SAY:
		if phrase in letm:
			speak("Hello")

	OPN_RDIO = ["open radio", "radio music", "radio", "online song"] # Whenever you say one of these words it is going to open Online Radio
	for phrase in OPN_RDIO:
		if phrase in letm:
			speak("I am openning radio for you")
			webbrowser.open("https://www.iheart.com/for-you/")

	OPN_CMD = ["open cmd"]
	for phrase in OPN_CMD:
		if phrase in letm:
			os.system("start cmd")

	if "what is your name" in letm or "who are you" in letm:
		speak("My name is Leon")

	PING_LIST = ["hack","ping","ddos"]
	for phrase in PING_LIST:
		if phrase in letm:
			speak("PLease enter the url")
			url = input(">>>> ")
			speak(url + "Is that right?")
			
			speak("For yes please enter 1")
			speak("For no please enter 2")
			
			bb = 0
			xx = int(input(">>>> "))
			if xx == 1:
				os.system("color a")
				speak("How many times do you want it to run?" + "Please enter it below in integer form.")
				aa = int(input(">>>> "))
				#webbrowser.open("https://www.youtube.com/watch?v=gyqJXCqiZhQ")
				speak("I am going to run it " + str(aa) + "times")
				#playsound("C:\\Users\\12162\\Desktop\\Leon\\leon_music\\hack.mp3")
				"""
				music_dr = 'C:\\Users\\12162\\Desktop\\Leon\\leon_music'
				song = os.listdir(music_dr)
				print(song)
				speak("Music is being played")
				os.startfile(os.path.join(music_dr, song[0]))
				"""
				while (aa >= 0):
					os.system("ping " + url)
					aa -= 1
					if aa == -1:
						os.system("color 7")
			elif xx == 2:
				speak("Sorry I can't do it right now")

	GOOGLE_SEARCH= ["search on Google","search on google","make a search on Google"] # Whenever you say one of these words it is going to search any word you said on Google
	for phrase in GOOGLE_SEARCH:
		if phrase in letm:
			sr.Microphone(device_index=1)
			r=sr.Recognizer()
			r.energy_threshold=5000
			with sr.Microphone() as source:
				speak("What do you want to search on google")
				audio=r.listen(source)
				try:
					text=r.recognize_google(audio)
					speak("You said : {}".format(text))
					url='https://www.google.co.in/search?q='
					search_url=url+text
					webbrowser.open(search_url)
				except:
					speak("Can't recognize")

	WOLFRAM_SEARCH = ["search on wolfram"]
	for phrase in WOLFRAM_SEARCH:
		if phrase in letm:
			r = sr.Microphone(device_index = 1)
			r = sr.Recognizer()
			r.energy_threshold = 5000
			with sr.Microphone() as source:
				speak("What do you want to search on WOLFRAM ALPHA")
				audio = r.listen(source)
				try:
					text = r.recognize_google(audio)
					speak("You said {}".format(text))
					url = 'https://www.wolframalpha.com/input/?i='
					search_url = url+text
					webbrowser.open(search_url)
				except:
					speak("I can't search it right now!")