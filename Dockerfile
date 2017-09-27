FROM python:2.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD ERP /code/
 RUN pip install -r ERP/requirements.txt
 RUN python ERP/Authentication/auth_rcp_service.py
 RUN python ERP/Inventory/validate_queue.py
 RUN python ERP/PointOfSale/recive_sales_queue.py
 RUN python ERP/manage.py migrate
 RUN python ERP/manage.py runserver 0.0.0.0:8008
 ADD . /code/
