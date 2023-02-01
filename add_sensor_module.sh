MODULE=$1

if [ -z "$MODULE" ]; then
    echo "Usage: $0 <module>"
    exit 1
fi

MODULE_SOURCE_DIRECTORY="sensor_modules/$MODULE"

if [ ! -d "$MODULE_SOURCE_DIRECTORY" ]; then
    echo "Module $MODULE does not exist"
    exit 1
fi

echo "Installing sensor module $MODULE..."

echo "Copying files..."
for file_or_directory in $(ls $MODULE_SOURCE_DIRECTORY); do
    cp -r "$MODULE_SOURCE_DIRECTORY/$file_or_directory" lib/
done

echo "Done!"
