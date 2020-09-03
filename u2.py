
#-*- codeing = utf-8 -*-
#@Time : 2020/9/2 10:32
#@Author :wai
#@Flie : u2.py
#@Software : PyCharm

import uiautomator2 as u2
import time
import re

d = u2.connect('你自己设备的编号填这里') # connect to device
print(d.info)


def getQunName(qunlist):
    for item in d(resourceId="com.tencent.mm:id/b32"):
        if qunlist.count(item.get_text()) == 0:
            qunlist.append(item.get_text())
        else:
            continue
    if d(resourceId='com.tencent.mm:id/azb').exists():
        print('列表长度:' + str(len(qunlist)))
        d.press("back")
        return qunlist
    else:
        d.swipe_ext('up', 0.25)
        getQunName(qunlist)

def qf(QNlist):
    for item in QNlist:
        #过滤带圈字母，防止群名因含有带圈字母而搜索不到群名
        qn = re.sub(u'[\u24b6-\u24e9]','',item)
        print(qn)

        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d.send_keys(qn)  # adb广播输入 输入群名
        d.set_fastinput_ime(False)  # 切换成正常的输入法

        d(resourceId="com.tencent.mm:id/gbv",text=item).click()
        d(resourceId="com.tencent.mm:id/g78").click()

        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d.send_keys("群发内容")  # adb广播输入 输入群名
        d.set_fastinput_ime(False)  # 切换成正常的输入法

        d(resourceId="com.tencent.mm:id/anv", text="发送").click()
        print("已向" + item + "群发送成功")
        d.press("back")
        d(resourceId="com.tencent.mm:id/bhn", text=qn).click()
        d.clear_text()

        time.sleep(3)


def main():
    QNlist = []
    getQunName(QNlist)

    d(resourceId="com.tencent.mm:id/cns", text="微信").click()
    d(resourceId="com.tencent.mm:id/cn1").click()
    qf(QNlist)

if __name__ == '__main__':
    main()
