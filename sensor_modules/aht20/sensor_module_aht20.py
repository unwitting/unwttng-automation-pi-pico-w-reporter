import board
import busio
import adafruit_ahtx0

SDA = board.GP0
SCL = board.GP1

i2c = busio.I2C(SCL, SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)


def get_state():
    return [
        ("temperature", sensor.temperature, "celcius"),
        ("humidity", sensor.relative_humidity, "%"),
    ]
