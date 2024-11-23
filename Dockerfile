FROM python:3.12.7

WORKDIR /app
COPY pyproject.toml pdm.lock* /app/

RUN pip install pdm

RUN pdm install

COPY . /app

CMD ["pdm", "run", "start"]