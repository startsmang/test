
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Project : pytest-allure-selenium-po-demo
# @Time    : 2023/2/16 14:27
# @Author  : mojin
# @Email   : 397135766@qq.com
# @File    : screen_recordings.py
# @Software: PyCharm
# -------------------------------------------------------------------------------
import cv2
import threading
import numpy as np
from PIL import ImageGrab,ImageDraw
from pynput.mouse import Controller



m=Controller()
class RecordScreen():
    def __init__(self, images_path='out.mp4'):
        self.images_path = images_path
        self.flag = False
        self._status=False

    def record_screen(self):

        screen = ImageGrab.grab()
        width, high = screen.size

        fourcc =cv2.VideoWriter_fourcc(*'avc1')
        video = cv2.VideoWriter(self.images_path, fourcc, 16, (width, high), True)
        image_lst = []
        n = 1

        while True:
            if self.flag:
                break

            img = ImageGrab.grab()
            co=m.position#获取当前鼠标位置
            x=co[0]
            y=co[1]
            draw=ImageDraw.Draw(img) #画一个鼠标
            draw.polygon([(x,y),(x+30,y+20),(x+20,y+30)],fill=(255,0,0)) #画个三角形，红色填充

            imm = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # 转为opencv的BGR模式

            image_lst.append(imm)
            video.write(imm)

            n = n + 1

        video.release()
        self._status = True

    def status(self):
        return self._status

    def stop(self):
        self.flag = True
        while True:
            if self.status():
                break

        return self.status()  #

    def start(self):
        th = threading.Thread(target=self.record_screen)
        th.start()

#
# if __name__ == '__main__':
#     new = datetime.now().strftime("%Y%m%d%H%M%S")
#     name = f"{new}.mp4"
#
#     SR = RecordScreen(name)
#     SR.start()
#
#     time.sleep(3)
#
#     new = datetime.now().strftime("%Y%m%d%H%M%S")
#     name = f"{new}.mp4"
#     SR1 = RecordScreen(name)
#     SR1.start()
#
#     time.sleep(3)
#
#     SR.stop()
#
#     time.sleep(3)
#     SR1.stop()
