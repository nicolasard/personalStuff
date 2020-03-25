### Installing Grafana

What's Grafana? Grafana it's a monitoring tool, it have alarms included (We don't use te alarm feature in my current work). An other cool tool like grana it's Chronograf (https://docs.influxdata.com/chronograf/v1.7/)
Ass you know I love install standalone applications, so this will be my guid about how to install Grafana in a standalone.

*Environment:* Virtualiced Debian Linux

Take in consideration that this guide as you see in the following chart have many components.

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


### Parsing text log data to influxDB.
We can push also push some of our applications data to the influxDB server. This can be made thanks to the **filebeat** and **logstash** applications

#### About Filebeat
Filebeat it's the application that reads the logs from and send them to Logstash.

❓ TODO: Check why filebeat won't process twice the same file, maybe it's hashing it. Where? 

#### About Logstash
Logstash have the concept of *"Pipelines"*. A pipeline has a input, it could have a filter, and it have an output.



The most common filter that you can use in Logstash it's called Grok https://www.elastic.co/guide/en/logstash/7.6/plugins-filters-grok.html

