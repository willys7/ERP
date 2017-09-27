FROM python:2.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD ERP/requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 RUN python ERP/manage.py migrate
 RUN python ERP/manage.py runserver 0.0.0.0:8008
 