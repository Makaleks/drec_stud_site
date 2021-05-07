FROM python:3.6.8

WORKDIR /app
RUN apt-get update && apt-get install --yes unzip postgresql postgresql-contrib
# RUN pip install --upgrade pip
COPY requirements.txt .
COPY src/requirements.txt ./src/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .
RUN chmod +x ./docker_run.sh
ENTRYPOINT ["./docker_run.sh"]