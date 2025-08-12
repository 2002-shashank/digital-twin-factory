import json
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB connection details (matching your Docker setup)
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "Mre8etfVrp1XHhLH2WsG7m80QF6I7C2syJYi27QG7meUvOBY0VouYhbD-3gWxHvsZH9Adtz1oK48J4wBWiCRTA=="
INFLUX_ORG = "factory-org"
INFLUX_BUCKET = "factory-bucket"

# InfluxDB client setup
influx_client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("✅ Connected to MQTT broker")
    client.subscribe("factory/line1/#")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📥 Topic: {msg.topic}")
        print(f"Payload: {payload}")

        point = Point("machine_data") \
            .tag("machine_id", payload["machine_id"]) \
            .tag("type", payload["type"]) \
            .tag("status", payload["status"]) \
            .field("temperature", float(payload["metrics"]["temperature"])) \
            .field("throughput", int(payload["metrics"]["throughput"])) \
            .field("vibration", float(payload["metrics"]["vibration"])) \
            .time(int(payload["timestamp"] * 1e9))  # nanoseconds

        write_api.write(bucket=INFLUX_BUCKET, record=point)
        print("✅ Written to InfluxDB\n" + "-"*40)

    except Exception as e:
        print("❌ Error:", e)

# MQTT client setup
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883, 60)
mqtt_client.loop_forever()
