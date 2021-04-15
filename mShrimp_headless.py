from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument("--headless")#指定无头模式
option.add_argument('--start-maximized')#浏览器最大化
option.add_experimental_option('excludeSwitches',['enable-automation'])#防止被识别
browser = webdriver.Chrome(options=option)

browser.get('https://www.jx3box.com/macro/100')
browser.implicitly_wait(10)

#元素是否存在判定
def NodeExists(xpath):
   try:
      browser.find_element_by_xpath(xpath)
      return True
   except:
      return False


macroname_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__header is-top']/div[@class='el-tabs__nav-wrap is-top']/div[@class='el-tabs__nav-scroll']/div[@class='el-tabs__nav is-top']/div")
stracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item']/span[@class='u-title']" % (0,0)
acupoint_eles = browser.find_elements_by_xpath(stracupoint)
acupoint_eless = [[0 for i in range(len(acupoint_eles))] for j in range(len(macroname_eles))]
#开始导入宏,遍历所有宏
print("---开始导入宏与奇穴--")
for index2 in range(len(macroname_eles)):
    #点击页面上每个宏的小页面切换
    browser.execute_script("arguments[0].click();", macroname_eles[index2])
    #奇穴相关代码块
    #奇穴元素列表acupoint_eles的xpath默认地址
    stracupoint = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@id='talent-box-%d']/div[@class='w-qixue-box false']/ul[@class='w-qixue-clist']/li[@class='w-qixue-clist-item']/span[@class='u-title']" % (index2,index2)
    acupoint_eles = browser.find_elements_by_xpath(stracupoint)

    for acu_index in range(len(acupoint_eles)):
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
                    #f.write('### 奇穴：参考宏%d' % (acu_index2+1))
                    newacu = 3
                    break
            elif index2 > 0 and acupoint_eless[acu_index2][acu_index] != acupoint_eles[acu_index].text and acupoint_eles[acu_index].text != 0:
                print("该层奇穴与宏%d奇穴%d不一致,此奇穴将新写一份" %(acu_index2+1,acu_index+1))
                newacu = 1
                
    if newacu == 1 or index2 == 0:
        print("此为存在不一致或是第一份奇穴，将新写一份")
        #f.write('### 奇穴：')
        for acu_index in range(len(acupoint_eles)):
            print(acupoint_eles[acu_index].text)
            #f.write(acupoint_eles[index].text+' ')
    #f.write('\n')

    #宏相关代码块
    #f.write('{% codeblock '+macroname_eles[index2].text+' %}\n')
    print(macroname_eles[index2].text)
    #用于自变量strmacro中的参数，找不到则去掉这条
    ifusage = ' withUsage'
    #宏语句列表macro_eles的xpath默认地址
    strmacro = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box%s']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li" % (index2,ifusage)

    #判定宏所在页是否需要加' withUsage'字段，默认加
    if NodeExists(strmacro):
        print("存在此元素，无需修改")
    else:
        print("不存在，去掉withUsage")
        strmacro = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li" % (index2)

    macro_eles = browser.find_elements_by_xpath(strmacro)
    for index in range(len(macro_eles)):
        print(macro_eles[index].text)
        #f.write(macro_eles[index].text+'\n')
    #f.write('{% endcodeblock %}\n')
browser.quit()
