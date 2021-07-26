FROM python:3.9

EXPOSE 8000

ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT [ "uvicorn" ]
CMD [ "app:app" \
    "--host", "0.0.0.0", \
    "--port", "8000", \
    "--reload", \
    "--reload-dir", "/app" ]
