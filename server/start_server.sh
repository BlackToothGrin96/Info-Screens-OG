# You can add environment variables to this script that you might otherwise add as command line arguments in the `docker-compose` commands.

# export ROLE_ARN=$1
# echo "ROLE_ARN:" $ROLE_ARN
# export BUCKET_NAME=$2
# echo "BUCKET_NAME:" $BUCKET_NAME
echo "Server is running in production environment"

# How to make this container available on the network: https://pythonspeed.com/articles/docker-connection-refused/
uvicorn main:app --host=0.0.0.0 --port=8000
