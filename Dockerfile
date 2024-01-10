FROM python:3.11

LABEL authors="Anton Zhilinskey"

RUN mkdir /django_blog

WORKDIR /django_blog

COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip

RUN pip install pipenv && pipenv install --dev --system --deploy

COPY . .

RUN chmod a+x docker/*.sh