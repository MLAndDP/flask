from flask import Flask
from flask import request,Response, render_template
import torch
app = Flask(__name__)
model = torch.load("../faster_rcnn_r50_fpn_1x_voc0712_cpu-0c36e0a3.pth")
@app.route('/')
def hello_world():
    # 获取图片文件 name = upload
    return render_template('index.html', name="demo")

@app.route('/upload/', methods=['POST'])
def upload():
    # 获取图片文件 name = upload
    img = request.files['file']
    #TODO 调用神经网络
    img = model(img)
    print(img)
    #返回图片
    resp = Response(img, mimetype="image/jpeg")
    return resp

if __name__ == '__main__':
    app.run(port=8080)
