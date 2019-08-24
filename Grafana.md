### Installing Grafana

What's Grafana? Grafana it's a monitoring tool, it have alarms included (We don't use te alarm feature in my current work). An other cool tool like grana it's Chronograf (https://docs.influxdata.com/chronograf/v1.7/)
Ass you know I love install standalone applications, so this will be my guid about how to install Grafana in a standalone.

*Environment:* Virtualiced Debian Linux

1. Download Grafana binaries from https://grafana.com/grafana/download

2. 

![Schema of grafana components](https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=GrafanaArquitecture.drawio#R7VlNb6MwEP01OW6FAZfkuE26H%2BpWqpSV2p5WFkzArYORMQ3pr18TTPhwktJsWnLYU5mHbfB7b8ZDOnKmy%2Fy7IEl0ywNgI9sK8pEzG9k2spyx%2BlMg6xLB2CqBUNBAD6qBOX2FaqZGMxpA2hooOWeSJm3Q53EMvmxhRAi%2Bag9bcNZ%2BakJCMIC5T5iJ3tNARiU6rnZR4D%2BAhlH1ZGTpO0tSDdZAGpGArxqQcz1ypoJzWV4t8ymwgryKl3Letz13ty8mIJZ9JuT8ZrzgD2iJrT%2Fx%2FevkiVL5xdXvJtfVhiFQ%2B9chFzLiIY8Ju67RK8GzOIBiVUtF9ZhfnCcKRAp8AinXWkySSa6gSC6Zvgs5lQ%2BN68diqQuso1muV94E6yqIpVg%2FNIPGrCKsp22ial65v2JTe2nTUMoz4cMBrir7ERGCPDDO2YqrsgL4EtT7qHkCGJH0pf0eRNsz3I6rFVQXWsR3CKrXfSEs00%2F6GS9Yls%2BuDKVrHQshVhGVME%2FIhoKVSua2ZnpZEBLyw0yaO9cT7LHOBF0K7CpVVnVioSpbokZSOdYHkeUYZKkqtiAxGZwrjM6Nq8v%2FlaJ3pcA9K8UeD3xOpcCG%2BX8Dg1AlwPDuPzfzI3SAk0G8fYEuO%2FZ%2By9%2Bb6A4EVZSA0GAqBX%2BGKWe8QGIew2kzweuZCZNBz0znYG3TrAwtuI3bgttHCT6AtsgaVFw8oLh2b3XdtrjoGG0DkkbbKj2E0O6QQnvGeXZD1CFFpSptQx9o3dbXQUOfaGODLTNN4uBr8QWtIp%2BRNKX%2BbsvXNeyxcedNx7fL2fl9xnm7FW0ohncIVmG9Pa%2BfcMep2si%2BDshFHR%2BUu9STmh%2F9nXW2P0dUxrvsLFTSYCy08dR218fbbGLYbM6I%2F2x6jTGapEUlTiOSwMZyPAs%2Bp9t0Ou2mZ19gMz3RDrU9%2FFGnlmUQd0soOyve3EnHW9gbnjf7dHXtyD7N8tpHuftGaTuXNm1PCz5IvcPWieqdiz%2B33iHX8B9I%2F3Rpu6PF%2B6ccdrwOX30%2Ftcfvb0xUWP%2FaXRJe%2F8%2FAuf4L)

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

#### About Telegraph

Telegraph it's like a 

```bash
# 1.) Download the Binary.
wget wget https://dl.influxdata.com/telegraf/releases/telegraf-1.11.1_linux_amd64.tar.gz
# 2.) Uncompress it.
tar -zxvf influxdb-1.7.7_linux_amd64.tar.gz
# 3.) Configure it

# 4.) Tun Telegraph
/usr/bin/telegraph
```
#### About Kapacitor
"Kapacitor is an open source data processing framework that makes it easy to create alerts, run ETL jobs and detect anomalies. Kapacitor is the final piece of the TICK stack." from https://docs.influxdata.com/kapacitor/v1.5/


