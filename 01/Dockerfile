# FROM: docker image pull from docker hub.
FROM python:3.7

# ENV: Specify environment variables that is used in the Docker container
# PYTHONUNBUFFERED 1: Off the buffer of stdout and stderr.
ENV PYTHONUNBUFFERED 1

# RUN: Execute some commands in the container when building the docker image.
# mkdir /code: Make the directory named "code" under the root directory.
RUN mkdir /code

# WORKDIR: Set the working directory for any RUN, ADD and so on.
WORKDIR /code

# ADD: Add some files to the container.
ADD . /code/

# pip install ~: Install some libraries that is written in requirements.txt.
RUN pip install -r requirements.txt
