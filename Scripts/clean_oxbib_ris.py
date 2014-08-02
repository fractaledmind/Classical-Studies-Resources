import re
import xmltodict
import json


ris = open('/Users/smargheim/Downloads/ZOTERO.ris', 'r')
data = ris.read()
ris.close()

chaps = re.findall("TY\\s\\s-\\sCHAP.*?ER\\s\\s-", data, re.S)

chs = []
for ch in chaps:
	n1 = re.sub("T1", "sub", ch)
	n2 = re.sub("AU", "ed", n1)
	n3 = re.sub("T2", "T1", n2)
	n4 = re.sub("A2", "AU", n3)
	n5 = re.sub("sub", "T2", n4)
	f = re.sub("ed", "A2", n5)
	chs.append(f)

for i, item in enumerate(chs):
	data = re.sub(chaps[i], item, data)


ris = open('/Users/smargheim/Downloads/horace.ris', 'w')
ris.write(data)
ris.close()

