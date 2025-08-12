# 🏭 Digital Twin Factory Monitoring System

This project simulates a smart factory with virtual machines that publish sensor data (temperature, vibration, throughput) via MQTT. The data is stored in InfluxDB and visualized using Grafana.

---

##  Stack Used

- **Python** (MQTT Simulator & Data Ingest)
- **Mosquitto** (MQTT Broker)
- **InfluxDB** (Time-series database)
- **Grafana** (Dashboards + Alerts)
- **Docker Compose** (Orchestration)

---

##  Features

- Real-time simulation of CNC, Press, and Packaging units
- MQTT topics: `factory/line1/<machine>`
- Storage in InfluxDB with proper schema (tags + fields)
- Grafana dashboards for:
  - Machine-wise monitoring
  - Parameter-wise tracking
  - Alerts via email
- Modular setup using Docker Compose

---

##  How to Run

```bash
docker-compose up
