import board
import adafruit_ahtx0

sensor = adafruit_ahtx0.AHTx0(board.I2C())


def get_state():
    return [
        ("temperature", sensor.temperature, "celcius"),
        ("humidity", sensor.relative_humidity, "%"),
    ]
