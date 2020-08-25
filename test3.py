import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from lxml import html
import time
from selenium import webdriver
import sys
# tb = pd.read_html('https://www.qixin.com/company/06a8671f-693d-4ec4-b317-96ff0ce6a3ad?section=changeInfo')[5]
# print(tb)
def login(username,password):
    """
    登录程序，输入用户密码，手工完成认证。
    return:
    """
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get('https://www.qixin.com/auth/login?return_url=%2Fcompany%2F5db4a5ed-776b-46a5-a129-648a6f47de34%3Fsection%3DchangeInfo')
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/input").send_keys(password)
    print ("请在2s内手工完成认证，认证后请勿点击登录按钮。")
    # driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[1]").click()
    # driver.find_element_by_css_selector('body > div.web-diversion-container.event-maizeng > div.fixed-bottom > div > div.closing.pull-right').click
    time.sleep(2)
    driver.find_element_by_css_selector('body > div.web-diversion-container.event-maizeng > div.fixed-bottom > div > div.closing.pull-right').click

    # driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]').click
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[4]/div").click()
    return driver
# /html/body/div[5]/div[1]/div/div[1]
# /html/body/div[5]/div[1]/div/div[1]
driver = webdriver.Chrome()
driver.maximize_window()
# driver.set_window_size(1920, 1080)
# driver =login(username = '15180533493', password = 'jxgayzk0308')
driver.set_page_load_timeout(30)
time.sleep(3)
browser=driver.get('https://www.qixin.com/company/4c8bd41b-2534-43c0-8643-5bf4dca1991e?section=changeInfo')#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
# for page in range(3):

html_source=driver.page_source#获取网页的html数据
tree = html.fromstring(html_source)

len_page = len(tree.xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li'))
# driver.find_element_by_xpath('//div[contains(@class, "container clearfix")]//*[contains(@class,"closing pull-right")]').click
# driver.find_element_by_css_selector('body > div.web-diversion-container.event-maizeng > div.fixed-bottom > div > div.closing.pull-right').click
# print(len_page)
a = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]')
a.click()
time.sleep(0.5)
i = 2
pre = 0
while i<=len_page-1:
# for i in range(2,len_page):
    b = driver.find_element_by_xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li[{}]/a'.format(i))
    cur = b.text 
    # driver.find_element_by_css_selector("div#page> :last-child").click()
    # cur_a = tree.xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li[{}]/a/text()'.format(i))
    # print(cur_a)
    if int(cur) != int(pre) + 1:
        should_click = driver.find_element_by_xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li[5]/a')
        cur = should_click.text
        should_click.click()
        pre = cur
    else:
        b.click()
        pre = cur
    # if cur_a == ['5'] and :
        i += 1
    time.sleep(0.5)
