# markdown2anki

 将md笔记转换成可以导入Anki的格式

# 使用方法

模仿笔记样例格式写自己的笔记，将md文件和图片文件放同一文件夹下，运行脚本即可得到可导入Anki的txt文件。

建议配合个人习惯适当修改后使用

# 修改说明

1. 新增对markdown部分语法转html语法的支持.
 - 支持将''''转换为'<code></code>'
 - 支持将'[]()'转换为'<img src= >'
2. 在原来的基础上,新增了利用[markdown-img](https://github.com/icexmoon/markdown-img)项目将图片上传至图床,方便跨设备快速同步,如果你不熟悉该项目,可以参考作者介绍该项目文章[VSCode内Markdown图床上传](https://www.yuque.com/noheartpen/gur8p4/rkop5l)。
3. 新增对同时转换多份笔记的支持
4. 新增对多字段导入的支持: 只有中间有存空行才会被认为是2条笔记

>GPA[しっ]妬[と]心[しん]を掻き立てる 因GPA激起了嫉妒心(这一行是日语例句和复习时帮助回忆的提示)
>
>刺激を与えて、感情や行動を起こすように促す。(这一行是辅助回忆的日语原文释义)
>
>注意，是我被绩点挑动了我自己的嫉妒心 (这一行是印在背面的提醒)
>
>PS:这只是一个加深印象的例句😜
>               (请注意,这里是一行空行)

>[し]妬[と]心[しん]を掻き立てる 因GPA激起了嫉妒心\刺激を与えて、感情や行動を起こすように促す。\注意，是我被绩点挑动了我自己的嫉妒心 \PS:这只是一个加深印象的例句😜

实际导入效果

5. 新增对没有加粗行导入Anki的支持,如上所示,并没有存在'****'的加粗语法,但依旧可以导入Anki
6. 修改后的版本更适合日常在电脑端(VSCode)和利用md记笔记的习惯，然后利用AnkiDrod复习的Anki重度使用者

# 未来计划
1. 新增对Anki内显示注音的优化支持 会在有'[]'的汉字前添加一个半角空格,防止错位
2. 新增对一条字段多次挖空制卡的支持

# 鸣谢

感谢原作者提供的源码支持ヾ(≧▽≦*)o
