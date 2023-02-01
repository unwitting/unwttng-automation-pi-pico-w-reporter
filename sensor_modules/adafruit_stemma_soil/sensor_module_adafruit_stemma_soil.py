from adafruit_seesaw.seesaw import Seesaw


def get_state(i2c):
    sensor = Seesaw(i2c, addr=0x36)
    return [
        ("soil-moisture", sensor.moisture_read(), None),
        ("soil-temperature", sensor.get_temp(), "celcius"),
    ]
