FROM python:3.6
MAINTAINER lawzeeml@buffalo.edu

COPY ./cse312 /cse312

WORKDIR /cse312

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
