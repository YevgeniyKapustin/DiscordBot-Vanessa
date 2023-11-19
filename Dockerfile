FROM python:3.12.0

WORKDIR /bot/

RUN pip install 'poetry==1.6.1'
COPY poetry.lock pyproject.toml /bot/

RUN poetry config virtualenvs.create false &&  \
    poetry install --no-interaction --no-ansi --no-dev

COPY . .

CMD python main.py
