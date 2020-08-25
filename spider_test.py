from selenium import webdriver
from lxml import html
from selenium.webdriver.common.action_chains import ActionChains
import time
'''
    第一行tr[1]....以此类推 第一行第一列 td[1]...以此类推 
    em : 新增关键字（红色）
'''
# chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# browser = webdriver.Chrome(executable_path=chromedriver_path)
browser = webdriver.Chrome()
page = browser.get('https://www.qixin.com/company/06a8671f-693d-4ec4-b317-96ff0ce6a3ad?section=changeInfo')

html_source = browser.page_source
tree = html.fromstring(html_source)
content = tree.xpath('//*[@id="changeInfo"]/div[2]/div[2]/nav/ul/li')

# menu_table = tree.find_element_by_xpath('//*[@id="changeInfo"]/table/tbody')
# rows = tree.find_elements_by_tag_name('tr')
# print(rows)
# table = page.find_element_by_id('table')
print(content)
def get_table_content(tableId,page): 
    arr = [] 
    arr1 = []  
    table_loc = (By.ID,tableId) 
    # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据 
    table_tr_list = page.find_element(*table_loc).find_elements(By.TAG_NAME, "tr") 
    for tr in table_tr_list: 
        arr1 = (tr.text).split(" ") #以空格拆分成若干个(个数与列的个数相同)一维列表 
        # print(tr.text) 
        # print(arr1) 
        arr.append(arr1)  #将表格数据组成二维的列表 
    return arr

def get_dept_list(driver):
        row= driver.find_elements_by_tag_name('tr')
        list1=[]
        for i in row:
            j=i.find_elements_by_tag_name('td')
            for item in j:
                text=item.text
                list1.append(text)
        logging.info('返回的列表数据是{0}'.format(list1))
        return list1
# get_dept_list(browser)
# pre_name = tree.xpath('//*[@id="changeInfo"]/table/tbody/tr[1]/td[4]/a/text()')
# after_name = tree.xpath('//*[@id="changeInfo"]/table/tbody/tr[1]/td[5]/a/text()')#  变更后人名
# delete = tree.xpath('//*[@id="changeInfo"]/table/tbody/tr[1]/td[4]/gm_del/text()')
# changed_name = [y for y in after_name if y not in pre_name]
# //*[@id="changeInfo"]/table/tbody/tr[1]/td[2]
# //*[@id="changeInfo"]/table/tbody/tr[1]/td[4]
# //*[@id="changeInfo"]/table/tbody/tr[1]/td[4]/a[2]
# //*[@id="changeInfo"]/table/tbody/tr[2]/td[5]
# print(delete)
# print(content)
# print(pre_name)
# print(after_name)
# print(changed_name)
