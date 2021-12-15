FROM python:3.7-alpine
MAINTAINER Matías Cárdenas

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

# uses de package manager that comes with alpine, and adds postgresql package
# --update: update the registry before we add with
# --no-cache: don't store the registry index on our dockerfile
# as we want to minimize number of packages used by our docker container
RUN apk add --update --no-cache postgresql-client

# temporary packages that need to be while installing requirements
# and then they can be removed
# setup an alias to the dependencies to easily remove them later
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

# remove the dependencies with the alias we set before
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user