# Stage 1: Builder
FROM python:3.8-slim-buster as builder

WORKDIR /python-docker

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Final
FROM python:3.8-slim-buster

WORKDIR /python-docker

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /python-docker /python-docker

EXPOSE 5000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
