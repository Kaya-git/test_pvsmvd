FROM python:3.11-slim

RUN mkdir /app

COPY /requirements.txt .

RUN pip install --upgrade pip \
  && pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /src

CMD [ "python", "main.py" ]
