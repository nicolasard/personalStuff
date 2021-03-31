# About InfluxDB

### Introduction
Download the linux binary from InfluxData https://portal.influxdata.com/downloads/ (Influx Data it's the company behind Influx)

Influx DB it's like a SQL database for time series. 

>Conceptually you can think of a measurement as an SQL table, where the primary index is always time. tags and fields are effectively >columns in the table. tags are indexed, and fields are not. The difference is that, with InfluxDB, you can have millions of >measurements, you don’t have to define schemas up-front, and null values aren’t stored.
>
><cite> From getting started guide https://docs.influxdata.com/influxdb/v1.7/introduction/getting-started/</cite>

### Installation

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

You can also install it in your system using some package manager. For example in my sandbox servers I have the following Salt formula to do that.
```bash
{# install_influxdb.sls #}

{#  With this we are safe that this state will be applied just to the servers that will be used for influxdb #}

{% if 'influxdb' in grains['server_role']  %}

influxdb-repository:
  pkgrepo.managed:
    - humanname: Telegraf Repository
    - name: deb https://repos.influxdata.com/debian {{ salt['grains.get']('oscodename') }} stable
    - dist: {{ salt['grains.get']('oscodename') }}
    - file: /etc/apt/sources.list.d/telegraf.list
    - gpgcheck: 1
    - key_url: https://repos.influxdata.com/influxdb.key

install-influxdb:
  pkg.installed:
    - pkgs:
      - influxdb2

{% endif %}
```

### Using the influx client

You can use the influx client at the server where you have influxdb runing with just the following command.

```bash
root@ln-moni01:/home/nardison# influx
Connected to http://localhost:8086 version 1.8.3
InfluxDB shell version: 1.8.3
```

#### Show and use database (Like in SQL)

```bash
> show databases;
name: databases
name
----
_internal
telegraf
> use telegraf;
Using database telegraf
```

Create a database (Similar as in SQL)

```bash
> create database dummydata;
> show databases;
name: databases
name
----
_internal
telegraf
dummydata
```

#### Show measurements (In influxdb we don't have tables, we have measurements)
```bash
> show measurements;
name: measurements
name
----
apc_mainvoltage
cpu
disk
diskio
ethtool
http_response
http_response_ipg-prod5-api
http_responsehttp_response_ipg-prod5-api
kernel
mem
mysql
net
net_response
ping
processes
sensors
swap
system
test
```

Also if you want to delete a measurment
```bash

```

#### Retention policies

Retention policies indicates how long we should retain the data in the database, after that time influxdb will delete it.

```bash
> show retention policies;
name    duration shardGroupDuration replicaN default
----    -------- ------------------ -------- -------
autogen 0s       168h0m0s           1        true
```

You can have multiple retention policies, by database, by measurement.

If you want to change the retention policies you can run `alter retention policy <retention-name> on <database-name> duration <new-duration>;`

```bash
> alter retention policy autogen on telegraf duration 182d;
> show retention policies;
name    duration  shardGroupDuration replicaN default
----    --------  ------------------ -------- -------
autogen 4368h0m0s 168h0m0s           1        true
```

#### Line Protocol (aka how to insert values in influxdb and create measurements)

https://docs.influxdata.com/influxdb/v1.8/write_protocols/line_protocol_tutorial/

```bash
curl -i -XPOST "http://localhost:8086/write?db=science_is_cool" --data-binary 'weather,location=us-midwest temperature=82 1465839830100400200'
```

Taking advantaje that you can just doing a simple curl post to insert values, you can run an escript as the following to insert dummy data.

```python
# populate.py
# Minimal example of how to insert data to influxdb

import urllib2
import time
import random

def writedummytemp(temp):
    url = 'http://localhost:8086/write?db=dummydata'
    data= 'weather,location=us-midwest temperature='+str(temp)
    cont_len = len(data)
    req = urllib2.Request(url, data, {'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': cont_len})
    f = urllib2.urlopen(req)
    response = f.read()
    f.close()

while True:
    temp=20+random.randrange(10)
    writedummytemp(temp)
    time.sleep(5)
```

### Data sampling 
At https://docs.influxdata.com/kapacitor/v1.5/working/cli_client/#data-sampling we have a good documentation about datas-sampling, this will be useful to get a sample of data to test later an task.
