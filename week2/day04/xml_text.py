#__author:gzc
#date:2019/1/9

import xml.etree.ElementTree as ET

tree = ET.parse('plant')
root = tree.getroot()
print(root.tag)
plant: object

# 查找遍历XML文件
# for plant in root:
#     print(plant.tag,plant.attrib)
#     for i in plant:
#         print(i.tag,i.text)
for node in root.iter('PRICE'):
    new_price = float(node.text.replace('$',''))+1
    node.text = '$'+str(new_price)
    node.set('updateed','yes')

tree.write('plant_new.xml')