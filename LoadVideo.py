import cv2

"""
    HikVision
    rtsp://[username]:[passwd]@[ip]:[port]/[codec]/[channel]/[subtype]/av_stream
    
    username：E.g admin.
    passwd：Password.
    ip：Machine's ip address，E.g 192.168.1.10.
    port：Defults 554，if your prot number is the defult,you can ignore it.
    codec：E.g h264、MPEG-4、mpeg4...
    channel：Channel number，starting at 1.
    subtype：Code stream type.(main , sub).
    
    
    Dahua
    rtsp://username:password@ip:port/cam/realmonitor?channel=1&subtype=0
    
    username：E.g admin.
    passwd：Password.
    ip：Machine's ip address，E.g 192.168.1.10.
    port：Defults 554，if your prot number is the defult,you can ignore it.
    channel：Channel number，starting at 1.
    subtype：Code stream type.(subtype=0|1).
"""
if __name__ == '__main__':
    cap = cv2.VideoCapture("rtsp://user:passwd@127.0.0.1:554/h264/ch1/main/av_stream")
    while cap.isOpened():
        success, frame = cap.read()
        cv2.imshow("frame", frame)
        cv2.waitKey(1)