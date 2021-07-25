'''
web自动化     python  ---浏览器驱动---->   浏览器
第三方库 selenium 1)安装 pip install selenium    2)导入  import selenium
1、ide :录制脚本
2、RC:封装了一些调用库的方法函数，及调用代理服务器执行浏览器操作
3、weddriver :驱动浏览器，利用webdriver 操作浏览器页面的元素
4、分布式

浏览器安装驱动：要找和本地浏览器对应的版本
使用步骤：
1、下载好驱动，解压后得到exe文件
2、放到python 安装目录下即可(我的在c盘：C:\Program Files\Python37

1、谷歌驱动：http://npm.taobao.org/mirrors/chromedriver/
2、火狐：   https://github.com/mozilla/geckodriver/releases
3、IE      https://selenium-release.storage.googleapis.com/index.html
4、Edge:   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
5、safari : https://developer.apple.com/safari/download/

web页面常见操作
1:打开浏览器
driver = webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
2:最大化浏览器
driver.maxmize_window()
3:前进后退和刷新操作
driver.back()   返回上一个页面
driver.forward()   前进到上一个页面
driver.refresh()   刷新页面
4：关闭浏览器
关闭Chromedriver服务(关闭所有关联的浏览器窗口 ：driver.quit()
关闭当前窗口： driver.close()

元素定位：id,name,class,tag, partial_link,link, xpath, css
id 整个html页面，就一个id,id唯一（动态id 不做考虑
如何确定id唯一： 找到对应的标签位置，点击，然后ctrl+f (最下面有搜索框），输入id对应的值。查询结果
name :不一定唯一
xpath: 路径
1、xpath 绝对路径（不推荐使用，点击对应的元素，然后点击鼠标右键，然后选择copy,选择copy xpath
2、相对路径定位
标签名+属性 ===>  //标签名[@属性名=属性值]    例：//input[@id='username']
3、层级定位
//标签名[@属性名=属性值]/标签名[@属性名=属性值]/标签名 例：//div[@class='login-logo']/b
4、文本内容定位
//标签名[text()='零售出库']
5、包含属性值：//标签名[contains(@属性名/text(),属性值)]   ---了解
   //input[contains(@class,'username')]
假设想通过变化的id 来进行元素定位，可借助属性值，attribute
ifr_id = driver.find_element_by_xpath(
'//iframe[@src=src="/pages/materials/retail_out_list.html"]').get_attribute('id')

页面框架：
在一个固定的地方可以切换多个页面，并且其他内容不变（左侧树，右侧内容，顶端导航）
左边不变，右边可以切换多个页面 ===iframe框架，整个html页面下面嵌套了一个html页面
1、识别是否有子页面的方式，页面层级路径中去找有无iframe,如有，则需切换iframe ,元素才可以定位
iframe页面切换的三种方式：1，id或name切换  2、通过webelement元素切换  3、通过iframe下标来切换
1，id或name切换
通过id或name切换:driver.switch_to.frame(id)
2、通过webelement元素切换
driver.switch_to.frame(
driver.find_element_by_xpath(
"//iframe[@id='{}']".format(iframe_id)
)
)
3、通过iframe下标来切换
通过iframe下标来定位：从0开始，第一个iframe-0 ,第二个iframe-2....
driver.switch_to.frame(1)
切换之后，就在当前html页面中了，就可以直接用元素定位方式定位

等待方式：
强制等待：time.sleep(10)--没有完成等待时间，不往下执行
显示等待：
隐式等待：可以设置一个等待时间，在这个等待时间还没结束之前，
元素找到了，就不继续等待，直接往下执行代码 driver.implicitly_wait(10)
注意：一个session会话中只需要调用一次，对整个driver周期都生效


'''
from selenium import webdriver
import time
# #启动浏览器
# driver =webdriver.Chrome()
# #打开一个erp项目地址
# driver.get('http://erp.lemfix.com/login.html')
# time.sleep(5)  # 延迟5s
#
# # 前进后退和刷新操作
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
#
# # 通过执行js文件，新开一个窗口
# js = 'window.open("http://wy.lemonban.com:3000/user.html#/pages/frame/login")'
# driver.execute_script(js)
#
# # 窗口最大化
# driver.maximize_window()
#
# # 关闭当前浏览器窗口（最先打开的那个页面）
# driver.close()

driver = webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
driver.implicitly_wait(10)
# 输入用户名和密码,并点击登录，因为有id ,所以都可以通过id查找到对应的框
driver.find_element_by_id('username').send_keys('13916686542')
driver.find_element_by_id('password').send_keys('lemon123')
driver.find_element_by_id('btnSubmit').click()
time.sleep(5)
#验证登录的用户是否跟输入的用户一致,
# 第一次报错，说找不到对应的p标签，
# 可能是页面还没有缓存出来，
# 前面加个时间time.sleep(20),给页面缓存的时间
login_user = driver.find_element_by_xpath('//p').text
if login_user == '13916686542' :
    print('这个登陆用户是{}'.format(login_user))
else :
    print ('用户名不一致，这条测试用例不通过')
# 点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()
time.sleep(10)
# 输入数据并搜索对应的结果,没有找到该元素，因为该元素是嵌套的子页面
# 要先切换到嵌套的子页面
# 通过id切换，发现找不到 ---动态id 找不到报错
# driver.find_element_by_id('tabpanel-372adhi3d-frame')
# 拓展：假设我们一定要通过id来切换，怎么实现？
# ifr_id = driver.find_element_by_xpath(
# '//iframe[@src=src="/pages/materials/retail_out_list.html"]').get_attribute('id')
# driver.switch_to.frame(ifr_id)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
driver.find_element_by_id('searchNumber').send_keys('806')
# driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys('886')
driver.find_element_by_id('searchBtn').click()
# 获取并判断查询到的内容
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-rl-2-0"]/td[@field="number"]/div').text
if '806' in num:
    print("这条测试用例通过")
else :
    print("查询结果错误！这条测试用例不通过")

time.sleep(2)
# driver.close()
