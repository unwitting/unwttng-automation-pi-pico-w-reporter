# unwttng-automation-pi-pico-w-reporter

A skeleton general-purpose data reporting project. Made to run on the **Raspberry Pi Pico W**, and built with CircuitPython. Data is logged to a configurable endpoint, but the data format used by `unwttng-automation-functions` is assumed.

## Get started

### Create project directory

Create an empty project directory, let's say `my-new-reporter`. `cd` into it.

```bash
curl https://raw.githubusercontent.com/unwitting/unwttng-automation-pi-pico-w-reporter/main/initialise_project_directory.sh | bash
```

This will set up a project directory with the base code to get started.

### Install CircuitPython firmware

From here, you can:

```bash
./setup_pi.sh
```

to install the correct firmware onto a Pi Pico in bootloader mode.

### Add sensor modules

For each sensor module you'd like to install, run:

```bash
./add_sensor_module.sh <module_id>
```

where module ID is one of the supported sensors:

* `aht20`: AHT20 temperature & humidity sensor

### Configure with secrets.py

You'll need to create one file yourself: `secrets.py`, in the root of the project.

It should export a Python dictionary called `secrets` with the following entries:

```python
secrets = {
    # Your WiFi SSID
    "WIFI_SSID": "---",
    # Your WiFi password
    "WIFI_PASSWORD": "---",

    # Ping-able URL: the reporter will issue a HTTP GET request to it with '?ping=pong' as a query string,
    # and expect a JSON response that looks like {ping: "pong"}
    "REMOTE_PING_URL": "https://---",

    # Reporting URL: the reporter will HTTP POST data (in JSON format) to it on each poll
    "REMOTE_REPORT_STATE_URL": "https://---",

    # A unique ID for this reporting device in the fleet
    "REPORT_STATE_DEVICE_ID": "---",

    # A location string (a/string/with/optional/slashes) denoting the physical location of the sensors
    "REPORT_STATE_SENSOR_LOCATION": "testlocation1",

    # How many seconds between sensor polls?
    "POLL_INTERVAL": 10,
}
```

### Run on the Pi

Push the project's code to a Pi Pico W mounted as `CIRCUITPY`:

```bash
./push_to_pi.sh
```
