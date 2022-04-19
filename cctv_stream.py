import cv2
import imutils
from imutils.video import VideoStream
import numpy as np
rtsp_url = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"
# rtsp_url = "rtsp://FAruk:FAruk@45#!@202.4.125.250/media/video1"
# rtsp_url = "rtsp://FAruk:FAruk@45#!@202.4.125.254:554/cam/realmonitor?channel=1&subtype=0"
# rtsp_url = "rtsp://amberitltd:AmberIT!#1997@202.4.125.254:554/cam/realmonitor?channel=1&subtype=0"
# rtsp_url = "rtsp://admin:@mber@it#1997@202.4.125.250/unicast/c2/s2/live"


# video_stream = VideoStream(rtsp_url).start()
#
# while True:
#     frame = video_stream.read()
#     if frame is None:
#         continue
#
#     frame = imutils.resize(frame, width=800)
#     cv2.imshow('Chowdhury', frame)
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()
# video_stream.stop()

capture = cv2.VideoCapture(rtsp_url)
while True:
    ret, frame = capture.read()
    cv2.imshow('Chowdhury', frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 1:
        break

capture.release()
cv2.destroyAllWindows()
