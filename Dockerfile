FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04


RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends install -yq \
        python3-dev \
        python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip install flask gevent Pillow flask-cors -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    mkdir /usr/local/web
COPY ./ /usr/local/web/
EXPOSE 5000
ENTRYPOINT ["python3","/usr/local/web/app.py"]