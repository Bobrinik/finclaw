FROM python:3.10-bullseye

RUN groupadd -g 1000 app && useradd -m -u 1000 -g app app

WORKDIR /app

COPY ./dist dist/
COPY ./tools/* tools/
RUN pip install dist/*.tar.gz

USER app
