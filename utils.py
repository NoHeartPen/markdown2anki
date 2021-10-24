import os
from re import I
def replace_formula(formula):
    formula_str = formula.group() 
    formula_str = formula_str.replace('{{', '{ {') 
    formula_str = formula_str.replace('}}', '} }')
    formula_str = '\(' + formula_str + '\)'
    return formula_str

def replace_cloze(cloze):
    cloze_str = cloze.group()
    cloze_str = cloze_str.replace('**', '') 
    cloze_str = '{{c1::<u>' + cloze_str + '</u>}}'  
    return cloze_str

def replace_cloze_SimpRead(cloze_SimpRead):
    cloze_SimpRead_str = cloze_SimpRead.group()
    cloze_SimpRead_str = cloze_SimpRead_str.replace('~~','')
    cloze_SimpRead_str = '{{c1::<u>' + cloze_SimpRead_str + '</u>}}'
    return cloze_SimpRead_str

def replace_picture(picture):
    picture_str = picture.group()
    picture_str = picture_str.replace('![](','')
    picture_str = picture_str.replace(')','')
    picture_str = '<img src=' + picture_str + '>'
    return picture_str

def replace_hiragana(hiragana):
    Hiragana_str = hiragana.group()
    Hiragana_str = Hiragana_str.replace('[',"")
    Hiragana_str = Hiragana_str.replace(']','')
    Hiragana_str = '[{{c1::'+ Hiragana_str + '}}]'
    return Hiragana_str

def replace_code(code):
    code_str = code.group()
    code_str = code_str.replace('`','')
    code_str = '<code>' + code_str + '<\code>'
    return code_str

def replace_Bold(Bold):
    Bold_str = Bold.group()
    Bold_str = "<b>"+Bold_str.replace('**', '')+"</b>" 
    return Bold_str
