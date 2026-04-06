FROM python:3.12-slim

ARG WORKDIR
ENV WORKDIR=${WORKDIR}

RUN groupadd -r appuser && useradd -r -g appuser appuser

RUN mkdir -p $WORKDIR && chown -R appuser:appuser $WORKDIR

WORKDIR ${WORKDIR}

COPY . ${WORKDIR}

RUN pip install --no-cache-dir -r requirements.txt

USER appuser