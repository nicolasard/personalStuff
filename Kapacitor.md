# Kapacitor

"Kapacitor is an open source data processing framework that makes it easy to create alerts, run ETL jobs and detect anomalies. Kapacitor is the final piece of the TICK stack." from https://docs.influxdata.com/kapacitor/v1.5/ also a good introduction can be found here https://youtu.be/lfNcYG0bMhU 

https://docs.influxdata.com/kapacitor/v1.5/introduction/getting-started/

Also it's interesting to checkout the repository https://github.com/influxdata/kapacitor

Kapacitor have many integrations, SMTP (mailing), slack, telegram, pagerduty, etc. At my sandbox servers I'm using SMTP and the free acount of pagerduty that allows you up to 5 users oncall.

Creating your tick script, the tick script is where you write the logic of your alert or ETL. It's composed of "Nodes" (https://docs.influxdata.com/kapacitor/v1.5/nodes/) that are joined via pipes (|). The first node is always batch or stream.

To load a alert from a tick file
```
 kapacitor define http-alert -tick http-alert.tick
```

To see the alerts you have defined in kapacitor
```
root@ln-moni01:/home/nardison# kapacitor list tasks
ID         Type      Status    Executing Databases and Retention Policies
http-alert batch     enabled   true      ["telegraf"."autogen"]
sf_task    batch     disabled  false     ["telegraf"."autogen"]
```

To see how the 

```
root@ln-moni01:/home/nardison# kapacitor show  http-alert
ID: http-alert
Error:
Template:
Type: batch
Status: enabled
Executing: true
Created: 25 Oct 20 17:01 -03
Modified: 12 Dec 20 20:08 -03
LastEnabled: 12 Dec 20 20:08 -03
Databases Retention Policies: ["telegraf"."autogen"]
TICKscript:
dbrp "telegraf"."autogen"

// HTTP egallo.com.ar alerts
var data = batch
    |query('''
        select mean(result_code) from "telegraf"."autogen"."http_response"
      ''')
        .groupBy('host')
        .period(10s)
        .every(10s)

data
    |alert()
        .info(lambda: "mean" > 0)
        .message('El sitio www.egallo.com.ar aparenta estar caido')
        .log('/tmp/alert')

data
    |alert()
        .warn(lambda: "mean" > 0)
        .message('El sitio www.egallo.com.ar aparenta estar caido')
        .log('/tmp/alert2')

DOT:
digraph http-alert {
graph [throughput="0.00 batches/s"];

query1 [avg_exec_time_ns="0s" batches_queried="1" errors="0" points_queried="1" working_cardinality="0" ];
query1 -> alert3 [processed="1"];
query1 -> alert2 [processed="1"];

alert3 [alerts_inhibited="0" alerts_triggered="0" avg_exec_time_ns="0s" crits_triggered="0" errors="0" infos_triggered="0" oks_triggered="0" warns_triggered="0" working_cardinality="1" ];

alert2 [alerts_inhibited="0" alerts_triggered="0" avg_exec_time_ns="0s" crits_triggered="0" errors="0" infos_triggered="0" oks_triggered="0" warns_triggered="0" working_cardinality="1" ];
}
```
