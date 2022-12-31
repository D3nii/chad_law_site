FROM ubuntu:latest

# Copy local code to the container image.
ENV APP_HOME /app
ENV PYTHONUNBUFFERED True
WORKDIR $APP_HOME

ADD * /
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies and Gunicorn
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install --no-cache-dir -r /tmp/requirements.txt && pip install --no-cache-dir gunicorn

# Copy the rest of the codebase into the image
COPY --chown=app:app . ./
USER $APP_HOME

CMD exec gunicorn wsgi:server --bind :$PORT --log-level info --workers 1 --threads 8
