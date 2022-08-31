import tkinter as tk
import datetime
import xml.etree.ElementTree as ET
import codecs
import urllib.request, urllib.parse, urllib.error
from urllib.parse import quote
import re
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import Text
import PIL
from PIL import ImageTk, Image
import os
import codecs
import sys
from tkinter.font import Font
import requests
import json


icon='''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'''
def EE():
    
    words=ent.get()
    word_list=words.split(' ')
    
        
        
    content=''

    #################################################
    app_id = '6a82c3bd'
    app_key = '660d8c2da9bf7ff86c55b66b34510a0f'
    language = 'en'
    for word in word_list:
        word_id=word
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        js=r.json()
        print (word)
        subcontent=''
        results_list=js['results']
        lexicalEntries_list=results_list[0]["lexicalEntries"]


        pronunciations_list=lexicalEntries_list[0]["pronunciations"]
        for dic in pronunciations_list:
            for k in dic:
                if k == "phoneticSpelling":
                    pronunciation=dic["phoneticSpelling"]
    
        for item in lexicalEntries_list:    
            defin_list=[]    
            count=1    
            for k in item:
                if k == "entries":
                    entries_list=item["entries"]            
                    for dic in entries_list:
                        for k in dic:
                            if k == "senses":
                                senses_list=dic["senses"]                        
                                for dic in senses_list:                               
                                #for k in dic:
                                    if "definitions" in dic:
                                        defin_list.append(str(count)+'. '+dic['definitions'][0])
                                        count=count+1
                                    if "examples" in dic:
                                        examples_list=dic["examples"]
                                        for dic in examples_list:
                                            for k in dic:
                                                if k == "text":
                                                    defin_list.append('"'+dic['text']+'"')                                                   
                                
                                for dic in senses_list:                                                                                    
                                    if "subsenses" in dic:                                    
                                        subsenses_list=dic["subsenses"]                                    
                                        for dic in subsenses_list:
                                            for k in dic:                                            
                                                if k == "definitions":                                                
                                                    defin_list.append(str(count)+'. '+dic["definitions"][0])
                                                    count=count+1
                                                if k == "examples":
                                                    examples_list=dic["examples"]
                                                    for dic in examples_list:
                                                        for k in dic:
                                                            if k == "text":
                                                                defin_list.append('"'+dic['text']+'"')
                                                                
            part_of_speech=item["lexicalCategory"]           
            subcontent=subcontent+'\n'+part_of_speech+'\n'
            for defin in defin_list:
                subcontent=subcontent+defin+'\n'
            subcontent=subcontent+'\n'        
        content=content+word+'   '+'/'+pronunciation+'/'+'\n'+subcontent+'\n-------------\n'
    t.insert(END,content)         
   

def EC():
    
    words=ent.get()
    word_list=words.split(' ')      
        
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    
    for word in word_list:
                       
        url='https://tw.dictionary.search.yahoo.com/search?p='+ word
        req=urllib.request.Request(url,headers=headers)
        html=urllib.request.urlopen(req)
        doc=html.read()
        read=doc.decode('utf-8','ignore')
        soup=BeautifulSoup (doc,'html.parser')  
                
        
        tag=soup.find(attrs={"class":"fz-14"})
        
        
        try:
            line=tag.get_text()
            if line.startswith("KK"):               
                pho=line
            
            else:
                pho='NULL'
        except:
            continue


        defin_list=[]

        #main explanation!!
            
        try:
            tag2=soup.find_all(attrs={"class":"dictionaryExplanation"})
            for tag in tag2:
                line2=tag.get_text()
                defin_list.append('[Main]'+line2)
                    
        except:
            continue

        #main explanation!!
            
        try:
            tag3=soup.find_all(attrs={"class":"fz-14"})
            
            for tag in tag3:
                line3=tag.get_text()
                if re.search('^[0-9]',line3) and len(line3) >=3:
                #if '[' not in line3:
                    defin_list.append(line3)
                else:
                    continue                
        except:
            continue

        t.insert(END,'---------------'+'\n'+word+'\n'+pho+'\n'+'\n')
        
        for defin in defin_list:
            t.insert(END, defin+'\n')
            
    t.insert(END,'-------------------')


def CE():

    words=ent.get()
    word_list=words.split(' ')
   
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"  
    
    for word in word_list:   
        
        url='https://tw.dictionary.search.yahoo.com/search?p='+quote(word)
        req=urllib.request.Request(url,headers=headers)
        html=urllib.request.urlopen(req)            
        doc=html.read()
        read=doc.decode('utf-8','ignore')
        soup=BeautifulSoup (doc,'html.parser')            
        
            
        defin_list=[]

             #main explanation!!
            
        try:
            tag2=soup.find(attrs={"class":"dictionaryExplanation"})            
            line2=tag2.get_text()
            defin_list.append(line2)             
                    
                    
        except:
            continue

            #main explanation!!
            
        t.insert(END,'---------------'+'\n'+word+'\n'+'\n')
        
        for defin in defin_list:
            t.insert(END, defin+'\n')
            
    t.insert(END,'-------------------')

