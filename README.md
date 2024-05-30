# TrueWind

A simple API to return true wind speed and angle.

## Usage

To use this API, perform a GET request in the following format:
```
http://127.0.0.1:5000/wind/?wind_speed=<wind_speed>&wind_angle=<wind_angle>&boat_speed=<boat_speed>
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
docker run fredsheppard/true_wind
```
