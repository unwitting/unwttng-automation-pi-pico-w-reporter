export CODE_BUNDLE_URL="https://github.com/unwitting/unwttng-automation-pi-pico-w-reporter/archive/refs/heads/main.zip"
export CODE_BUNDLE_FILENAME="code.tar.gz"

if [ "$(ls -A .)" ]; then
    echo "Current directory is not empty, aborting..."
    exit 1
fi

echo "Downloading code bundle..."
curl "$CODE_BUNDLE_URL" -o "$CODE_BUNDLE_FILENAME"

echo "Extracting code bundle..."
tar -xzf "$CODE_BUNDLE_FILENAME"

echo "Removing code bundle..."
rm "$CODE_BUNDLE_FILENAME"

echo "Done! Run setup_pi.sh to install firmware and push_to_pi.sh to copy project files."
