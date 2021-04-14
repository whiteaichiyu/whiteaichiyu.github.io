from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
#option.add_argument("--headless")#指定无头模式
option.add_argument('--start-maximized')#浏览器最大化
option.add_experimental_option('excludeSwitches',['enable-automation'])#防止被识别
browser = webdriver.Chrome(options=option)

browser.get('https://www.jx3box.com/macro/10800')
browser.implicitly_wait(200)

macroname_eles = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__header is-top']/div[@class='el-tabs__nav-wrap is-top']/div[@class='el-tabs__nav-scroll']/div[@class='el-tabs__nav is-top']/div")


#开始导入宏,遍历所有宏
print("---开始导入宏--")
for index2 in range(len(macroname_eles)):
    #点击页面上每个宏的小页面切换
    browser.execute_script("arguments[0].click();", macroname_eles[index2])
   # f.write('{% codeblock '+macroname_eles[index2].text+' %}\n')
    print(macroname_eles[index2].text)
    #宏语句元素列表定位
    strmacro = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-%d']/div[@class='u-macro macro-box withUsage']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li" % (index2)
    print(strmacro)
    macro_eles = browser.find_elements_by_xpath(strmacro)
    
    for index in range(len(macro_eles)):
        print(macro_eles[index].text)
        #f.write(macro_eles[index].text+'\n')
    #f.write('{% endcodeblock %}\n')
    strmacro = " "  
browser.quit()
