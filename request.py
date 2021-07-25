import requests
import jsonpath

# 注册
url_reg = 'http://47.115.15.198:7001/smarthome/user/register'
data_reg= {"phone":"13112341000",
           "pwd":"1234567a",
           "rePwd":"1234567a",
           "userName":"柠檬dls",
           "verificationCode":"lemon"}
header_reg = {'X-Lemonban-Media-Type':'lemonban.v2',
                'Content-Type':'application/json'}

res_reg = requests.post(url=url_reg,json=data_reg,headers=header_reg)
print(res_reg.json())  # json():获取响应正文为json格式，以字典数据返回
# print(res_reg.content.decode('utf8'))  # content:获取二进制内容，例如 图片文件 ，需要手动解码utf8
# print(res_reg.text())  # text : 文本格式，获取响应正文文本，以str数据返回，自动解码

# 登录
url_login = 'http://47.115.15.198:7001/smarthome/user/login'
data_login = {
  "pwd": "1234561a",
  "userName": "八戒12"
}
header_login = {'X-Lemonban-Media-Type':'lemonban.v2',
                'Content-Type':'application/json'}

res_login = requests.post(url=url_login,json=data_login,header=header_login).json()

# 获取token.id
# 方法1：通过字典嵌套取值
# token = res_login['data']['token_info']['token']
# user_id = res_login['data']['id']
# print(token,user_id)
# 方法2：jsonpath  --第三方库 1）安装 pip install jsonpath 2)导入：import jsonpath
token = jsonpath.jsonpath(res_login,'$.data.token_info.token')[0]  #不加【0】,取出的是list类型
user_id = jsonpath.jsonpath(res_login,'$..id')[0]
print(token,user_id)

# 完善商户信息
url_comp = 'http://47.115.15.198:7001/smarthome/merchant/complete'
data_comp = {
  "address": "湖南省长沙市岳麓区xx街道12345678901234567",
  "establishDate": "2021-04-02",
  "legalPerson": "韩",
  "licenseCode": "xh430646464sdfa",
  "licenseUrl": "http://127.0.0.1/smarthome/aaa.jpg",
  "merchantName": "青海文梅科技有限公司1234567890",
  "merchantType": 2,
  "registerAuthority": "城中区派出所123456789012345678901234",
  "tel": "18888888888",
  "userId": user_id,
  "validityDate": "2033-05-02"

}
header_comp = {'X-Lemonban-Media-Type':'lemonban.v2',
                'Content-Type':'application/json','Authorization':'Bearer '+token}

res_comp = requests.put(url=url_comp,json=data_comp,headers=header_comp).json()

# 封装成函数
def api_fun (url,data):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
                    'Content-Type': 'application/json'}
    res = requests.post(url=url,json=data,headers=header).json()
    return res

# 调用函数
url_login = 'http://47.115.15.198:7001/smarthome/user/login'
data_login = {
  "pwd": "1234561a",
  "userName": "八戒12"
}
res_login= api_fun(url_login,data_login)
print(res_login)

# 如何测试文件上传
'''
文件上传使用的content type
基本步骤：
构建文件数据，通过open函数以二进制方式打开文件
构建相关数据
发送请求，将文件数据以files参数传入，其他消息体数据通过data或json传入


'''
url_file = 'http://47.115.15.198:7001/smarthome/file/upload'
header_file = {'X-Lemonban-Media-Type': 'lemonban.v2'}
files = {'file':('aaa.png',open('aaa.png','rb'),'image/png')}
res_file = requests.post(url=url_file,data=files,headers=header_file).json()


# get 请求方法，定义参数，
url_code = "http://47.115.15.198:7001/smarthome/verificationCode/message"
param_code = {"phone":"13112341234"}
header_code = {'X-Lemonban-Media-Type': 'lemonban.v2'}
res_code = requests.get(url_code,param_code,header = header_code).json()
