# set base mirror
FROM python:3.10-slim-buster

# set the working directory to app
WORKDIR /app

# copy all files in the current directory to app
COPY . .

# install the required python packages
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r gradio_ui/requirements.txt && \
    mkdir -p /app/VideoDir

# declare the port on which the container listens
EXPOSE 7860

# map cache directory
VOLUME /app/.cache/gradio_cache
VOLUME /app/VideoDir

# run the application
CMD ["sh", "-c", "uvicorn gradio_ui.app:app"]
