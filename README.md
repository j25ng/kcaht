# kchat
- Python chat program using Apache Kafka

## TEST
### Producer
```bash
$ python producer.py
[DONE]: 0.04024648666381836
```
### Consumer
```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-s
{"str": "value0"}
{"str": "value1"}
{"str": "value2"}
{"str": "value3"}
{"str": "value4"}
{"str": "value5"}
{"str": "value6"}
{"str": "value7"}
{"str": "value8"}
{"str": "value9"}
```
