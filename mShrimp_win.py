from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument("--headless")#指定无头模式
browser = webdriver.Chrome(options=option)

browser.get('https://www.jx3box.com/macro/10543')
browser.implicitly_wait(200)
#宏位置节点定位
macro_nodes = browser.find_elements_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-prepend']/div[@class='m-single-macro']/div[@class='el-tabs el-tabs--card el-tabs--top']/div[@class='el-tabs__content']/div[@id='pane-0']/div[@class='u-macro macro-box withUsage']/div[@class='u-macro-inner']/div[@class='w-jx3macro']/ol/li")

print("-----")
for index in range(len(macro_nodes)):
    print(macro_nodes[index].text)

browser.quit()
