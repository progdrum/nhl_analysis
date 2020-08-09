# FROM tiangolo/meinheld-gunicorn-flask:python3.8
FROM python:3.8.5-buster

# Copy requirements and app files
COPY . /app
COPY ./requirements.txt app/requirements.txt

# Install the requirements
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the Flask port and run the Flask app
CMD gunicorn --bind 0.0.0.0:5000 app.main:app
