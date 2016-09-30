# This program converts the status files, that result from the pickling operation to MessagePack'ed tweets and then populate a Kafka Topic.

import json
import cPickle as pickle
import jsonpickle
import msgpack,sys
from kafka import KafkaProducer
from kafka import KafkaConsumer

filename1 = open('stutases_201661_0.p', 'rb') 
json_list = []  #create empty list that will be used to store JSON objects

#Add the 'unpickled' and JSON-converted tweets to json_list from hourly pickled files

while 1:   #remove for for-loop test
    try:
        status = (pickle.load(filename1))    #Read a line from the pickle file
        new_frozen = jsonpickle.encode(status, unpicklable = False)  #creates a JSON string from the 'status' variable
        json_list.append(json.loads(new_frozen))
   
    except EOFError:
        print "End of file reached."
        break
    
#Kafka Producer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

#Kafka Consumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',value_deserializer=msgpack.loads)

#Kafka Topic

consumer.subscribe(['GeoTweets'])

#MessagePack Tweets and send to Kafka

for i in range(len(json_list)):
    packed = msgpack.packb(json_list[i])
    producer.send('GeoTweets', packed)

#Check the tweets in Kafka Consumer

for msg in consumer:
        tweet = msg.value
        print (tweet["id"]) 
        
