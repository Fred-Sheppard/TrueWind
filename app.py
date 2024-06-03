import math
import os
import sqlite3

import boto3
from flask import request, Flask, jsonify

app = Flask(__name__)

# Configure S3
s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'true-wind-bk'
db_file_name = 'truewind.db'
local_db_path = f'/tmp/{db_file_name}'


def download_db_from_s3():
    if not os.path.exists(local_db_path):
        s3.download_file(bucket_name, db_file_name, local_db_path)


@app.route('/')
def home():
    return """<h1>Welcome to Wind API</h1>
Enter a request in the form 
&lt;address&gt;/api/?wind_speed=10&wind_angle=45&boat_speed=6<br>"""


@app.route('/history/')
def history():
    # Download the database from S3
    download_db_from_s3()

    # Open the database connection
    conn = sqlite3.connect(local_db_path)
    cursor = conn.cursor()

    # Example: Fetching some data from the database
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    cursor.execute("SELECT * FROM request_history")
    db_result = cursor.fetchall()
    conn.close()
    html = '<h1>History</h1><br><strong>Request Time | Boat Speed | Wind Speed | Wind Angle</strong><br>'
    for entry in db_result:
        html += f'{entry}<br>'
    return html


@app.route('/api/')
def api():
    # noinspection PyBroadException
    try:
        speed = float(request.args.get('wind_speed'))
        angle = float(request.args.get('wind_angle'))
        boat = float(request.args.get('boat_speed'))
    except Exception:
        return """
<h1>GET request formatting error</h1>
Enter a request in the form 
&lt;address&gt;/api/?wind_speed=10&wind_angle=45&boat_speed=6"""

    angle_rad = math.radians(angle)
    x = speed * math.cos(angle_rad)
    y = speed * math.sin(angle_rad)
    true_x = x - boat
    true_y = y

    true_speed = round(math.sqrt(true_x ** 2 + true_y ** 2), 2)
    true_angle = round(math.degrees(math.tan(true_y / true_x)), 2)

    return jsonify({'true_speed': true_speed, 'true_angle': true_angle})


if __name__ == '__main__':
    app.run(debug=True)
