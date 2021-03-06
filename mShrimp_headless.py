#v1待完成：1每次执行脚本时备份数据，shell脚本cp souce目录内容到source_bak 并压缩.2异常处理，参考selenium爬取动态网页作者文档。3根据停更天数来处理操作，停更10天内每次都执行同步，超过30天提示换作者

from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
import os

option = ChromeOptions()
option.add_argument("--no-sandbox")#无沙箱模式
option.add_argument("--headless")#指定无头模式
option.add_argument('--start-maximized')#浏览器最大化
option.add_experimental_option('excludeSwitches',['enable-automation'])#防止被识别
browser = webdriver.Chrome(options=option)

#元素是否存在判定
def NodeExists(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        return True
    except:
        return False

def upMacro(menpai,menpai2,fmode):
    #载入网页
    browser.get('https://www.jx3box.com/macro/'+menpai.pageID)
    #隐式等待10秒
    browser.implicitly_wait(10)

    #作者元素定位
    author_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/div[@class='u-author u-sub-block']/a[@class='u-name']")
    #更新时间元素定位
    uptime_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/span[@class='u-modate u-sub-block']/time")
    #版本元素定位
    version_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/header[@class='m-single-header']/div[@class='m-single-info']/div[@class='u-meta u-sub-block'][2]/span[@class='u-value']")
    #宏名元素列表定位
    macroname_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__header is-top']/div[@class='el-tabs__nav-wrap is-top']/div[@class='el-tabs__nav-scroll']/div[@class='el-tabs__nav is-top']/div")
    #奇穴元素xpath值
    stracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item']/span[@class='u-title']" % (0,0)
    canusestracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item w-qixue-is_skill']/span[@class='u-title']" % (0,0)
    #奇穴元素列表定位
    acupoint_eles = browser.find_elements_by_xpath(stracupoint+"|"+canusestracupoint)
    #加速元素定位
    speed_ele = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-0']/div[@class='u-speed']")
    #正文最长路径
    body_xpath = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-post']/div[@class='m-single-content']/div[@class='c-article-box']/div[@id='c-article']/div[@id='c-article-part1']/p/span/span/img"
    #body_eles2 = body_xpath+"[%d]" %(index)
    #截取最长路径截取找到src分布位置
    body_eles = browser.find_elements_by_xpath(body_xpath+" | "+body_xpath[0:211]+"/img"+" | "+body_xpath[0:211]+"/span/img")
    #奇穴元素二维数组
    acupoint_eless = [[0 for i in range(len(acupoint_eles))] for j in range(len(macroname_eles))]
    print("原作者："+author_ele.text)
    #停更天数计算---
    today = time.time()
    t = time.mktime(time.strptime(uptime_ele.text,"%Y-%m-%d"))
    unupsec = today-t
    unupday = int(unupsec/60/60/24)
    
    if unupday<20:
        print("作者已停更",unupday,"天")
        os.system('if [ $(ll source_bak/ | grep -c '+menpai.dirn+') -eq 1 ]; then cp source/'+menpai.dirn+'/index.md source_bak/'+menpai.dirn+'/index'+time.strftime("%Y-%m-%d", time.localtime()) +'.md; else mkdir source_bak/'+menpai.dirn+'; fi')
        os.system('cp source/'+menpai.dirn+'/index.md source_bak/'+menpai.dirn+'/index'+time.strftime("%Y-%m-%d", time.localtime()) +'.md')
        #os.system('cp source\\'+menpai.dirn+'\index.md source_bak\\'+menpai.dirn+'\index'+time.strftime("%Y-%m-%d", time.localtime()) +'.md')
    elif unupday>30:
        print('该作者已停更',unupday,'天，建议换作者')
    else:
        print("作者已停更",unupday,"天")
    
    #---
    #打开被同步文件
    f = open('source\\'+menpai.dirn+'\index.md', fmode, encoding='utf-8')
    #f = open('./source/qixiu/index.md', 'w', encoding='utf-8')
    if fmode == 'w' :
        #主页头文件
        f.write('---\ntitle: '+menpai.menpainame+'\n')
        f.write('date: ')
        formtoday = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        f.write(formtoday)
        f.write('\n')
        f.write('---\n')
        #图片路径
        f.write('{% img [fullimage] /images/'+menpai.dirn+'-foot.jpg [title '+menpai.menpainame+' [alt text]] %}\n')
    f.write('## 心法：'+menpai.xinfa+'\n')
    f.write('\n')
    f.write('**版本：'+version_ele.text+uptime_ele.text+'**\n')
    f.write('\n')
    f.write('### 秘籍：\n')
    f.write(menpai.miji)
    f.write('\n')
    f.write('### 急速：'+speed_ele.text+'\n')
    f.write('\n')
    #开始导入宏与奇穴,遍历所有宏与奇穴
    print("---开始导入宏与奇穴--")
    for index2 in range(len(macroname_eles)):
        #点击页面上每个宏的小页面切换
        browser.execute_script("arguments[0].click();", macroname_eles[index2])
        #奇穴相关代码块
        #奇穴元素列表acupoint_eles的xpath默认地址
        stracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item']/span[@class='u-title']" % (index2,index2)
        canusestracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item w-qixue-is_skill']/span[@class='u-title']" % (index2,index2)
        acupoint_eles = browser.find_elements_by_xpath(stracupoint+"|"+canusestracupoint)

        print('len=',len(acupoint_eles),'acu=',acupoint_eles)
        for acu_index in range(len(acupoint_eles)):
            print('its acu no',acu_index)
            print('222'+acupoint_eles[acu_index].text)
            print('奇穴2维数组：',acupoint_eless)
            print('111',acupoint_eless[index2][acu_index])
            acupoint_eless[index2][acu_index] = acupoint_eles[acu_index].text
        print(acupoint_eless)
        newacu = 0
        for acu_index2 in range(index2):
            acucount = 0
            if newacu == 3:
                break
            for acu_index in range(len(acupoint_eles)):
                if index2 > 0 and acupoint_eless[acu_index2][acu_index] == acupoint_eles[acu_index].text:
                    print("该层奇穴与宏%d奇穴%d%s一致" %(acu_index2+1,acu_index+1,acupoint_eles[acu_index].text))
                    print(acucount)
                    acucount = acucount + 1
                    if acucount == 12:
                        print(acucount)
                        print("此奇穴完全一致，略过")
                        f.write('### 奇穴：参考宏%d' % (acu_index2+1))
                        newacu = 3
                        break
                elif index2 > 0 and acupoint_eless[acu_index2][acu_index] != acupoint_eles[acu_index].text and acupoint_eles[acu_index].text != 0:
                    print("该层奇穴与宏%d奇穴%d不一致,此奇穴将新写一份" %(acu_index2+1,acu_index+1))
                    newacu = 1
                # elif index2 > 0 :
                #     print('空值略过')
                #     newacu = 3
                #     break
                    
        if newacu == 1 or index2 == 0:
            print("此为存在不一致或是第一份奇穴，将新写一份")
            f.write('### 奇穴：')
            for acu_index in range(len(acupoint_eles)):
                print(acupoint_eles[acu_index].text)
                f.write(acupoint_eles[acu_index].text+' ')
        f.write('\n')

        #宏相关代码块
        f.write('{% codeblock '+macroname_eles[index2].text+' %}\n')
        print(macroname_eles[index2].text)
        #用于自变量strmacro中的参数，找不到则去掉这条
        ifusage = ' withUsage'
        #宏语句列表macro_eles的xpath默认地址
        strmacro = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box%s']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li" % (index2,ifusage)

        #判定宏所在页是否需要加' withUsage'字段，默认加
        if NodeExists(strmacro):
            print("存在元素withUsage，无需修改")
        else:
            print("不存在，去掉withUsage")
            strmacro = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li" % (index2)

        macro_eles = browser.find_elements_by_xpath(strmacro)
        for index in range(len(macro_eles)):
            print(macro_eles[index].text)
            f.write(macro_eles[index].text+'\n')
        f.write('{% endcodeblock %}\n')
    f.write('\n')
    #循环打法
    f.write('### 循环打法：\n')
    #遍历正文所有/p值，按顺序写入文字与图片src

    # for bodyindex in range(len(body_eles)):
    #     bodytext_eles = browser.find_elements_by_xpath(body_xpath[0:211])
    #     for bodyindex2 in range(len(bodytext_eles)):
    #         if len(bodytext_eles[bodyindex2].text) > 0:
    #             print(bodytext_eles[index2].text)
    #             f.write(bodytext_eles[bodyindex2].text+'\n') 
    #     print(body_eles[index].get_attribute("src"))
    #     f.write('![avatar]('+body_eles[bodyindex].get_attribute("src")+')\n')
    bodyindex = 0
    bodytext_eles = browser.find_elements_by_xpath(body_xpath[0:211])
    for bodyindex2 in range(len(bodytext_eles)):
        if len(bodytext_eles[bodyindex2].text) > 0:
            #print(bodytext_eles[index2].text)
            f.write(bodytext_eles[bodyindex2].text+'\n')
        elif bodyindex < len(body_eles):
            f.write('![avatar]('+body_eles[bodyindex].get_attribute("src")+')\n')
            bodyindex = bodyindex+1
    #test
    if fmode == 'a':
        browser.close()
        browser.quit()
    else:
        f.write('\n---\n')
    f.close()
    #迭代调用，用于追加心法2，无心法2则参数天None
    if menpai2 != None :
        upMacro(menpai2,None,'a')
    elif fmode == 'w':
        browser.close()
        browser.quit()
class menpaixinfa:
    def __init__(self,pageID,dirn,menpainame,xinfa,miji):
        self.dirn = dirn
        self.pageID = pageID
        self.menpainame = menpainame
        self.xinfa = xinfa
        self.miji = miji

bingxin = menpaixinfa('10800','qixiu','七秀','冰心诀','玳弦急曲—3伤害+1距离\n剑气长江—1回剑舞+1减CD，其他点伤害会心距离均可\n江海凝光—2伤害+1会心+1距离\n繁音急节—3减CD+1满堂会心\n天地低昂—2减CD+1持续时间，另一本随意\n心鼓弦——3减读条+1距离\n')
yunshang = menpaixinfa('22084','qixiu','七秀','云裳心经','秘籍：回雪飘摇：3疗效1距离\n翔鸾舞柳：2疗效2距离\n上元点鬟：1疗效3距离\n王母挥袂：2疗效2会心\n繁音急节：3减cd1满堂\n心鼓弦：3减cd1距离（配合璇妗奇穴可达到5分钟战复）\n天地低昂：2减cd1持续时间1回蓝\n江海凝光：3距离1伤害\n')
upMacro(bingxin,yunshang,'w')#参数：门派心法1（必填）,门派心法2（可选,没有就填None）,写入文件模式,(默认'w',函数嵌套时会用到'a'从尾部追加，平时调用时一定用默认'w')

mowen = menpaixinfa('20123','changge','长歌','莫问（大微流）','宫——2读条1伤害1会心\n商——2会心2伤害\n徵——3会心1伤害\n羽——2会心2伤害\n杯水——3读条1效果\n青霄——3效果1减CD\n')
browser = webdriver.Chrome(options=option)
upMacro(mowen,None,'w')