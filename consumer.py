import json

from kafka import KafkaConsumer

if __name__ == '__main__':
    
    consumer = KafkaConsumer(
            topic = 'org.sf.crime.calls',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=False,
            group_id='calls-group',
            value_deserializer = lambda call: json.loads(call.decode('utf-8')))

    for call in consumer:
        if call:
            print(call.value)
