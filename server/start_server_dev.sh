# You can add environment variables to this script that you might otherwise add as command line arguments in the `docker-compose` commands.

echo "Server is running in development environment"

# How to make this container available on the network: https://pythonspeed.com/articles/docker-connection-refused/
uvicorn main:app --reload --host=0.0.0.0
#uvicorn main:app --reload --host=192.168.1.155
