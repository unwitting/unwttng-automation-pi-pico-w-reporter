import adafruit_ahtx0


def get_state(i2c):
    sensor = adafruit_ahtx0.AHTx0(i2c)
    return [
        ("temperature", sensor.temperature, "celcius"),
        ("humidity", sensor.relative_humidity, "%"),
    ]
