from flask import Flask
from flask import request, Response, render_template
import torch
from mmdet.apis import inference_detector, init_detector, show_result
import numpy
from PIL import Image
from gevent import pywsgi
import io
import base64
from flask import jsonify, json

app = Flask(__name__)
model = init_detector(
    "/home/yons/zhengxin/mmdetection/configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712.py",
    "/home/yons/zhengxin/mmdetection/faster_rcnn_r50_fpn_1x_voc0712-acc8ede0.pth", device=torch.device('cuda', 0))


# model = torch.load()
@app.route('/')
def hello_world():
    # 获取图片文件 name = upload
    return render_template('index.html', name="demo")


class Model(object):

    def __init__(self, img, num):
        self.num = num
        self.img = img


@app.route('/upload/', methods=['POST'])
def upload():
    # 获取图片文件 name = upload
    img = request.files['file']
    score_thr = 0.9
    img = Image.open(img)
    img = numpy.asarray(img)
    result = inference_detector(model, img)
    a = numpy.zeros(shape=(0, 5))
    result = [result[i] if i == 14 else a for i in range(len(result))]
    scores = result[14][:, -1]
    inds = scores > score_thr
    result[14] = result[14][inds, :]
    img = show_result(img, result, model.CLASSES, score_thr=score_thr, wait_time=1, show=False)
    img = Image.fromarray(numpy.uint8(img))
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    # 返回图片
    # m = Model(base64.b64encode(imgByteArr),len(result[14]))
    # resp = Response(base64.b64encode(imgByteArr), mimetype="application/text")
    # return jsonify(
    #     img=base64.b64encode(imgByteArr),
    #     num=len(result[14]))
    print(type(base64.b64encode(imgByteArr)))
    return json.dumps({'img': str(base64.b64encode(imgByteArr), encoding = "utf-8"), 'num': len(result[14])}), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.debug = True
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()
