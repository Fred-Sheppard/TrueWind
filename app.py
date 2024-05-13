import math
from urllib import request

from flask import request, Flask, jsonify

app = Flask(__name__)


@app.route('/wind/')
def wind():
    speed = float(request.args.get('wind_speed'))
    angle = float(request.args.get('wind_angle'))
    boat = float(request.args.get('boat_speed'))

    angle_rad = math.radians(angle)
    x = speed * math.cos(angle_rad)
    y = speed * math.sin(angle_rad)
    true_x = x - boat
    true_y = y

    true_speed = round(math.sqrt(true_x ** 2 + true_y ** 2), 2)
    true_angle = round(math.degrees(math.tan(true_y / true_x)), 2)

    return jsonify({'speed': true_speed, 'angle': true_angle})


if __name__ == '__main__':
    app.run()
