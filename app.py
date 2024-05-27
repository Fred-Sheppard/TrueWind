import math
from urllib import request

from flask import request, Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return """<h1>Welcome to Wind API</h1>
Enter a request in the form 
&lt;address&gt;/wind/?wind_speed=10&wind_angle=45&boat_speed=5"""


@app.route('/wind/')
def wind():
    # noinspection PyBroadException
    try:
        speed = float(request.args.get('wind_speed'))
        angle = float(request.args.get('wind_angle'))
        boat = float(request.args.get('boat_speed'))
    except Exception:
        return """
<h1>GET request formatting error</h1>
Enter a request in the form 
&lt;address&gt;/wind/?wind_speed=10&wind_angle=45&boat_speed=5"""

    angle_rad = math.radians(angle)
    x = speed * math.cos(angle_rad)
    y = speed * math.sin(angle_rad)
    true_x = x - boat
    true_y = y

    true_speed = round(math.sqrt(true_x ** 2 + true_y ** 2), 2)
    true_angle = round(math.degrees(math.tan(true_y / true_x)), 2)

    return jsonify({'true_speed': true_speed, 'true_angle': true_angle})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
