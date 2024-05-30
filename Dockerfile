# Stage 1: Build
FROM python:3.8-slim-buster AS build

WORKDIR /python-docker

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.8-slim-buster

WORKDIR /python-docker

# Copy only the necessary files from the build stage
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY . .

# Ports are exposed through kubernetes/helm

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
