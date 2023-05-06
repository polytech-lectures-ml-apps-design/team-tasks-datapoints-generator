from kafka import KafkaConsumer


consumer = KafkaConsumer('raw_data', bootstrap_servers='localhost:29092')

for msg in consumer:
    print(msg)
