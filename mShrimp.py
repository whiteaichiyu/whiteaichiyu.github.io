#v1待完成：1每次执行脚本时备份数据，shell脚本cp souce目录内容到source_bak 并压缩.2异常处理，参考selenium爬取动态网页作者文档。3根据停更天数来处理操作，停更10天内每次都执行同步，超过30天提示换作者

from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

option = ChromeOptions()
option.add_argument('--start-maximized')#浏览器最大化
option.add_experimental_option('excludeSwitches',['enable-automation'])#防止被识别
browser = webdriver.Chrome(options=option)

#载入网页
browser.get('https://www.jx3box.com/macro/10800')
#打开被同步文件
f = open('source\qixiu\index.md', 'w', encoding='utf-8')
#隐式等待200秒
browser.implicitly_wait(200)
#作者元素定位
author_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/div[@class='u-author u-sub-block']/a[@class='u-name']")
#更新时间元素定位
uptime_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/span[@class='u-modate u-sub-block']/time")
#版本元素定位
version_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/div[@class='u-meta u-sub-block'][2]/span[@class='u-value']")
#奇穴元素列表定位
acupoint_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-0']/div[@id='talent-box-0']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item']/span[@class='u-title']")
#加速元素定位
speed_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-0']/div[@class='u-speed']")
#宏名元素列表定位
macroname_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__header is-top']/div[@class='el-tabs__nav-wrap is-top']/div[@class='el-tabs__nav-scroll']/div[@class='el-tabs__nav is-top']/div")
#正文最长路径
body_xpath = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-post']/div[@class='m-single-content']/div[@class='c-article-box']/div[@id='c-article']/div[@id='c-article-part1']/p/span/span/img"
#body_eles2 = body_xpath+"[%d]" %(index)
#截取最长路径截取找到src分布位置
body_eles = browser.find_elements_by_xpath(body_xpath+" | "+body_xpath[0:211]+"/img")

print("原作者："+author_ele.text)
#停更天数计算---
today = time.time()
t = time.mktime(time.strptime(uptime_ele.text,"%Y-%m-%d"))
unupsec = today-t
unupday = int(unupsec/60/60/24)
print("作者已停更",unupday,"天")
#---

#主页头文件
f.write('---\ntitle: 七秀\n')
f.write('date: ')
formtoday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f.write(formtoday)
f.write('\n')
f.write('---\n')
#图片路径
f.write('{% img [fullimage] /images/qixiu-foot.jpg [title 七秀 [alt text]] %}\n')
f.write('## 心法：冰心诀 （新妆流）\n')
f.write('\n')
f.write('**版本：'+version_ele.text+uptime_ele.text+'**\n')
f.write('\n')
f.write('### 奇穴：')
for index in range(len(acupoint_eles)):
    print(acupoint_eles[index].text)
    f.write(acupoint_eles[index].text+' ')
f.write('\n')
f.write('### 秘籍：\n')
f.write('玳弦急曲—3伤害+1距离\n剑气长江—1回剑舞+1减CD，其他点伤害会心距离均可\n江海凝光—2伤害+1会心+1距离\n繁音急节—3减CD+1满堂会心\n天地低昂—2减CD+1持续时间，另一本随意\n心鼓弦——3减读条+1距离\n')
f.write('\n')
f.write('### 急速：'+speed_ele.text+'\n')
f.write('\n')
#开始导入宏,遍历所有宏
print("---开始导入宏--")
for index2 in range(len(macroname_eles)):
    #点击页面上每个宏的小页面切换
    browser.execute_script("arguments[0].click();", macroname_eles[index2])
    f.write('{% codeblock '+macroname_eles[index2].text+' %}\n')
    print(macroname_eles[index2].text)
    #宏语句元素列表定位
    macro_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box withUsage']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li")%(index2)
    for index in range(len(macro_eles)):
        print(macro_eles[index].text)
        f.write(macro_eles[index].text+'\n')
    f.write('{% endcodeblock %}\n')
f.write('\n')
#循环打法
f.write('### 循环打法：\n')
#遍历正文所有/p值，按顺序写入文字与图片src
for index in range(len(body_eles)):
    bodytext_eles = browser.find_elements_by_xpath(body_xpath[0:211])
    for index2 in range(len(bodytext_eles)):
        if len(bodytext_eles[index2].text) > 0:
            #print(bodytext_eles[index2].text)
            f.write(bodytext_eles[index2].text+'\n') 
    #print(body_eles[index].get_attribute("src"))
    f.write('![avatar]('+body_eles[index].get_attribute("src")+')\n')

browser.quit()