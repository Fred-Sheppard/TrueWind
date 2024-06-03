# TrueWind

A simple API to return true wind speed and angle.

## Usage

To use this API, perform a GET request in the following format:
```
http://ab6a99ef966004288a77448dfd20b8ff-1464420605.us-east-1.elb.amazonaws.com/api/?wind_speed=10&wind_angle=45&boat_speed=5
```

### Parameters
**wind_speed**: The apparent wind speed as read from your instruments, measured in knots.


**wind_angle**: The apparent wind angle in relation to your heading, measured in degrees. 90 degrees to port can be inputted as both -90 or 270

**boat_speed**: The speed of your boat through the water in knots.

### Outputs

The output of the GET request is formatted in JSON as follows:

```json
{
  "true_angle": 89.23,
  "true_speed": 7.07
}
```

**true_speed**: The speed of the wind in knots.

**true_angle**: The angle of the wind in relation to your heading, measured in degrees.

## Hosting

To host the image locally, run the following:
```bash
docker run -p 5000:5000 fredsheppard/true_wind
```
