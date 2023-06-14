FROM python:3.11

WORKDIR app/

COPY ./pyproject.toml /app/pyproject.toml

RUN pip install -e .

COPY ./src /app/src

CMD ["uwsgi", "--http", "0.0.0.0:5000", "--master", "-p", "1", "-w", "src.hello.main:app"]