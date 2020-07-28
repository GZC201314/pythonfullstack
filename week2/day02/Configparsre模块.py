# __author:gzc
# date:2018/11/24

import configparser

config = configparser.ConfigParser()
# config["DEFAULT"] = {
#     'ServrAliveIntrval': '45',
#     'Comperssion': 'yes',
#     'ComperssionLevel': '9'
# }
# config["DEFAULT1"] = {
#     'ServrAliveIntrval': '45',
#     'Comperssion': 'yes',
#     'ComperssionLevel': '9'
# }
#
# with open('example.ini','w') as configer:
#     config.write(configer)

# 读取配置文件
config.read('example.ini')
# 除DEFAULT 模块外的其他模块
print(config.sections())
# 获取DEFAULT模块的配置项
print(config.defaults().get('servraliveintrval'))

# 获取任意配置项
print(config['DEFAULT1']['servraliveintrval'])
config['DEFAULT1']['servraliveintrval']='100'

# 删除配置项
# 删除块下面的一个配置项
config.remove_option('GZC','age')
# 删除一个块
config.remove_section('GZC')


with open('example.ini','w') as config1:
    config.write(config1)