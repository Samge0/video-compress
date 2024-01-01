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

Using docker, if you want to compress the video according to the file path, you need to map the file path where the video is located to docker, and then use `/app/VideoDir/xxx` to operate the video file.

Otherwise, a single video file compression operation may be performed in the manner of uploading a file.


```shell
docker run -d \
--name video-compress-gradio \
-v ~/docker_data/video-compress/gradio_cache:/app/gradio_cache \
-v ~/docker_data/VideoDir:/app/VideoDir \
-p 7860:7860 \
--pull=always \
--restart always \
samge/video-compress-gradio:latest
```