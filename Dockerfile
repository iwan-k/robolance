FROM python:3.11

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install poetry==1.7.1

RUN poetry install

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]


