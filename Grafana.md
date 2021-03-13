### Installing Grafana

What's Grafana? Grafana it's a monitoring tool, it have alarms included (We don't use te alarm feature in my current work). An other cool tool like grana it's Chronograf (https://docs.influxdata.com/chronograf/v1.7/)
Ass you know I love install standalone applications, so this will be my guid about how to install Grafana in a standalone.

*Environment:* Virtualiced Debian Linux

Take in consideration that this guide as you see in the following chart have many components.

![Schema of grafana components](https://github.com/nicolasard/personalStuff/blob/master/GrafanaArquitecture.png)

### The complete overview to monitor a server
Grana needs a "Data Source" that it's used to show the data from. One good datasource will be InfluxDB, a time series database. If you want to monitor the Ram memmory in different servers for example, this DB should be populated with a "Time series collector" like Telegraph.

##### Creating measurements
If you use telegraf, telegraf will create that for you. But is good to know how to create your own manually because this is going to help you when you start work with Kapacitor to create some dummy data to generate alerts.



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

### Parsing text log data to influxDB.
We can push also push some of our applications data to the influxDB server. This can be made thanks to the **filebeat** and **logstash** applications

#### About Filebeat
Filebeat it's the application that reads the logs from and send them to Logstash.

❓ TODO: Check why filebeat won't process twice the same file, maybe it's hashing it. Where? 

#### About Logstash
Logstash have the concept of *"Pipelines"*. A pipeline has a input, it could have a filter, and it have an output.



The most common filter that you can use in Logstash it's called Grok https://www.elastic.co/guide/en/logstash/7.6/plugins-filters-grok.html

#### Grafana
Grafana is pretty intuitive to create dashboards, and one pretty feature is that you can create the dashboards, export them as json and load them when programatically. Also you can configure the datasources (https://grafana.com/docs/grafana/latest/administration/provisioning/) 

