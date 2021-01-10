## Shellscripting
A collection of the most used shellscripting tricks.

wc -l file.txt counts the number of lines

#### Delete old files of a folder
Useful when you want to free old data/logs.

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

## Forensic Analysis
uptime - Get server uptime.
last - Get who was login into the system.

#### The history log
You can cat the history log from cat ~/.bash_history
