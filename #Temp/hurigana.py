
import re
import utils
import os
from pathlib import Path
import pyperclip
import shutil

# 调整文件语法 将markdown语法替换为Html语法
path = os.getcwd()
p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '[' in line:
                hurigana = line
                hurigana = re.sub(r'\w\[\{\{', utils.space_hurigana, hurigana)
                card = hurigana+"\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open(filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)