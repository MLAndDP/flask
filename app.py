from flask import Flask
from flask import request,Response, render_template
import torch
from mmdet.apis import inference_detector, init_detector, show_result
import numpy
from PIL import Image
app = Flask(__name__)
model = init_detector(
        "../configs/pascal_voc/faster_rcnn_r50_fpn_1x_voc0712.py", "../faster_rcnn_r50_fpn_1x_voc0712_cpu-0c36e0a3.pth", device=torch.device('cuda', 0))
# model = torch.load()
@app.route('/')
def hello_world():
    # 获取图片文件 name = upload
    return render_template('index.html', name="demo")

@app.route('/upload/', methods=['POST'])
def upload():
    # 获取图片文件 name = upload
    img = request.files['file']
    img = Image.open(img)
    img = numpy.array(img)
    result = inference_detector(model, img)
    img = show_result(img, result, model.CLASSES, score_thr=0.5, wait_time=1)
    # img = cv2.read
    #TODO 调用神经网络
    # img = model(img)
    print(img)
    #返回图片
    resp = Response(img, mimetype="image/jpeg")
    return resp

if __name__ == '__main__':
    app.run(port=8080)
