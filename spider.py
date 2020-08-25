# -*- coding: utf-8 -*-

import xlwt
import bs4
import urllib.request,urllib.error
import re
from selenium import webdriver
from lxml import html
import time
from bs4 import BeautifulSoup
import pandas as pd

class tianyancha:

    def __init__(self,,username = None, password = None,url = None):
        '''
        初始化
        '''
        self.username = username
        self.password = password
        self.url = url

    def login(self):
        """
        登录程序，输入用户密码，手工完成认证。
        :return:
        """
        driver = webdriver.Chrome()
        driver.get('https://www.qixin.com/auth/login?return_url=%2Fcompany%2F5db4a5ed-776b-46a5-a129-648a6f47de34%3Fsection%3DchangeInfo')
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/input").send_keys(self.username)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/input").send_keys(self.password)
        print ("请在8s内手工完成认证，认证后请勿点击登录按钮。")
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[4]/div").click()
        return driver

    def get_url(self):
        return url

    def run(self):
        '''
            run the spider
        '''
        global driver
        driver = webdriver.Chrome()
        return driver

    def change_page(self,driver):
        """
        实现多列表页的翻页功能。
        :param driver:
        :return:
        """
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.set_page_load_timeout(30)
        time.sleep(3)
        browser=driver.get('https://www.qixin.com/company/4c8bd41b-2534-43c0-8643-5bf4dca1991e?section=changeInfo')#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
        html_source=driver.page_source#获取网页的html数据
        tree = html.fromstring(html_source)
        len_page = len(tree.xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li'))
        a = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]')
        a.click()
        time.sleep(0.5)
        i = 2
        pre = 0
        while i<=len_page-1:
            b = driver.find_element_by_xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li[{}]/a'.format(i))
            cur = b.text 
            if int(cur) != int(pre) + 1:
                should_click = driver.find_element_by_xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li[5]/a')
                cur = should_click.text
                should_click.click()
                pre = cur
            else:
                b.click()
                pre = cur
                i += 1
            time.sleep(0.5)

    def Business_change(self,driver):
        '''
        Author: Carl Yao
        parameters: 
        return: Pandas DataFrame of Business_change
        '''
        res = {}
        driver.set_page_load_timeout(30)
        time.sleep(3)
        Business_change_page = driver.get('https://www.qixin.com/company/5db4a5ed-776b-46a5-a129-648a6f47de34')#TODO#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
        # for page in range(3):
        html=driver.page_source#获取网页的html数据
        soup=BeautifulSoup(html,'lxml')#对html进行解析
        table_select=soup.find('div',id = 'changeInfo')
        table = table_select.find('table',class_ = 'table table-bordered margin-t-1x')
        name=[]
        try:
            for th in table.find_all('tr')[0].find_all('th'):
                name.append(th.get_text())#获取表格的字段名称作为字典的键
        except IndexError:
            Error = '----------------------------------------------------------------'+'\n'+\
                    '------------There is No Business Change Record Here-------------' +'\n'+\
                    '----------------------------------------------------------------'
            return Error
        else:
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
                        df_business_change = pd.DataFrame.from_dict(dic,orient='index').T
                        df_flag = 1
                    else:
                        df_business_change = df_business_change.append([dic], ignore_index=True)    
                    # jsonDump(dic,url[1])#保存数据
                flag=1
                # driver.find_element_by_link_text(u"下一页").click()#利用find_element_by_link_text方法得到下一页所在的位置并点击，点击后页面会自动更新，只需要重新获取driver.page_source即可。
            return df_business_change
    
    def law_risk(self,driver):
        '''
        Author : Carl Yao
        parameters:
        return: Pandas DataFrame of law risk
        '''
        driver.set_page_load_timeout(30)
        time.sleep(3)
        law_risk_page = driver.get('https://www.qixin.com/risk/5db4a5ed-776b-46a5-a129-648a6f47de34')   
        # for page in range(3):
        html=driver.page_source#获取网页的html数据
        soup=BeautifulSoup(html,'lxml')#对html进行解析
        table_select=soup.find('div',id = 'lawSuits')
        table = table_select.find('table',class_ = 'table table-bordered margin-t-1x')
        name=[]
        try:
            for th in table.find_all('tr')[0].find_all('th'):
                name.append(th.get_text())#获取表格的字段名称作为字典的键
        except IndexError:
            Error = '----------------------------------------------------------------'+'\n'+\
                    '-------------There is No Law Risk Record Here-------------------' +'\n'+\
                    '----------------------------------------------------------------'
            return Error
        else:
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
                        df_law_risk = pd.DataFrame.from_dict(dic,orient='index').T
                        df_flag = 1
                    else:
                        df_law_risk = df_law_risk.append([dic], ignore_index=True)    
                    # jsonDump(dic,url[1])#保存数据
                flag=1
                # driver.find_element_by_link_text(u"下一页").click()#利用find_element_by_link_text方法得到下一页所在的位置并点击，点击后页面会自动更新，只需要重新获取driver.page_source即可。
            return df_law_risk
    
    def guarantee(self,driver):
        driver.set_page_load_timeout(30)
        time.sleep(3)
        guarantee_page=driver.get('https://www.qixin.com/publicly/5db4a5ed-776b-46a5-a129-648a6f47de34')#使用get方法请求url，因为是模拟浏览器，所以不需要headers信息    
        html=driver.page_source#获取网页的html数据
        soup=BeautifulSoup(html,'lxml')#对html进行解析
        table_select=soup.find('div',id = 'companyEvents')
        table = table_select.find('table',class_ = 'table table-bordered')
        name=[]
        try:
            for th in table.find_all('tr')[0].find_all('th'):
                name.append(th.get_text())#获取表格的字段名称作为字典的键
        except IndexError:
            Error = '----------------------------------------------------------------'+'\n'+\
                    '-------------There is No Guarantee Record Here------------------' +'\n'+\
                    '----------------------------------------------------------------'
            return Error
        else:
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
                        df_guarantee = pd.DataFrame.from_dict(dic,orient='index').T
                        df_flag = 1
                    else:
                        df_guarantee = df_guarantee.append([dic], ignore_index=True)    
                flag=1
            df_guarantee = df_guarantee.drop('详情',axis = 1)
            return df_guarantee

    def main(self):
        driver = self.run()
        df_business_change = self.Business_change(driver)
        df_law_risk = self.law_risk(driver)
        df_guarantee  = self.guarantee(driver)

        return df_business_change,df_law_risk,df_guarantee

if __name__ == "__main__":
    a = tianyancha()
    df_business_change,df_law_risk,df_guarantee = a.main()
    print(df_business_change)
    print('\n')
    print(df_law_risk)
    print('\n')
    print(df_guarantee)


