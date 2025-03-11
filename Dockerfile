FROM python:3.12.7

WORKDIR /app
COPY pyproject.toml pdm.lock* /app/

RUN pip install pdm

RUN pdm install  --prod

EXPOSE 8000

COPY . /app

CMD ["pdm", "run", "start"]
