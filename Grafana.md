### Installing Grafana

What's Grafana? Grafana it's a monitoring tool, it have alarms included (We don't use te alarm feature in my current work). An other cool tool like grana it's Chronograf (https://docs.influxdata.com/chronograf/v1.7/)
Ass you know I love install standalone applications, so this will be my guid about how to install Grafana in a standalone.

*Environment:* Virtualiced Debian Linux

1. Download Grafana binaries from https://grafana.com/grafana/download

2. 

![Schema of grafana components](https://github.com/nicolasard/personalStuff/blob/master/GrafanaArquitecture.png)

### The complete overview to monitor a server
Grana needs a "Data Source" that it's used to show the data from. One good datasource will be InfluxDB, a time series database. If you want to monitor the Ram memmory in different servers for example, this DB should be populated with a "Time series collector" like Telegraph.



#### About InfluxDB
Download the linux binary from InfluxData https://portal.influxdata.com/downloads/ (Influx Data it's the company behind Influx)

Influx DB it's like a SQL database for time series. 

>Conceptually you can think of a measurement as an SQL table, where the primary index is always time. tags and fields are effectively >columns in the table. tags are indexed, and fields are not. The difference is that, with InfluxDB, you can have millions of >measurements, you don’t have to define schemas up-front, and null values aren’t stored.
>
><cite> From getting started guide https://docs.influxdata.com/influxdb/v1.7/introduction/getting-started/</cite>

```bash
# 1.) Download the Binary.
wget https://dl.influxdata.com/influxdb/releases/influxdb-1.7.7_linux_amd64.tar.gz
# 2.) Uncompress it.
tar -zxvf influxdb-1.7.7_linux_amd64.tar.gz
# 3.) Check the configuration.
### TODO
# 4.) Run Influx DB
/var/bin/influxd
```

#### About Telegraf

Telegraf it's like a 

```bash
# 1.) Download the Binary.
wget wget https://dl.influxdata.com/telegraf/releases/telegraf-1.11.1_linux_amd64.tar.gz
# 2.) Uncompress it.
tar -zxvf influxdb-1.7.7_linux_amd64.tar.gz
# 3.) Configure it
Telefraf takes the config from a file in 
  $TELEGRAF_CONFIG_PATH, /home/faloggs/.telegraf/telegraf.conf, or /etc/telegraf/telegraf.conf
  
# 4.) Run Telegraf
/usr/bin/telegraf
```
#### About Kapacitor
"Kapacitor is an open source data processing framework that makes it easy to create alerts, run ETL jobs and detect anomalies. Kapacitor is the final piece of the TICK stack." from https://docs.influxdata.com/kapacitor/v1.5/

https://docs.influxdata.com/kapacitor/v1.5/introduction/getting-started/


