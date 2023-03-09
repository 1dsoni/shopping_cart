# Backend for shopping api
Backend server is created using django framework. The project is divided into several "django apps".

### How to run the server in local

#### Requirements:
```
git
docker
```

#### Starting the server
```
1. clone the repository in local
2. build the docker image: docker build -t backend .
3. run the docker container: docker run -d -p 8000:8000 backend
```

### Debugging
We can check the logs of the running docker container by
```
1. list the running docker container: docker container ls
2. print logs of the container: docker logs <container_id> -f
```