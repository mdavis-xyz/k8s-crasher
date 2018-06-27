set -e
set -x
IMAGE_NAME="mlda065/crasher"
sudo docker build -t $IMAGE_NAME ./app
sudo docker push $IMAGE_NAME
