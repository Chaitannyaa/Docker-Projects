FROM python:3.9

WORKDIR /app/backend

COPY . /app/backend

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python /app/backend/manage.py runserver 0.0.0.0:8000
