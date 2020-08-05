# FROM tiangolo/meinheld-gunicorn-flask:python3.8
FROM python:3.8.5-buster

# Copy requirements and app files
COPY . /app
COPY ./requirements.txt app/requirements.txt

# Workaround for dumb NumPy thing
# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

# Install the requirements
# RUN pip install Pillow==6.2.1 --no-cache-dir
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the Flask port and run the Flask app
# CMD ["python", "main.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000" "wsgi:app"]
