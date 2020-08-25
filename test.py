# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
import sys
import pandas as pd
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# curpath=sys.path[0]
# print curpath

def getData(url):
    
    driver =webdriver.Chrome()
    driver.set_page_load_timeout(30)
    time.sleep(3)
    browser=driver.get(url)#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
    # for page in range(3):
    
    html=driver.page_source#获取网页的html数据
    tree = html.fromstring(html)
    len_page = len(tree.xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li'))
    soup=BeautifulSoup(html,'lxml')#对html进行解析
    table_select=soup.find('div',id = 'changeInfo')
    table = table_select.find('table',class_ = 'table table-bordered margin-t-1x')
    name=[]
    for th in table.find_all('tr')[0].find_all('th'):
        name.append(th.get_text())#获取表格的字段名称作为字典的键
    flag = 0 #标记，当爬取字段数据是为0，否则为1
    df_flag = 0 #标记是否创建dataframe
    for tr in table.find_all('tr'):
    #第一行为表格字段数据，因此跳过第一行
        if flag==1:
            dic={}
            i=0
            for td in tr.find_all('td'):
                dic[name[i]]=td.get_text().replace('\n','').replace('\r','')
                i+=1
            if df_flag == 0:
                df = pd.DataFrame.from_dict(dic,orient='index').T
                df_flag = 1
            else:
                df = df.append([dic], ignore_index=True)    
            # jsonDump(dic,url[1])#保存数据
        flag=1
        # driver.find_element_by_link_text(u"下一页").click()#利用find_element_by_link_text方法得到下一页所在的位置并点击，点击后页面会自动更新，只需要重新获取driver.page_source即可。
    return df
url = 'https://www.qixin.com/company/06a8671f-693d-4ec4-b317-96ff0ce6a3ad?section=changeInfo'
print(getData(url))

