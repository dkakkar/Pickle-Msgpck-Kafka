FROM python:2.7.11

WORKDIR /usr/local/src/pickle_msgpack_kafka

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# The user of this docker image is expected to attach a volume with this file at this path
RUN ln -s /var/classifier/status.p .

# Do this last; most likely to change
COPY src/pickle-msgpck-kafka.py ./

CMD ["python2", "pickle-msgpck-kafka.py"]
