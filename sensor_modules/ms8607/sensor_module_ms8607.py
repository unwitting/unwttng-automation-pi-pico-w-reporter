from adafruit_ms8607 import MS8607


def get_state(i2c):
    sensor = MS8607(i2c)
    return [
        ("temperature", sensor.temperature, "celsius"),
        ("humidity", sensor.relative_humidity, "%"),
        ("pressure", sensor.pressure, "hPa"),
    ]
