# pull python image
FROM python:3

# evironment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# craete a folder in the virtual server (Docker environment)
RUN mkdir /code
# set working folder for virtual server
WORKDIR /code

# add required text and install
ADD requirements.txt /code/
RUN pip install -U pip && pip install -r requirements.txt

# copy all content from the current directory to 'code' folder
ADD . /code/