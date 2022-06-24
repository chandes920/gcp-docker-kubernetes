FROM python:3.9-alpine

WORKDIR .

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "login.py", "--host=0.0.0.0", "--port=5000"]
