import re
import utils
import os
from pathlib import Path
import pyperclip
import shutil
import pyautogui

#将笔记中的图片上传到图床
cmd = "python -m markdown_img "
os.system(cmd)
path = os.getcwd() + '\markdown_img'+'\\'
p = Path(path)
FileList=list(p.glob("**/*.md"))
for file in FileList:
    oldname = os.path.abspath(file)
    newname = os.path.abspath(file).replace("_image","")
    newname = os.path.abspath(newname).replace("\markdown_img","")
    shutil.move(oldname,newname)

#将笔记转换为Anki支持的txt格式
path = os.getcwd()
p = Path(path)
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
path = os.getcwd()
p = Path(path) 
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
            elif '['in line:
                Hiragana = line
                Hiragana = re.sub(r'\[(.*?)\]',utils.replace_hiragana,Hiragana)
                card = Hiragana+"\n"
                cards.append(card)
            elif '**' in line:
                Cloze = line
                Cloze = re.sub(r'\*\*(.*?)\*\*', utils.replace_cloze, Cloze)
                card = Cloze+"\n"
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

# 处理一行中同时出现[]、**2种制卡语法的行
path = os.getcwd() + '\Anki'+'\\'
p = Path(path)
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8')as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '**' in line:
                Cloze = line
                Cloze = re.sub(r'\*\*(.*?)\*\*', utils.replace_cloze, Cloze)
                card = Cloze+"\n"
                cards.append(card) 
            elif '~~' in line:
                Cloze_SimpRead = line
                Cloze_SimpRead = re.sub(r'~~(.*?)~~',utils.replace_cloze_SimpRead,Cloze_SimpRead)
                card = Cloze_SimpRead + "\n"
                cards.append(card)
            elif "{{c1::" in line:#请注意,不要随意删掉这一条件分支,否则只含一种制卡语法的行会直接被丢弃!
                card = line + "\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

# 处理一行中同时出现[]、**、
# 三种制卡语法的行，一般是很久以后复习时又有了新的发现，写笔记很少会分的这么细
path = os.getcwd() + '\Anki'+'\\'
p = Path(path) 
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8')as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '~~' in line:
                Cloze_SimpRead = line
                Cloze_SimpRead = re.sub(r'~~(.*?)~~',utils.replace_cloze_SimpRead,Cloze_SimpRead)
                card = Cloze_SimpRead + "\n"
                cards.append(card)
            elif "{{c1::" in line:#请注意,不要随意删掉这一条件分支,否则只含一种制卡语法的行会直接被丢弃!
                card = line + "\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

# 调整挖空次数
path = os.getcwd() + '\Anki'+'\\'
p = Path(path)
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if "{{c1::"in line:
                colze = line
                colze_number = colze.count("{{c1::")
                number = 1
                while number < colze_number:
                    number = number+1
                    colze=re.sub(r'\d{1}',str(number),colze,1)
                    number = int (number)
                card = colze+"\n"
                cards.append(card)

            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

#补齐Anki字段数,由于自己习惯习惯了4条字段,所以用于分割字段的反斜杠上限就是3个
path = os.getcwd() + '\Anki'+'\\'
p = Path(path)
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            number_backslash = line.count("\\")
            if number_backslash == 1 :
                line = line.replace("\n","")
                card = line+"\\ "+"\\ "+"\n"
                cards.append(card)
            elif number_backslash == 2:
                line = line.replace("\n","")
                card = line+"\\ "+"\n"
                cards.append(card)
            elif number_backslash == 3:
                card = line
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    os.unlink('./Anki/'+filename)
    with open('./Anki/'+filename.replace(".md",""), 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

# 解决 注音的部分被也被多次挖空
path = os.getcwd() + '\Anki'+'\\'
p = Path(path) 
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if "[{{c2"in line:
                colze = line
                colze=re.sub(r'\[\{\{c\d{1}',"[{{c1",colze)
                card = colze+"\n"
                cards.append(card)
            elif "{{" in line:
                card = line + "\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)


# 解决注音假名偏移问题
path = os.getcwd() + '\Anki'+'\\'
p = Path(path)
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '[{{' in line:
                hurigana = line
                hurigana = re.sub(r'\w\[\{\{', utils.space_hurigana, hurigana)
                card = hurigana+"\n"
                cards.append(card)
            elif "{{" in line:
                card = line + "\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

# 更改分割字段
path = os.getcwd() + '\Anki'+'\\'
p = Path(path) 
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '\\' in line:
                hurigana = line
                hurigana = re.sub(r'\\', r'\t', hurigana)
                card = hurigana+"\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open('./Anki/'+filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

pyperclip.copy(path)
os.system("D:\\03Program\\Anki\\anki.exe")
pyautogui.hotkey('y')






