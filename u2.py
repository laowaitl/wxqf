
#-*- codeing = utf-8 -*-
#@Time : 2020/9/2 10:32
#@Author :张弘彪
#@Flie : u2.py
#@Software : PyCharm

import uiautomator2 as u2
import time
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
        d.press("back")
        return qunlist
    else:
        d.swipe_ext('up', 0.25)
        getQunName(qunlist)

def qf(QNlist):
    for item in QNlist:
        d(resourceId="com.tencent.mm:id/cns", text="微信").click()
        d(resourceId="com.tencent.mm:id/f8y").click()

        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d.send_keys(item)  # adb广播输入 输入群名
        d.set_fastinput_ime(False)  # 切换成正常的输入法

        d(text=item).click()
        d(resourceId="com.tencent.mm:id/g78").click()

        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d.send_keys("建设厅ABC/管理岗/特工/标准员/二建继续教育代看考试 \nAB新培报名/网课视频加急处理欢迎咨询\n快速处理钜惠！张 18388367047   ")  # adb广播输入 输入群名
        d.set_fastinput_ime(False)  # 切换成正常的输入法

        d(resourceId="com.tencent.mm:id/anv", text="发送").click()
        d.press("back")
        time.sleep(1000)

def main():
    QNlist = []
    getQunName(QNlist)
    qf(QNlist)

if __name__ == '__main__':
    main()
