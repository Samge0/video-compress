## docker of video-compress

### build docker
```shell
docker build . -t samge/video-compress -f docker/Dockerfile
```

### upload
```shell
docker push samge/video-compress
```

### run the docker image
If the `ACCESS_TOKEN` environment variable and `config.json` are configured at the same time, the value of the environment variable `ACCESS_TOKEN` is read first.

Method 1: Run by configuring `ACCESS_TOKEN` environment variables
```shell
docker run -d \
--name video-compress \
-e ACCESS_TOKEN=xxx \
-p 8233:8000 \
--pull=always \
--restart always \
samge/video-compress:latest
```

Method 2: Run as `config.json` mapping

Here `~/docker_data/video-compress/config.json` needs to be replaced with the user's local mapping path.
```shell
docker run -d \
--name video-compress \
-v ~/docker_data/video-compress/config.json:/app/config.json \
-p 8233:8000 \
--pull=always \
--restart always \
samge/video-compress:latest
```