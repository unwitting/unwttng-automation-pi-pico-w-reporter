CIRCUITPY_VOLUME=/Volumes/CIRCUITPY
MANAGED_FILES="main.py secrets.py lib"

if [ -d "$CIRCUITPY_VOLUME" ]; then
    echo "$CIRCUITPY_VOLUME is present, copying files..."
else 
    echo "$CIRCUITPY_VOLUME is not present, aborting..."
    exit 1
fi


echo "Removing old files..."
for file in $MANAGED_FILES; do
    echo "  Removing $file..."
    rm -rf "$CIRCUITPY_VOLUME"/$file
done

SENSOR_MODULES=$(python -c 'import secrets; print(" ".join(secrets.secrets["SENSOR_MODULES"]))')
for module in $SENSOR_MODULES; do
    ./add_sensor_module.sh $module
done

echo "Copying new files..."
for file in $MANAGED_FILES; do
    echo "  Copying $file..."
    cp -r $file "$CIRCUITPY_VOLUME"
done

echo "Done!"
