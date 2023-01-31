# unwttng-automation-pi-pico-w-reporter

A skeleton general-purpose data reporting project. Made to run on the **Raspberry Pi Pico W**, and built with CircuitPython. Data is logged to a configurable endpoint, but the data format used by `unwttng-automation-functions` is assumed.

## Get started

Create an empty project directory, let's say `my-new-reporter`. `cd` into it.

```bash
curl https://raw.githubusercontent.com/unwitting/unwttng-automation-pi-pico-w-reporter/latest/initialise_project_directory.sh | bash
```

This will set up a project directory with the base code to get started.

From here, you can:

```bash
./setup_pi.sh
```

to install the correct firmware onto a Pi Pico in bootloader mode, and then:

```bash
./push_to_pi.sh
```

to push the current state of the working directory to a Pi Pico in runtime mode.
