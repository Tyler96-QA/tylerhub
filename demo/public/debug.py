# from selenium import webdriver

# options=webdriver.ChromeOptions()
# options.add_argument('lang=zh_CN.UTF-8')
# options.add_argument('--incognito')
# options.add_argument('--start-maximized')

# driver=webdriver.Chrome(chrome_options=options)
# driver.get('https://www.baidu.com/')
# import logging
# def logout(name):
#     # 先创建一个logger
#     logger = logging.getLogger(name)  # 定义Logger的名字，之前直接用logging调用的名字是root，日志格式用%(name)s可以获得。这里的名字也可以自定义比如"TEST"
#     logger.setLevel(logging.DEBUG)  # 低于这个级别将被忽略，后面还可以设置输出级别
#     # 创建handler和输出级别
#     ch = logging.StreamHandler()  # 输出到屏幕的handler
#     ch.setLevel(logging.INFO)  # 输出级别和上面的忽略级别都不一样，可以看一下效果

#     # 创建日志格式，可以为每个handler创建不同的格式
#     ch_formatter = logging.Formatter('%(name)s %(asctime)s {%(levelname)s}:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')  # 关键参数datefmt自定义日期格式

#     # 把上面的日志格式和handler关联起来
#     ch.setFormatter(ch_formatter)

#     # 将handler加入logger
#     logger.addHandler(ch)

#     return logger

# logout('test').info('thuehhth')
# # # 以上就完成了，下面来看一下输出的日志
# # logger.debug('logger test debug')
# # logger.info('logger test info')
# # logger.warning('logger test warning')
# # logger.error('logger test error')
# # logger.critical('logger test critical')

# from browser_actions import Commonweb
# from selenium import webdriver
# from other_actions import public_method
# import time

# c=Commonweb()
# p=public_method()
# c.open_browser()
# c.open_web('https://www.baidu.com/')
# time.sleep(2)
# c.double_click('css,.hot-refresh-text')
# time.sleep(3)
# c.suspension('css,.s-top-right-text')
# time.sleep(1)
# c.web_click('css,.soutu-btn')
# time.sleep(2)
# c.is_element_isdisplayed('css,.upload-pic')
# c.web_click('css,.upload-pic')
# time.sleep(1)
# c.uploadimg()
# time.sleep(2)
# c.get_screenpict('baidu')
# c.web_click('css,.upload-pic')
# time.sleep(1)
# c.uploadimg()

# import os
# import time
# print(os.getcwd())
# pictour_dir=os.path.join(os.sys.path[0],'pictour')
# print(pictour_dir)
# # # pict_name=time.strftime('%Y-%m-%d-%H.%M.%S',time.localtime(time.time()))
# # # print(pict_name)
# # # pri_path=os.path.join(os.path.join(os.getcwd(),'pictour'),time.strftime('%Y-%m-%d-%H.%M.%S',time.localtime(time.time())))
# # # print(pri_path)

# # print(os.sys.path[0]) #上级目录
# # print(os.__file__)
# # print(os.path.abspath(__file__))
# # os.mkdir('pictour')
# # pict_path=os.path.join(os.sys.path[0],'picture')
# # if not os.path.exists(pict_path):
# #     os.mkdir(pict_path)
# # pict_name=os.path.join(pict_path,'{}.png'.format(54564))
# # print(pict_name)
# # # print(pict_path)
# # # print(os.path.exists('D:\master\pictour'))

# # def c(a):
# #     return a+1
    
# # c=lambda a:a+1


# # def c(a):
# #     return c+2

# # d=lambda y:test(y)
# from browser_actions import Commonweb
# from other_actions import public_method
# import time
# import datetime

# c=Commonweb()
# p=public_method()
# c.open_browser()
# c.open_web('https://at-bos-frontend-uat.atfxdev.com/login')
# c.display_input('css,.ivu-input-default','tyler.tang')
# c.display_input('css,.ivu-input-default','Tl123456',1)
# c.display_click('css,.ivu-btn-large')
# c.display_click('css,.ivu-badge>span')
# c.display_click('css,[data-old-padding-top] > [href="/client/clientListNew/:type*"]')
# c.display_input('css,.ivu-input-group-with-append > [placeholder]','1200008354')
# time.sleep(1)
# c.display_click('css,.ivu-btn-icon-only > .ivu-icon')
# time.sleep(1)
# c.display_click('css,div.ivu-table-overflowX>table>tbody.ivu-table-tbody>tr>td',1)
# c.switch_windows(1)
# time.sleep(2)
# c.display_click('css,[href="#tdAccount"]')
# time.sleep(4)
# print(c.is_element_selected('css,.ivu-checkbox-input'))
# print(c.get_attributes('css,label.switch>span.ivu-switch>input','value',2))
# time.sleep(1)
# list_len=c.get_lenofelement('xpath,//*[@id="tdAccount"]/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr/td[1]/div/div/span')
# print(list_len)
# for i in range(0,list_len):
#     if str(c.get_text('xpath,//*[@id="tdAccount"]/div[2]/div/div/div[3]/div[1]/div[2]/table/tbody/tr/td[1]/div/div/span',i))==str(693005664):
#         print(i+1)
#         break


# star=datetime.datetime.now()
# c.display_click('css,.s_btn')
# end=datetime.datetime.now()
# print(end-star)
# c.web_click('css,.blk-sure-btn')
# time.sleep(0.5)
# if c.is_displayed('css,.la-redo-alt',2):
#     print(1111)
# else:
#     print(2222)

