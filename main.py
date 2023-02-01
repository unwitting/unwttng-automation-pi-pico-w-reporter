from secrets import secrets
from reporter import Reporter


import board
import busio

SDA = board.GP0
SCL = board.GP1
i2c = busio.I2C(SCL, SDA)


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

r = Reporter(secrets, sensors)
r.run()
