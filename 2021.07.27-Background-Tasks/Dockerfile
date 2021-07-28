FROM python:3.9 as base
ENV PYTHONPATH="${PYTHONPATH}:/demo"
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

FROM base as celery
ENTRYPOINT [ "celery" ]
CMD [ "-A", "celery_demo", "worker", "--loglevel=INFO" ]

FROM base as dramatiq
ENTRYPOINT [ "dramatiq" ]
CMD [ "--verbose", "dramatiq_demo" ]
