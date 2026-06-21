# start from an official Python image. 
# slim means minimal size, no unnecessary packages.
FROM python:3.11-slim

# all commands from here run inside /app folder inside 
# the container.
WORKDIR /app

#  copy requirements first, before the app code. 
# This is intentional — Docker caches layers, 
# so if your code changes but requirements don't, 
# it skips the slow pip install step.
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy your app folder into the container.
COPY ./app ./app

#  tells Docker this container listens on port 8000. 
# Just documentation, doesn't actually open the port.
EXPOSE 8000

# the command that runs when the container starts. 
# Notice --host 0.0.0.0 — without this the app only 
# listens inside the container and you can't reach it 
# from outside.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]