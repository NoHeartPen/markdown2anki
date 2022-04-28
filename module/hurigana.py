# 该模块用于修正假名注音偏移的影响,在[{{语法前添加一个半角空格

import re
import os
from pathlib import Path

def space_hurigana(space):
    space_hurigana= space.group()
    space_hurigana = ' '+space_hurigana
    print(space_hurigana)
    return space_hurigana


path = os.getcwd()
p = Path(path) 
FileList=list(p.glob("**/*.txt"))
for file in FileList:
    with open(file, 'r',encoding='UTF-8') as note_file:
        cards = []
        lines = note_file.readlines() 
        for line in lines: 
            if '[' in line:
                hurigana = line
                hurigana = re.sub(r'\w\[\{\{', space_hurigana, hurigana)
                card = hurigana+"\n"
                cards.append(card)
            else:
                continue
    filename=os.path.basename(file)
    with open(filename, 'w', encoding='UTF-8') as txt_file:
        txt_file.writelines(cards)