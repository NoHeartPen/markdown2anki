import re
import utils
import os
from pathlib import Path
import pyperclip

#将笔记中的图片上传到图床
cmd = "python -m markdown_img "
os.system(cmd)
    
#将笔记转换为Anki支持的txt格式
path = os.getcwd() + '\markdown_img'+'\\'

p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.md"))
for file in FileList:
    with open(file, 'r', encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines:
            if '|20' in line:
                break
            elif '本文由 [简悦 SimpRead]'in line:
                continue
            elif line != "\n":
                line = line.replace('\n','\\')
                card = line
                cards.append(card)
            elif line == "\n":
                card = line
                cards.append(card)
            else:
                continue
    with open("{}.txt".format(file), 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)
# 调整文件语法 将markdown语法替换为Html语法
path = os.getcwd() + '\markdown_img'+'\\'
p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '![' in line:
                Picture = line
                Picture = re.sub(r'\!\[\]\((.*?)\)',utils.replace_picture,Picture)
                card =Picture+"\n"
                cards.append(card)
            elif '](' in line:
                Link = line
                Link = re.sub(r'\[(.*?)\)',utils.replace_link,Link)
                card = Link+"\n"
                cards.append(card)
            elif '`' in line:
                Code = line
                Code = re.sub(r'\`(.*?)\`',utils.replace_code,Code)
                card = Code+"\n"
                cards.append(card)
            else:
                continue
        for line in lines: 
            if '**' in line:
                Cloze = line
                Cloze = re.sub(r'\*\*(.*?)\*\*', utils.replace_cloze, Cloze)
                card = Cloze+"\n"
                cards.append(card) 
            elif '['in line:
                Hiragana = line
                Hiragana = re.sub(r'\[(.*?)\]',utils.replace_hiragana,Hiragana)
                card = Hiragana+"\n"
                cards.append(card)
            elif '~~' in line:
                Cloze_SimpRead = line
                Cloze_SimpRead = re.sub(r'~~(.*?)~~',utils.replace_cloze_SimpRead,Cloze_SimpRead)
                card = Cloze_SimpRead + "\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

#补齐Anki字段数

path = os.getcwd() + '\Anki'+'\\'
p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            number_backslash = line.count("\\")
            if number_backslash == 1 :
                line =line.replace("\n","")
                card = line+"\\ "+"\\ "+"\n"
                cards.append(card)
            elif number_backslash == 2:
                line = line.replace("\n","")
                card = line+"\\ "+"\n"
                cards.append(card)
            else:
                continue
        filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)
pyperclip.copy(path)
os.system("D:\\03Program\\Anki\\anki.exe")


