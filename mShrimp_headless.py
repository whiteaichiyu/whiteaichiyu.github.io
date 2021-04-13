from selenium import webdriver
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
#option.add_argument("--headless")#指定无头模式
option.add_argument('--start-maximized')#浏览器最大化
option.add_experimental_option('excludeSwitches',['enable-automation'])#防止被识别
browser = webdriver.Chrome(options=option)

browser.get('https://www.jx3box.com/macro/10800')
browser.implicitly_wait(200)
body_xpath = "/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-post']/div[@class='m-single-content']/div[@class='c-article-box']/div[@id='c-article']/div[@id='c-article-part1']/p"
body_eles = browser.find_elements_by_xpath(body_xpath)
src_eles = browser.find_element_by_xpath("/html/body/div[@id='app']/main[@class='c-main']/div[@class='m-single-box']/div[@class='m-single-post']/div[@class='m-single-content']/div[@class='c-article-box']/div[@id='c-article']/div[@id='c-article-part1']/p/").get_attribute('src')
# for index in range(len(body_eles)):
    #src_eles = browser.find_elements_by_xpath(str(body_xpath+"//@src"))
    # if src_eles[index].text[0:5]=="https":
    #     print(src_eles[index].text)
     #print(body_eles[index].text)
print(src_eles.text)
browser.quit()
