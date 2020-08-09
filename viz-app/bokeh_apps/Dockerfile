FROM python:3.8.5-buster

# Copy requirements and app files
COPY . /bokeh_apps
COPY ./requirements.txt bokeh_apps/requirements.txt

# Install pip and the requirements
RUN pip install --no-cache-dir -r bokeh_apps/requirements.txt

# Run the Bokeh app servers
CMD bokeh serve ./bokeh_apps/goalies_*.py
