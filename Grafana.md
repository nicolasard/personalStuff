### Installing Grafana

Ass you know I love install standalone applications, so this will be my guid about how to install Grafana in a standalone.

*Environment:* Virtualiced Debian Linux

1. Download Grafana binaries from https://grafana.com/grafana/download

2. 


### The complete overview to monitor a server
Grana needs a "Data Source" that it's used to show the data from. One good datasource will be InfluxDB, a time series database. If you want to monitor the Ram memmory in different servers for example, this DB should be populated with a "Time series collector" like Telegraph.





#### To install InfluxDB
Download the linux binary from InfluxData https://portal.influxdata.com/downloads/ (Influx Data it's the company behind Influx)

```bash
# 1.) Download the Binary.
wget https://dl.influxdata.com/influxdb/releases/influxdb-1.7.7_linux_amd64.tar.gz
# 2.) Uncompress it.
tar -zxvf influxdb-1.7.7_linux_amd64.tar.gz
# 3.) Check the configuration.

# Run Influx DB
/var/bin/influxd
```
