# Developing and Deploying an xApp for Anomaly Detection 

## Overview

This project demonstrates the deployment of a fully operational 5G network using **OpenAirInterface (OAI)** and **Kubernetes**. The network functions are containerized and orchestrated within a Kubernetes-based microservices environment, ensuring flexibility, scalability, and real-time performance monitoring.

The primary objective is to leverage the **Key Performance Measurement (KPM)** service model within **FlexRIC** to collect real-time metrics from the **Radio Access Network (RAN)**. An xApp was developed to integrate an **SVM model** to detect and classify anomalies in the network, enabling proactive network management and optimization.

---

## Tools & Technologies

- **Kubernetes**: For container orchestration and management.
- **OpenAirInterface5G (OAI)**: To set up the 5G Core Network and Radio Access Network.
- **FlexRIC**: Cloud-based RAN Intelligent Controller for real-time metric collection and management.
- **C**: For xApp development
- **Python**: For machine learning model implementation.
- **Docker**: For containerizing the xApp and other network components.

