# 🏭 Digital Twin for Smart Factory — Real-Time Monitoring & Alerts

A full-stack simulation of a smart manufacturing factory built entirely with open-source tools and containerized using Docker. This project simulates industrial machines, streams real-time sensor data over MQTT, stores it in InfluxDB, visualizes it in Grafana, and sends email alerts for abnormal conditions — all without requiring any physical hardware.

---

## 🚀 Project Highlights

-  **Factory Simulator (Python):** Generates real-time data for CNC, Press, and Packaging units.
-  **MQTT Broker (Mosquitto):** Transfers data using the publish-subscribe model.
-  **InfluxDB:** Time-series database to store sensor metrics with nanosecond precision.
-  **Grafana:** Rich dashboards to visualize temperature, vibration, and throughput.
-  **Alert System:** Configured threshold-based alerts with optional email integration.
-  **Dockerized Setup:** Clean, portable, and scalable container-based architecture.

---

##  Tech Stack

| Component     | Tool/Tech             |
|---------------|------------------------|
| Language      | Python 3               |
| Messaging     | MQTT (Mosquitto)       |
| Database      | InfluxDB 2.x           |
| Visualization | Grafana                |
| Containers    | Docker + Docker Compose|
| Dashboard     | Grafana Dashboards     |
| Alerting      | Email Notifications    |

---


---

##  Modules in This Project

1. **factory_simulator.py**
   - Simulates machines: CNC, Press, Packaging
   - Publishes data to topics like: `factory/line1/cnc_machine`

2. **mqtt_to_influx.py**
   - Subscribes to MQTT topics
   - Parses JSON payload
   - Writes data to InfluxDB with appropriate tags and fields

3. **Dockerized Services**
   - Mosquitto MQTT Broker
   - InfluxDB 2.7
   - Grafana (latest)

4. **Grafana Dashboards**
   - Real-time monitoring of each machine
   - Threshold-based color-coded metrics
   - Machine-specific panels with detailed graphs

5. **Email Alerting**
   - SMTP configured in `grafana.ini`
   - Alerts for over-temperature, high vibration, etc.
   - Integrated notification channel (e.g., Gmail)

---

##  Screenshots

| Panel | Screenshot |
|-------|------------|
| CNC Dashboard | ![CNC](assets/cnc-panel.png) |
| Press Panel   | ![Press](assets/press-panel.png) |
| Packaging Panel | ![Packaging](assets/packaging-panel.png) |
| Email Alert | ![Alert](assets/email-alert.png) |



---

##  Setup & Deployment (Docker)

```bash
git clone https://github.com/2002-shashank/digital-twin-factory.git
cd digital-twin-factory
docker-compose up

In separte Terminals:
cd simulator
python3 factory_simulator.py
python3 mqtt_to_influx.py



