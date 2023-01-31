export REPO_NAME="unwttng-automation-pi-pico-w-reporter"
export REPO_BRANCH="main"
export CODE_BUNDLE_URL="https://github.com/unwitting/${REPO_NAME}/archive/refs/heads/${REPO_BRANCH}.zip"
export CODE_BUNDLE_FILENAME="code.tar.gz"

echo $CODE_BUNDLE_URL
echo $CODE_BUNDLE_FILENAME

if [ "$(ls -A .)" ]; then
    echo "Current directory is not empty, aborting..."
    exit 1
fi

echo "Downloading code bundle..."
curl -L -o "$CODE_BUNDLE_FILENAME" "$CODE_BUNDLE_URL"

echo "Extracting code bundle..."
tar -xzf "$CODE_BUNDLE_FILENAME"

echo "Removing code bundle..."
rm "$CODE_BUNDLE_FILENAME"

echo "Expanding directory..."
mv ${REPO_NAME}-${REPO_BRANCH}/* ./
mv ${REPO_NAME}-${REPO_BRANCH}/.* ./
rm -rf ${REPO_NAME}-${REPO_BRANCH}/

echo "Done! Run setup_pi.sh to install firmware and push_to_pi.sh to copy project files."
