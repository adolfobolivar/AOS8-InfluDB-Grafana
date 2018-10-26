# Aruba MM/MC AOS 8.3 - InfluxDB - Grafana

Python Code Demo to create a wifi dashboard in GRAFANA from ARUBA Mobility Master and Mobility controller infrastructure.

# Infrastructure

The infraestruture needed is:

- Aruba Infrastructure: Mobility Master, Mobility Controller, Clearpass
- InfluxDB
- Grafana

<img align="left" src="https://github.com/adolfobolivar/AOS8-InfluDB-Grafana/blob/master/Physical%20Diagram.png">

# Logical Design

<img align="left" src="https://github.com/adolfobolivar/AOS8-InfluDB-Grafana/blob/master/Logical%20Diagram.png">

# InfluxDB 

Python script creates the database "example" and stores the data in multiple measurements:  

```
ubuntu@ubuntu:~$ influx
Connected to http://localhost:8086 version 1.6.3
InfluxDB shell version: 1.6.3
> use example
Using database example
> show measurements
name: measurements
name
----
Bandwidth_Consumed_CRCs
Number_Associations_APs
Number_Clients_SSID
Status_of_APs
cpuload
type_users
> 

```
# Dashboard generated in Grafana

I installed the Clock Panel and Gauge Panel Plugin for Grafana. Here is an example of the dashboard generated:

<img align="left" src="https://github.com/adolfobolivar/AOS8-InfluDB-Grafana/blob/master/Dashboard.png">

