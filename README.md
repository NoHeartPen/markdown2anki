# markdown2anki_项目说明

将md笔记转换成可以导入Anki的格式

## 项目版本

## v0.0.4 2021年10月28日

优化:
1. 修改判断Markdown图片语法的条件,现在插入图片时可以添加说明文字了;
2. 调整判断条件的顺序,在包含']('时会将之识别为Markdown超链接语法,而不是Anki注音的语法;
新增:
1. 支持将Markdown的超链接语法转为HTML的超链接语法

### v0.0.3 2021年10月24日

新增:
1. 支持快速处理[简悦](https://simpread.pro/)导出的Markdown标注(只是去掉了导出文件的开头说明性文字)
2. 新增~~~~即Markdown删除线语法制卡的支持
3. 修改了挖空部分的细节,凡是挖空的地方都会添加<code><u>下划线</u></code>,便于一张多次挖过空的卡牌上快速找到重点(虽然现在还并不能自动挖空🤣)

### v0.0.2 2021年10月6日

新增:处理完所有文件后会直接打开Anki程序,但需要自己手动修改note2cloze.py中的'os.system("D:\\03Program\\Anki\\anki.exe")',替换为自己的Anki安装路径,注意:该路径不能包含空格,否者会报错;另外注意使用'\\'表示'\'

### v0.0.1 2021年10月5日

参考修改说明部分

# 使用方法

模仿笔记样例格式写自己的笔记，将md文件和图片文件放同一文件夹下，运行脚本即可得到可导入Anki的txt文件。

建议结合个人习惯适当修改后使用

# 修改说明

1. 新增对Markdown部分语法转html语法的支持.
 - 支持将Markdown的双引号''语法转换为html'<code></code>'
 - 支持将Markdown的[]()转换为<img src= >
2. 在原来的基础上,新增了利用[Markdown-img](https://github.com/icexmoon/markdown-img)项目将图片上传至图床,方便跨设备快速同步,如果你不熟悉该项目,可以参考作者介绍该项目的文章[VSCode内Markdown图床上传](https://www.yuque.com/noheartpen/gur8p4/rkop5l)。
3. 新增对同时转换多份笔记的支持
4. 新增对多字段导入的支持: 中间有一行空行时(即书写完一条笔记后，要按2次回车键)才会被认为是2条笔记。另外，默认最多支持字段数是4，请结合自己的习惯修改
5. 修改后的版本更适合日常在电脑端(VSCode)和利用md记笔记的习惯，然后利用AnkiDrod复习的Anki重度使用者
6. 提供了exe可执行文件(位于dist文件夹下)，可以与Windows任务计划程序相配合，定时执行

# 未来计划

1. 新增对Anki内显示注音的优化支持 会在有'[]'的汉字前添加一个半角空格,防止错位
   ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-10-02-07-38-57.png)
   ![](https://markdoen-1304943362.cos.ap-nanjing.myqcloud.com//2021-10-02-07-39-29.png)
2. 新增对一条字段多次挖空制卡的支持

# 鸣谢

感谢原作者[L-M-Sherlock](https://github.com/L-M-Sherlock)的[markdown2anki](https://github.com/L-M-Sherlock/markdown2anki)项目提供的源码支持ヾ(≧▽≦*)o
