FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get -qq update
RUN apt-get install --yes apache2 apache2-dev


WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install
#RUN pip install -r requirements.txt
COPY . /code/