def WK_EE():
    words=ent.get()
    word_list=words.split(' ')

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0" 
        
    for word in word_list:
        try: 
            url='https://en.wikipedia.org/wiki/'+word
            req=urllib.request.Request(url,headers=headers)
            html=urllib.request.urlopen(req)
            html=urllib.request.urlopen(url)
            doc=html.read()
            read=doc.decode('utf-8','ignore')
            soup=BeautifulSoup (doc,'html.parser')      
            tags=soup.find_all('p')
            defin_list=[]
            defin_list2=[]
            re='may refer to'
            for tag in tags:
                defin=tag.get_text()
                if re in defin:
                    defin_list.append(defin)
                    tags2=soup.find_all(title=True)
                    for tag in tags2:
                        if tag.get_text() == tag['title']:
                            defin=tag.get_text()
                            defin_list2.append(defin)
                                        
                elif defin !='':                    
                    defin_list.append(defin)
                    
            for defin in defin_list[:5]:
                t.insert(END,'\n'+defin+'\n'+'\n')
                    
            for defin in defin_list2:
                t.insert(END,'\n'+defin+'\n'+'\n')
            t.insert(END, '-------------------------------------------------------------\n')
                       
        except:
            continue     
    
               

def WK_EC():
    words=ent.get()
    word_list=words.split(' ')

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0" 
    urlzh=[]
    
    for word in word_list:
        url='https://en.wikipedia.org/wiki/'+word
        req=urllib.request.Request(url,headers=headers)
        html=urllib.request.urlopen(req)
        html=urllib.request.urlopen(url)
        doc=html.read()
        read=doc.decode('utf-8','ignore')
        soup=BeautifulSoup (doc,'html.parser')      
        tags=soup.find_all('a')       
    
        
        try:
            for tag in tags:
                if tag.get_text() == '中文':
                    urlzh.append(tag['href'])
        except:
            continue
    
    for url in urlzh:
        req=urllib.request.Request(url,headers=headers)
        html=urllib.request.urlopen(req)
        html=urllib.request.urlopen(url)
        doc=html.read()
        read=doc.decode('utf-8','ignore')
        soup=BeautifulSoup (doc,'html.parser')      
        tags=soup.find_all('p')
        defin_list=[]
        for tag in tags:
            defin=tag.get_text()
            if defin != '':
                defin_list.append(defin)    
        for defin in defin_list[:5]:
            
            t.insert(END,'\n'+defin+'\n'+'\n')
        t.insert(END,'----------------------------------------------------------'+'\n')

def QEE():
    
    words=ent.get()
    word_list=words.split(' ')
    
        
        
    content=''

    #################################################
    app_id = '6a82c3bd'
    app_key = '660d8c2da9bf7ff86c55b66b34510a0f'
    language = 'en'
    for word in word_list:
        word_id=word
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        js=r.json()
        print (word)
        subcontent=''
        results_list=js['results']
        lexicalEntries_list=results_list[0]["lexicalEntries"]


        pronunciations_list=lexicalEntries_list[0]["pronunciations"]
        for dic in pronunciations_list:
            for k in dic:
                if k == "phoneticSpelling":
                    pronunciation=dic["phoneticSpelling"]
    
        for item in lexicalEntries_list:    
            defin_list=[]    
            count=1    
            for k in item:
                if k == "entries":
                    entries_list=item["entries"]            
                    for dic in entries_list:
                        for k in dic:
                            if k == "senses":
                                senses_list=dic["senses"]                        
                                for dic in senses_list:                               
                                #for k in dic:
                                    if "definitions" in dic:
                                        defin_list.append(str(count)+'. '+dic['definitions'][0])
                                        count=count+1
                                    if "examples" in dic:
                                        examples_list=dic["examples"]
                                        for dic in examples_list:
                                            for k in dic:
                                                if k == "text":
                                                    defin_list.append('"'+dic['text']+'"')                                                   
                                
                                for dic in senses_list:                                                                                    
                                    if "subsenses" in dic:                                    
                                        subsenses_list=dic["subsenses"]                                    
                                        for dic in subsenses_list:
                                            for k in dic:                                            
                                                if k == "definitions":                                                
                                                    defin_list.append(str(count)+'. '+dic["definitions"][0])
                                                    count=count+1
                                                if k == "examples":
                                                    examples_list=dic["examples"]
                                                    for dic in examples_list:
                                                        for k in dic:
                                                            if k == "text":
                                                                defin_list.append('"'+dic['text']+'"')
                                                        
            part_of_speech=item["lexicalCategory"]           
            subcontent=subcontent+' ['+part_of_speech+'] '
            for defin in defin_list:
                subcontent=subcontent+defin+' '
            subcontent=subcontent+'\n'        
        content=content+word+' '+subcontent.strip()+' |'


    t.insert(END,content)         


