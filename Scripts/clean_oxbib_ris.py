# -*- coding= utf-8 -*-
import re

def main():
    """Fix Oxford Bibliographies' author/editor error for book chapters.
    """
    with open('/Users/smargheim/Downloads/ZOTERO.ris', 'r') as file_obj:
        data = file_obj.read()

    chaps = re.findall(r"TY\s\s-\sCHAP.*?ER\s\s-", data, re.S)

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
        print chaps[i]
        data = re.sub(chaps[i], item, data)


    with open('/Users/smargheim/Downloads/new_zotero.ris', 'w') as file_obj:
        file_obj.write(data)

    return True

if __name__ == '__main__':
    main()
