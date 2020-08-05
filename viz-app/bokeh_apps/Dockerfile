FROM ubuntu:18.04

# Copy requirements and app files
COPY . /bokeh_apps
COPY ./requirements.txt bokeh_apps/requirements.txt

# Install pip and the requirements
RUN set -xe \
    && apt-get update \
    && apt-get install -y python3.8 python3-pip
RUN pip3 install --no-cache-dir -r bokeh_apps/requirements.txt

# Run the Bokeh app servers
# TODO: Run this in a separate container and use docker-compose
CMD bokeh serve ./bokeh_apps/goalies_*.py