def QEC():
    
    words=ent.get()
    word_list=words.split(' ')      
        
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    
    for word in word_list:
                       
        url='https://tw.dictionary.search.yahoo.com/search?p='+ word
        req=urllib.request.Request(url,headers=headers)
        html=urllib.request.urlopen(req)
        doc=html.read()
        read=doc.decode('utf-8','ignore')
        soup=BeautifulSoup (doc,'html.parser')  
                
        
        

        defin_list=[]

        #main explanation!!
        try:
            tag2=soup.find_all(attrs={"class":"dictionaryExplanation"})
            for tag in tag2:
                line2=tag.get_text()
                defin_list.append('*'+line2)
                    
        except:
            continue

        #main explanation!!
            
        try:
            tag3=soup.find_all(attrs={"class":"fz-14"})
            
            for tag in tag3:
                line3=tag.get_text()
                if re.search('^[0-9]',line3) and len(line3) >=3:
                #if '[' not in line3:
                    defin_list.append(line3)
                else:
                    continue                
        except:
            continue

        t.insert(END,'\n'+word+' ')
        
        for defin in defin_list:
            t.insert(END, defin+' ')
            

def DET():
    t.delete('1.0',END)

def DEE():
    ent.delete('0',END)
            

    
win=tk.Tk()
win.title('Ronel V Work Ark')
win.geometry('1500x500')
win.resizable(width='1500', height='1000')



iconImage=tk.PhotoImage(master=win, data=icon)
tk.Label(image=iconImage).pack(side=LEFT)



label2=tk.Label(win, text='\nCopyright © 2018 Ronel V. All rights reserved. ', wraplength='1000',justify='left',)
label2.pack(side=BOTTOM)



#label=tk.Label(win, text='\n',wraplength='1000',justify='center',)
#label.pack()
label4=tk.Label(win, text="",wraplength='1000',justify='left')
label4.pack(side=TOP)
#ent=tk.Entry(win,width=100)
#ent.pack(side=TOP)
#label0=tk.Label(win, text="\nChoose a mode. If chosen wrongly, it won't run.\n",wraplength='1000',justify='left')
#label0.pack()
frame1=tk.Frame(win,width=20)
frame2=tk.Frame(win,width=40)
frame2.pack(anchor=N)
frame1.pack(anchor=N)

ent=tk.Entry(frame2,width=115)
ent.pack(side=LEFT)

label1=tk.Label(frame1,text='Oxford Dictionary  ')
label2=tk.Label(frame1,text='Dr.eye')
label3=tk.Label(frame1,text='Wikipedia')
label5=tk.Label(frame1,text='Quizlet')
button=tk.Button(frame1,text='Eng - Eng',command=EE)
button2=tk.Button(frame1,text='Eng - Ch',command=EC)
button3=tk.Button(frame1,text='Ch - Eng',command=CE)
button6=tk.Button(frame1,text='Eng - Eng',command=WK_EE)
button7=tk.Button(frame1,text='Eng - Ch',command=WK_EC)
button4=tk.Button(win,text='Delete',command=DET)
button5=tk.Button(frame2,text='Delete',command=DEE)
button8=tk.Button(frame1,text='Eng - Eng',command=QEE)
button9=tk.Button(frame1,text='Eng - Ch',command=QEC)
label1.pack(side=LEFT)
button5.pack(side=LEFT,padx=5)
button.pack(side=LEFT)
#label2.pack(side=LEFT,padx=10)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT,padx=0)
button4.pack(side=BOTTOM,fill=X)
#label3.pack(side=LEFT,padx=10)
#button6.pack(side=LEFT,padx=0)
#button7.pack(side=LEFT)
label5.pack(side=LEFT,padx=10)
button8.pack(side=LEFT)
#button9.pack(side=LEFT)


myFont =Font(family="Calibri Light", size=14)
t=Text(win, height=50, width=350)
s=Scrollbar(win)
s.pack(side=RIGHT, fill=Y)
t.pack(side=RIGHT)
s.config(command=t.yview)
t.config(yscrollcommand=s.set)
t.configure(font=myFont)

win.mainloop()
