# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# curpath=sys.path[0]
# print curpath

def getData(url):
    driver =webdriver.Chrome()#使用下载好的phantomjs，网上也有人用firefox，chrome，但是我没有成功，用这个也挺方便
    driver.set_page_load_timeout(30)
    time.sleep(3)
    html=driver.get(url[0])#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
    for page in range(3):
        html=driver.page_source#获取网页的html数据
        soup=BeautifulSoup(html,'lxml')#对html进行解析，如果提示lxml未安装，直接pip install lxml即可
        table=soup.find('table',class_="report-table")
        name=[]
        for th in table.find_all('tr')[0].find_all('th'):
            name.append(th.get_text())#获取表格的字段名称作为字典的键
        flag=0#标记，当爬取字段数据是为0，否则为1
        for tr in table.find_all('tr'):
        #第一行为表格字段数据，因此跳过第一行
            if flag==1:
                dic={}
                i=0
                for td in tr.find_all('td'):
                    dic[name[i]]=td.get_text()  
                    i+=1        
                jsonDump(dic,url[1])#保存数据
            flag=1
        driver.find_element_by_link_text(u"下一页").click()#利用find_element_by_link_text方法得到下一页所在的位置并点击，点击后页面会自动更新，只需要重新获取driver.page_source即可。



if __name__ == '__main__':
    url=['http://datacenter.mep.gov.cn:8099/ths-report/report!list.action?xmlname=1465594312346','yzc'] #yzc为文件名，此处输入中文会报错，前面加u也不行，只好保存后手动改文件名……
    getData(url)#调用函数