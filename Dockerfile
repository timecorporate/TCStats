FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/
EXPOSE 8000
#RUN python manage.py collectstatic
CMD exec gunicorn tcstats_api.wsgi --bind 0.0.0.0:8000 --workers 3