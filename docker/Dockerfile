# set base mirror
FROM python:3.10-slim-buster

# set the working directory to app
WORKDIR /app

# copy all files in the current directory to app
COPY . .

# install the required python packages
RUN pip install --no-cache-dir -r requirements.txt

# declare the port on which the container listens
EXPOSE 8000

# run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
