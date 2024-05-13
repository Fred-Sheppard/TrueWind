# TrueWind

A simple API to return true wind speed and angle.

## Usage

```bash
curl http://localhost:5000/wind/\?wind_speed=5\&wind_angle=180\&boat_speed=5
```

### Parameters
**wind_speed**: The apparent wind speed as read from your instruments, measured in knots.


**wind_angle**: The apparent wind angle in relation to your heading, measured in degrees. 90 degrees to port can be inputted as both -90 or 270

**boat_speed**: The speed of your boat through the water in knots.

### Outputs

**true_speed**: The speed of the wind in knots.

**true_angle**: The angle of the wind in relation to your heading, measured in degrees.
