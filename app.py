from flask import Flask
from flask import request, render_template
# from mmdet.apis import inference_detector, init_detector, show_result
from PIL import Image
from gevent import pywsgi
import gevent
import io
import base64
from flask import json
from flask_cors import *
from threading import Condition

class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.condition = Condition()

    def waiting(self):
        self.condition.acquire()
        try:
            while self.count > 0:
                self.condition.wait()
        finally:
            self.condition.release()

    def count_down(self):
        self.condition.acquire()
        self.count -= 1
        if self.count <= 0:
            self.condition.notifyAll()
        self.condition.release()


app = Flask(__name__)
CORS(app, resources=r'/*')
@app.route('/')
def hello_world():
    # 获取图片文件 name = upload
    return render_template('index.html', name="demo")

@app.route('/upload', methods=['POST'],strict_slashes=False)
def upload():
    # 获取图片文件 name = upload
    img = request.files['file']
    img = Image.open(img)
    list = [[0 for i in range(4)] for j in range(5)]
    print(list)
    count = CountDownLatch(20)
    cutAndDetect(img, list, 1094, 912, count)
    count.waiting()
    return json.dumps({'img': list}), 200, {'ContentType': 'application/json'}

def cutAndDetect(im, list, vx, vy, count):
    dx = vx
    dy = vy
    x1 = 0
    y1 = 0
    x2 = vx
    y2 = vy
    xNum = 0
    yNum = 0
    while xNum <= 4:
        while yNum <= 3:
            g = gevent.spawn(check, im, x1, y1, x2, y2, list, xNum, yNum, count)
            g.join()
            yNum += 1
            y1 = y1 + dy
            y2 = y1 + vy
        yNum = 1
        xNum += 1
        x1 = x1 + dx
        x2 = x1 + vx
        y1 = 0
        y2 = vy

def check(im, x1, y1, x2, y2, list, i1, i2, count):
    im2 = im.crop((x1, y1, x2, y2))
    # TODO 这里引入目标检测并标注boundingBox

    im2 = im2.transpose(Image.ROTATE_90)
    imgByteArr = io.BytesIO()
    im2.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    list[i1][i2]=str(base64.b64encode(imgByteArr), encoding="utf-8")
    count.count_down()


if __name__ == '__main__':

    app.debug = True
    server = pywsgi.WSGIServer(("0.0.0.0", 5000), app)
    server.serve_forever()


