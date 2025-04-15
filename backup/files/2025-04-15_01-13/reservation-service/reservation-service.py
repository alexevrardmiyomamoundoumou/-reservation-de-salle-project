from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_reservation_event(user, room, time):
    event = {"user": user, "room": room, "time": time}
    producer.send('reservation_topic', event)
