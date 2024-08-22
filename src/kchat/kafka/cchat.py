from kafka import  KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer(
        'chat',
        bootstrap_servers=['ec2-13-125-40-163.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='chat-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중 ...")

try:
    for m in consumer:
        data = m.value
        print(f"[FRIEND] {data['message']}, {time.ctime(data['time'])}")
except KeyboardInterrupt:
    print("채팅 종료")
finally:
    consumer.close()
