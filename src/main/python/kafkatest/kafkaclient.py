'''
Created on 6 Jul 2017

@author: aadebuger
'''
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:1234')
producer.send('Topic2', b'some_message_bytes')
if __name__ == '__main__':
    pass