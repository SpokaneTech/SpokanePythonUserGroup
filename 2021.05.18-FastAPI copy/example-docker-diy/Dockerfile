FROM python:3.9

ADD ../requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", \
    "app:app", \
    "--reload", \
    "--reload-dir", "/app" ]
