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
    # # cap = cv2.VideoCapture("rtsp://admin:123456@192.168.1.10:554/h264/ch1/main/av_stream")
    # cap = cv2.VideoCapture("/Users/yangwenbo/opt/output.avi")
    # while cap.isOpened():
    #     success, frame = cap.read()
    #     print(success)
    #     cv2.imshow("frame", frame)
    #     cv2.waitKey(1)
    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()