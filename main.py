from secrets import secrets
from reporter import Reporter


import board
import busio
import time

SDA = board.GP0
SCL = board.GP1
i2c = busio.I2C(SCL, SDA)

indicator_led = None
if "INDICATOR_LED_PIN" in secrets:
    import digitalio

    indicator_led = digitalio.DigitalInOut(getattr(board, secrets["INDICATOR_LED_PIN"]))
    indicator_led.direction = digitalio.Direction.OUTPUT


class IndicatorLed:
    def __init__(self, led):
        self.led = led

    def flash(self, period):
        # Fake a PWM that's mostly off, since the LED is too bright
        now = time.monotonic()
        while time.monotonic() - now < period:
            self.led.value = True
            time.sleep(0.0001)
            self.led.value = False
            time.sleep(0.002)


indicator_led = IndicatorLed(indicator_led) if indicator_led else None


sensors = []
if "aht20" in secrets["SENSOR_MODULES"]:
    import sensor_module_aht20

    sensors.append(
        {
            "sensor_hardware": "aht20",
            "sensor_module": sensor_module_aht20,
            "i2c": i2c,
        }
    )
if "adafruit_stemma_soil" in secrets["SENSOR_MODULES"]:
    import sensor_module_adafruit_stemma_soil

    sensors.append(
        {
            "sensor_hardware": "adafruit_stemma_soil",
            "sensor_module": sensor_module_adafruit_stemma_soil,
            "i2c": i2c,
        }
    )
if "ms8607" in secrets["SENSOR_MODULES"]:
    import sensor_module_ms8607

    sensors.append(
        {
            "sensor_hardware": "ms8607",
            "sensor_module": sensor_module_ms8607,
            "i2c": i2c,
        }
    )

r = Reporter(secrets, sensors, indicator_led=indicator_led)
r.run()
