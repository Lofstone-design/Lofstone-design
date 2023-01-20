import re
from lxml import etree
from xml.etree import ElementTree
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('main.html',parser=parser)
res=''
for i in range(0,len(tree.xpath('//div[@class="hidden"]/tr/td/table/tr/td/h3/text()'))):
    name = tree.xpath('//div[@class="hidden"]/tr/td/table/tr/td/h3/text()')[i]
    #print(name)
    e=etree.tostring(tree.xpath('//div[@class="hidden"]/tr')[i], encoding='utf-8', pretty_print=True, method="html").decode('utf-8')
    e=e[:3]+' id="'+name+'"'+e[3:]
    res=res+e
print(res)