FROM python:3.9-alpine3.15
LABEL maintainer="santhosht5290@gmail.com"

ENV PYTHONUNBIFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt 
COPY ./app /app
WORKDIR /app
EXPOSE 8000




ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # install postgresql-client client package insdie alpine to connect psycopg2 to postgres
    apk add --update --no-cache postgresql-client && \ 
    # sets virtual depen package which can be removed later
    apk add --update --no-cache --virtual .tmp-build-deps \
    # install packages for postgres
    build-base postgresql-dev musl-dev && \
    #install python requirements
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ] ; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt && \
    echo "$DEV, here" ;\
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

USER django-user

