# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
import sys
import pandas as pd

def getData(url):
    
    driver =webdriver.Chrome()
    driver.set_page_load_timeout(30)
    time.sleep(3)
    browser=driver.get(url)#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
    html=driver.page_source#获取网页的html数据
    soup=BeautifulSoup(html,'lxml')#对html进行解析
    table_select=soup.find('div',id = 'lawSuits')
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
        flag=1
    return df
url = 'https://www.qixin.com/risk/55c7d464-63e0-4585-bd52-eb0c7fa23f0f'
print(getData(url))

