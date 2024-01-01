## gradio-docker of video-compress

### build docker
```shell
docker build . -t samge/video-compress-gradio -f docker/gradio/Dockerfile
```

### upload
```shell
docker push samge/video-compress-gradio
```

### run the docker image

create a cache mapping directory
```shell
mkdir -p ~/docker_data/video-compress/gradio_cache
```

running docker

If the `ACCESS_TOKEN` environment variable and `config.json` are configured at the same time, the value of the environment variable `ACCESS_TOKEN` is read first.

Method 1: Run by configuring `ACCESS_TOKEN` environment variables
```shell
docker run -d \
--name video-compress-gradio \
-e ACCESS_TOKEN=xxx \
-v ~/docker_data/video-compress/gradio_cache:/app/gradio_cache \
-p 7860:7860 \
--pull=always \
--restart always \
samge/video-compress-gradio:latest
```

Method 2: Run as `config.json` mapping

Here `~/docker_data/video-compress/config.json` needs to be replaced with the user's local mapping path.
```shell
docker run -d \
--name video-compress-gradio \
-v ~/docker_data/video-compress/config.json:/app/config.json \
-v ~/docker_data/video-compress/gradio_cache:/app/gradio_cache \
-p 7860:7860 \
--pull=always \
--restart always \
samge/video-compress-gradio:latest
```