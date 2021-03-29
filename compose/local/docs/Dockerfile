FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
RUN apt-get install python-pip python-dev build-essential libyaml-dev git -y

RUN pip install mkdocs

RUN apt-get update -y && apt-get install -y \
    apache2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./compose/local/docs/run.sh /run.sh
RUN chmod +x /run.sh
CMD ["run.sh"]
WORKDIR /docs
