BOOTLOADER_VOLUME=/Volumes/RPI-RP2
FIRMWARE_FILE="bin/adafruit-circuitpython-raspberry_pi_pico_w-en_GB-20230130-72981cf.uf2"

if [ -d "$BOOTLOADER_VOLUME" ]; then
    echo "$BOOTLOADER_VOLUME is present, copying firmware..."
else 
    echo "$BOOTLOADER_VOLUME is not present, aborting..."
    exit 1
fi

cp -r "$FIRMWARE_FILE" "$BOOTLOADER_VOLUME"
echo "Done! Pi should now reboot and mount as CIRCUITPY. Run push_to_pi.sh to copy project files."