# time.sleep(1)
# # c.display_input('css,.s_ipt','python')
# print(c.display_get_text('css,.title-content-title',1))
# c.display_click('css,.title-content-title')
# time.sleep(1)
# c.switch_windows(1)
# c.js_scroll('down')
# time.sleep(5)


# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# dr=webdriver.Chrome()
# dr.maximize_window()
# dr.get('https:\\www.baidu.com')

# ele=WebDriverWait(dr,10,0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.title-content-title')),message='timeout')
# print(ele)


#ele.click()

# from browser_actions import Commonweb
# from common_method import commonmethod
# import time
# import os

# common=Commonweb()
# dr=common.open_browser()
# commethed=commonmethod(dr)

# common.open_web('https://at-client-portal-uat.atfxdev.com/login')
# commethed.remove_register_topup()
# time.sleep(1)
# commethed.choose_register_lang('CN')
# commethed.login_cp('lemon.lin@newtype.io', 'Tl123456')
# time.sleep(10)
# print(common.element_is_visible('xpath,//div[@class="el-loading-mask"]'))
# while True:
#     text=common.get_attributes('xpath,//div[@class="el-loading-mask"]', 'style')
#     if 'display' not in text:
#         print(text)
#         continue
#     else:
#         common.display_click('xpath,//span[.="入金"]')

# import pymysql
# import pandas as pd
# conn=pymysql.connect(host='atfx2-dev.cey5cywit5mk.ap-east-1.rds.amazonaws.com',port=3306,user='atfx2-dev',password='W22b3yA3-ae9jTrerpb',db='')

# import pymongo
# import ssl

# ssl._create_default_https_context=ssl._create_unverified_context()

# ssl._create_default_https_context=ssl._create_unverified_context()



# client=pymongo.MongoClient('mongodb+srv://atfx-dev-admin:m578A3MGrcR3pRXVU2pA@atfx2-dev-loa0g.azure.mongodb.net'
# '/atfx_test?authSource=admin&replicaSet=atfx2-dev-shard-0&'
# 'readPreference=primary&appname=MongoDB%20Compass%20Community&retryWrites=true&ssl=true')

# db=client['atfxgm-uat']

# mydb=db['atfx_ib_links']
# data=mydb.find({'mtName':'mt4'}).limit(5)
# for i in data:
#     print(i['link'])

# print(type(data))
# for i in data:
#     print(data['link'])
# def A():
#     lis=[]
#     for i in 'hel':
#         dic={}
#         dic['point']=i
#         dic['key']=i
#         lis.append(dic)
#     return lis
# print(A())


# test={
#     "accountNumber": 1000000593,
#     "accountIbLink": "A03",
#     "mtPlatform": "mt4",
#     "currency": "USD",
#     "markup": "0",
#     "commission": 30,
#     "leverage": 200,
#     "mtGroup": "demoforex200",
#     "spreadType": "Edge",
#     "riskVideo": "Y",
#     "link": "+Gdea2zEybngAKqr+Jz7TgFKwooZcyQj5Sf6SnXvdqsOHcnNDE5ImIxftKiZ7QHOoP1PE6PKEPz952y/Epv1Sg==1583223302873",
#     "createBy": "admin",
#     "updateBy": "admin",
#     "isDeleted": 1,
#     "deleteDate": {
#       "$date": "2020-03-03T08:15:02.873Z"
#     },
#     "createDate": {
#       "$date": "2020-02-27T06:43:14.086Z"
#     },
#     "lastUpdateDate": {
#       "$date": "2020-02-27T06:43:14.086Z"
#     },
#     "__v": 0
# },
# {
#     "accountNumber": 1000000593,
#     "accountIbLink": "A03",
#     "mtPlatform": "mt4",
#     "currency": "USD",
#     "markup": "0",
#     "commission": 30,
#     "leverage": 100,
#     "mtGroup": "demoforex200",
#     "spreadType": "Edge",
#     "riskVideo": "Y",
#     "link": "+Gdea2zEybngAKqr+Jz7TgFKwooZcyQj5Sf6SnXvdqsQfEW5wN3JYjsVL09qzf2XoP1PE6PKEPz952y/Epv1Sg==1583223305961",
#     "createBy": "admin",
#     "updateBy": "admin",
#     "isDeleted": 1,
#     "deleteDate": {
#       "$date": "2020-03-03T08:15:05.961Z"
#     },
#     "createDate": {
#       "$date": "2020-02-27T06:43:33.613Z"
#     },
#     "lastUpdateDate": {
#       "$date": "2020-02-27T06:43:33.613Z"
#     },
#     "__v": 0
# }

# tset_list=[]
# for i in test:
#     test_dict={}
#     test_dict['link']=i['link']
#     test_dict['mtGroup']=i['mtGroup']
#     tset_list.append(test_dict)
# print(tset_list)

# dic={'currency': 'USD', 'markup': '0', 'leverage': 200, 'mtGroup': 'demoforex200', 'link': '+Gdea2zEybngAKqr+Jz7TgFKwooZcyQj5Sf6SnXvdqsOHcnNDE5ImIxftKiZ7QHOoP1PE6PKEPz952y/Epv1Sg==1583223302873'}

# print(len(dic))

# def A(d=1,a=None,b=None):
#     print(a and b != None)

# A(1)
a=None
b=None
print(a and b ==None)
print(a is None)