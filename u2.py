
#-*- codeing = utf-8 -*-
#@Time : 2020/9/2 10:32
#@Author :张弘彪
#@Flie : u2.py
#@Software : PyCharm

import uiautomator2 as u2

d = u2.connect('7pkr5prgfy5hmrnb') # connect to device
print(d.info)


def getQunName(qunlist):
    for item in d(resourceId="com.tencent.mm:id/b32"):
        if qunlist.count(item.get_text()) == 0:
            qunlist.append(item.get_text())
        else:
            continue
    if d(resourceId='com.tencent.mm:id/azb').exists():
        print('列表长度:' + str(len(qunlist)))
        return qunlist
    else:
        d.swipe_ext('up', 0.25)
        getQunName(qunlist)

def qf(list):
    d(text="搜索").click()


def main():
    QNlist = []
    getQunName(QNlist)


if __name__ == '__main__':
    main()
