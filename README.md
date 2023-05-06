# Data points generator for Kafka

Sample generator of data points (tag, timestamp, value) publishing to Kafka topic.

:zap: This generator is to test message structure and connectivity. 
It's not producing anything meaningful in terms of timeseries data, just random values! :zap: 

## App structure

 - sample producer (defined in `producer.py`)
 - sample consumer (defined in `consumer.py`)
 - Kafka message broker (in Docker containers)
 - docker compose to bring up Kafka and producer together

## Message format

Messages are individual datapoints as follows: 
```python
@dataclass
class DataPoint:
    tag_id: str
    timestamp: int
    value: float
```

## How to use

Build producer docker image with
```shell
docker build -t kafka_producer -f ./producer.Dockerfile .
```
Bring up the application with Docker Compose:
```shell
docker compose up -d
```
This will start publishing messages to Kafka (exposed on port 29092) in the topic **raw_data**,
which can be consumed like this:
```python
consumer = KafkaConsumer('raw_data', bootstrap_servers='localhost:29092')
```
the serialization format being 
```python
value_serializer=lambda x: json.dumps(asdict(x)).encode('utf-8')
```
A sample consumer is provided in `consumer.py`.

## Improvements

Avro serialization could be used instead of plain text UTF-8.
This would result in compact messages and less traffic.
Avro scheme is already available in `datapoint.avsc`.