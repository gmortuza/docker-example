# Docker-example
A simple python app that uses docker. 
## Build
To build the Docker file use the following command.

```
sudo docker build -t docker-example .
```
## Run
To run the docker image as a container use the following command:

```
sudo docker run -it docker-example
```
As this docker image takes input from user in terminal. You must run it with `-it`.

## Copy file from docker container to host

Run the `docker cp` command to copy the file from docker container to host.
In this case use the following command:
```
sudo docker cp [container_name]:/test.txt .
```
You can get the container name using the following command.
```
sudo docker ps -a
```
