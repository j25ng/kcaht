from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        "topic1",
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=15000,
        auto_offset_reset='latest', # 'earliest', 'latest'
        group_id="fbi",
        enable_auto_commit=True,
)

print('[Start] get consumer')

for m in consumer:
    #print(m)
    print(f"topic={m.topic}, partition={m.partition}, offset={m.offset}, value={type(m.value)}, timestamp={m.timestamp}")

print('[End] get consumer')
