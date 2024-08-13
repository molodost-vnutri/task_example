FROM python:3.12.4-alpine3.20

COPY . /source

WORKDIR /source

EXPOSE 8000

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir --upgrade poetry && \
    python -m poetry install

CMD [ "python", "-m", "poetry", "run", "uvicorn", "source.main:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]