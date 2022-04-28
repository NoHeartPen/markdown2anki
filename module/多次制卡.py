# 该模块用于实现多次挖空
import re
import os
from pathlib import Path

def replace_cloze(cloze):
    cloze_str = cloze.group()
    cloze_str = cloze_str.replace('**', '') 
    cloze_str = '{{c1::<u>' + cloze_str + '</u>}}'  
    return cloze_str

# 将markdown语法替换为Anki挖空语法
path = os.getcwd()
p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '**' in line:
                Cloze = line
                Cloze = re.sub(r'\*\*(.*?)\*\*', replace_cloze, Cloze)
                card = Cloze+"\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open(filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)

# 调整挖空次数
path = os.getcwd()
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
                    colze=re.sub(r'c\d{1}:',str(number),colze,1)
                    number = int (number)
                card = colze+"\n"
                cards.append(card) 
            else:
                continue
    filename=os.path.basename(file)
    with open(filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)