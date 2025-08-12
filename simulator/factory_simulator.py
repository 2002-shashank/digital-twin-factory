import time
import json
import random
import paho.mqtt.client as mqtt

# MQTT Settings
BROKER = "localhost"
PORT = 1883
TOPIC_PREFIX = "factory/line1/"

# Simulated factory machines
MACHINES = [
    {"id": "cnc_machine", "type": "CNC"},
    {"id": "press_machine", "type": "Press"},
    {"id": "packaging_unit", "type": "Packaging"}
]

def simulate_status():
    return random.choice(["RUNNING", "IDLE", "FAULT"])

def simulate_metrics():
    return {
        "temperature": round(random.uniform(30, 80), 2),
        "throughput": random.randint(10, 50),
        "vibration": round(random.uniform(0.1, 1.5), 2)
    }

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("🔁 Publishing simulated machine data...")
while True:
    for machine in MACHINES:
        payload = {
            "machine_id": machine["id"],
            "type": machine["type"],
            "status": simulate_status(),
            "metrics": simulate_metrics(),
            "timestamp": time.time()
        }
        topic = f"{TOPIC_PREFIX}{machine['id']}"
        client.publish(topic, json.dumps(payload))
        print(f"📤 Published to {topic}: {payload}")
    time.sleep(2)
