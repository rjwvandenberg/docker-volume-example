# Data persistence using docker volume. #

start.py contains a script that reads a number from a file prints it to standard output and saves the next number up to the file

First build a container with this script and run it:

```
docker build . -t startup_counter
docker run --name counter -t startup_counter
```

It should output 0 

Next start restart the container and inspect the logs

```
docker start counter
docker logs counter
```

It should output 0 and 1.

Imagine we want to update our application with a new version. We would need to recreate the container to update the application files:

```
docker rm counter
docker run --name counter -t startup_counter
```

This outputs 0, meaning we lost all the data.

To solve this we need some place to store our data that survives recreating the container.
One way of doing this is to use a docker volume: https://docs.docker.com/engine/admin/volumes/volumes/#start-a-service-with-volumes

```
docker volume create --name startup-counter-vol
```

We now recreate the container and link the volume to the /app directory

```
docker rm counter
docker run --name counter -v startup-counter-vol:/app -t startup_counter
```

Run it a couple more times and look at the output.

```
docker start counter
docker logs counter
```

The file is now saved inside the volume, meaning we can recreate the container without losing the data.

```
docker rm counter
docker run --name counter -v startup-counter-vol:/app -t startup_counter
```

This last command should output a number greater than 0 as we expected.

This will work for an application with a single process active at a time, multiple containers will likely require a different solution.
