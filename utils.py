import os
from re import I
def replace_formula(formula):
    formula_str = formula.group() # str.group()
    formula_str = formula_str.replace('$', '') 
    formula_str = formula_str.replace('{{', '{ {') 
    formula_str = formula_str.replace('}}', '} }')
    formula_str = '\(' + formula_str + '\)'
    return formula_str

def replace_cloze(cloze):
    cloze_str = cloze.group()
    cloze_str = cloze_str.replace('**', '') 
    cloze_str = '{{c1::' + cloze_str + '}}' 
    return cloze_str

def replace_picture(picture): #将markdown的图片语法转换为Anki支持的html
    picture_str = picture.group()
    picture_str = picture_str.replace('![](','')
    picture_str = picture_str.replace(')','')
    picture_str = '<img src=' + picture_str + '>'
    return picture_str

def replace_code(code): #将md格式的代码语法转换为Anki支持的html语法
    code_str = code.group()
    code_str = code_str.replace('`','')
    code_str = '<code>' + code_str + '<\code>'
    return code_str

def replace_Bold(Bold):
    Bold_str = Bold.group()
    Bold_str = "<b>"+Bold_str.replace('**', '')+"</b>"
    return Bold_str
