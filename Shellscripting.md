## Shellscripting
A collection of the most used shellscripting tricks.

```bash
wc -l file.txt counts the number of lines
```

#### Delete old files of a folder
Useful when you want to free old data/logs.

#### Using alias 
I use them to quick connect my ssh servers
```bash
alias ssh-prod-dc-app1-server1='ssh user@server1'
```

#### Shellscript functions
```bash
#!/bin/bash
function_name(){
  param1=$1
  param2=$2
  echo $param1
  echo "this is param 2 $param1"
 }
 
 function_name hello world
```

#### Find a file in a folder
```bash
find ./ -name filename.txt
```

#### Run a command for ever very xx seconds
```bash
while true; do date; ps aux|grep ssh;sleep 5;done
```

## Forensic Analysis
uptime - Get server uptime.
last - Get who was login into the system.

#### The history log
You can cat the history log from cat ~/.bash_history


#### Analize trafic with TCP 

To dump everything from iface enp0s3
```bash
tcpdump -w dump.pcap -i enp0s3
```

To dump all comes and goes to an specific ip
```bash
tcpdump -w dump.pcap host 1.1.1.1
```

The following comand save dump files of 10 mb, and rotate it in 5 files, so we as much we will have 10mb x 5 files of dump.
```bash
tcpdump -W 5 -C 10 -w capfile
```




