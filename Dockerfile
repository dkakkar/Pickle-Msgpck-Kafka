FROM python:2.7.11

WORKDIR /usr/local/src/classifier

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# The user of this docker image is expected to attach a volume with this file at this path
RUN ln -s /var/classifier/svmClassifier.pkl .

# Do this last; most likely to change
COPY src/sentiment.py ./

CMD ["python3", "sentiment.py"]
