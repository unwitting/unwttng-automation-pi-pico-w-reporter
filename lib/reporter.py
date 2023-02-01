import socketpool
import wifi
import ssl
import json
import time
import supervisor
import adafruit_requests
import adafruit_datetime


class Reporter:
    def __init__(self, secrets, sensors):
        self.secrets = secrets
        self.sensors = sensors
        print(
            f"""

- Boot ---
WiFi SSID: {self.secrets['WIFI_SSID']}
Device ID <{self.secrets['REPORT_STATE_DEVICE_ID']}>
Sensor location: {self.secrets['REPORT_STATE_SENSOR_LOCATION']}
Report interval: {self.secrets['POLL_INTERVAL']}s
----------
        """
        )
        self._set_up_wifi()

    def _set_up_wifi(self):
        print("- WiFi ---")
        print(f"Connecting to WiFi network {self.secrets['WIFI_SSID']}")
        pool = socketpool.SocketPool(wifi.radio)
        ssl_context = ssl.create_default_context()
        self.requests = adafruit_requests.Session(pool, ssl_context)
        wifi.radio.connect(self.secrets["WIFI_SSID"], self.secrets["WIFI_PASSWORD"])
        print(f"Connected with IP address {wifi.radio.ipv4_address}")
        if not self.remote_is_available():
            print("Remote is not available, restarting after 60 seconds")
            print("----------\n")
            time.sleep(60)
            supervisor.reload()
        print("----------\n")

    def remote_is_available(self):
        print("Checking remote availability")
        try:
            with self.requests.get(f"{self.secrets['REMOTE_PING_URL']}?ping=pong") as r:
                if r.status_code == 200:
                    data = json.loads(r.content)
                    if data.get("ping", None) == "pong":
                        print("Remote is available")
                        return True
                    print(
                        f"Error checking remote availability: Remote responded with unexpected data: {data}"
                    )
                    return False
                else:
                    print(
                        f"Error checking remote availability: Remote responded with status code {r.status_code}"
                    )
                    return False
        except Exception as e:
            print(f"Error checking remote availability: {e}")
            return False

    def report_state(self, state):
        print("Reporting state to remote")

        payload_state = []
        for sensor_hardware, sensor_state in state:
            payload_state.extend(
                [
                    {
                        "location": self.secrets["REPORT_STATE_SENSOR_LOCATION"],
                        "sensorHardware": sensor_hardware,
                        "name": name,
                        "value": value,
                        "unit": unit,
                    }
                    for name, value, unit in sensor_state
                ]
            )

        payload = {
            "reporter": {
                "type": "manual-state-reporter",
                "id": self.secrets["REPORT_STATE_DEVICE_ID"],
            },
            "state": payload_state,
        }
        for state in payload["state"]:
            if state["unit"] is None:
                del state["unit"]

        try:
            with self.requests.post(
                self.secrets["REMOTE_REPORT_STATE_URL"],
                json=payload,
            ) as r:
                if r.status_code == 200:
                    print("State reported successfully")
                    for state in payload["state"]:
                        print(
                            f" > {state['name']}: {state['value']}{state.get('unit', '')}"
                        )
                    return True
                else:
                    print(
                        f"Error reporting state: Remote responded with status code {r.status_code}"
                    )
                    return False
        except Exception as e:
            print(f"Error reporting state: {e}")
            return False

    def run(self):
        try:
            while True:
                print("- Loop ---")

                state = []
                for sensor in self.sensors:
                    state.append(
                        (
                            sensor["sensor_hardware"],
                            sensor["sensor_module"].get_state(sensor["i2c"]),
                        )
                    )

                self.report_state(state)
                print("----------\n")
                time.sleep(self.secrets["POLL_INTERVAL"])
        except Exception as e:
            print(f"Error in main run loop: {e}")
            print("Restarting after 60 seconds")
            print("----------\n")
            time.sleep(60)
            supervisor.reload()
