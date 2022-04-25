import cv2
from flask import Flask, render_template, Response, request

# rtsp_url = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"
# rtsp_url = "rtsp://admin:@mber@it#1997@202.4.125.250/unicast/c2/s2/live"
app = Flask(__name__)
capture = cv2.VideoCapture(rtsp_url)


def gen_frames(rtsp_url):
    while True:
        success, frame = capture.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/camera_feed', methods=['GET', 'POST'])
def camera_feed():
    return render_template('camera_stream.html')


@app.route('/video_feed', methods=['GET'])
def video_feed():
    rtsp_url = request.args['rtsp_url']

    return Response(gen_frames(rtsp_url), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_feed', methods=['POST'])
def rtsp_url():
    url = ''
    user_name = request.form['user_name']
    password = request.form['password']
    ip_address = request.form['ip_address']
    port = request.form['port']
    camera_type = request.form['camera_type']

    if camera_type == 'dahua':
        url = 'rtsp://' + user_name + ':' + password + '@' + ip_address + ':' + port + '/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>'
    elif camera_type == 'hikvision':
        url = 'rtsp://' + user_name + ':' + password + '@' + ip_address + ':' + port + '/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>'
    elif camera_type == 'uniview':
        url = 'rtsp://' + user_name + ':' + password + '@' + ip_address + ':' + port + '/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>'
    elif camera_type == 'axis':
        url = 'rtsp://' + user_name + ':' + password + '@' + ip_address + ':' + port + '/cam/realmonitor?channel=<channelNo>&subtype=<typeNo>'

    return url


if __name__ == "__main__":
    app.run(debug=False)
