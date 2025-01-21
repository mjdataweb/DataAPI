FROM python:3.9

WORKDIR /DataAPI

COPY . /DataAPI

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python3", "app.py"]