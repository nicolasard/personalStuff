## :triangular_flag_on_post: Personal Stuff Pages 

### Some sub-pages/guides
I started to document in some MarkDown pages my knowledge so it can go fast to what I learned before:

 1. [ReactJs](https://github.com/nicolasard/personalStuff/blob/master/reactJs.md)
 2. [Grafana](https://github.com/nicolasard/personalStuff/blob/master/Grafana.md)
 3. [Salt](https://github.com/nicolasard/personalStuff/blob/master/Salt.md)
 4. [Kubernates](https://github.com/nicolasard/personalStuff/blob/master/Kubernates.md) 
 5. [Apache2](https://github.com/nicolasard/personalStuff/blob/master/apache2.md) 
 6. [GIT](https://github.com/nicolasard/personalStuff/blob/master/git.md) 
 7. [VirtualBox](https://github.com/nicolasard/personalStuff/blob/master/virtualbox.md) 
 8. [Jenkins](https://github.com/nicolasard/personalStuff/blob/master/jenkins.md) 
 9. [SonarQube](https://github.com/nicolasard/personalStuff/blob/master/sonarqube.md) 
 10. [Debian LVM and RAID](https://github.com/nicolasard/personalStuff/blob/master/DebianHDD.md) 

### Initial guide for developers
This pretends to be a personal guide about how to set up a new development environment. I think that for these things it's cool to don't use auto-installers.

**Profile of the developer:** A guy running windows 7/10, who wants to deploy in Java for backend using Maven or Gradle. And for frontend wants to use Node with NPM.

Don't use installers if you can. (This it's going to help you if you don't have admin/root privileges on your computer. )

#### Brief of the software i use:
| Application/Tool | Description |
| --- | --- |
| Java JDK | Lastly i'm developing in java 1.8 but this guide could apply to whatever version. |
| Maven    | Package manager for java                                                          |
| Gradle   | A new package manager for java                                                    |
| MobaXTerm | A very good tool for windows local console, and ssh client |


### Download the tools and setup the environment.
I use to download all the software in **C:\E\tools\** but you can download the binaries wherever you want.

##### The setenv.bat script
This script to set a the environment.

```bash
@ECHO OFF
echo SETTING UP ENVIRONMENT VARIABLES

SET JAVA_HOME=E:\tools\java\jdk1.7.0_67
SET JRE_HOME=E:\tools\java\jdk1.7.0_67

SET PATH=%MAVEN_HOME%\bin;%ANT_HOME%\bin;%JAVA_HOME%\bin;%CATALINA_HOME%;%CATALINA_BASE%;%PATH%

```


#### Additional: Linux env

This setEnv.sh script  
```bash
JDK_HOME=/path/to/jre/jre6

export PATH=$JDK_HOME/bin:$PATH
```

### Puting some service/application in production
#### Making a Debian Linux init.d service script
I used this fabolous [this](https://debian-administration.org/article/28/Making_scripts_run_at_boot_time_with_Debian) fabulous guide from Debian. In my example I'm putting the jenkins stand alone war to run at server startup.

:exclamation: IMPORTANT ACLARATION: If we don't put the BEGIN/END INIT INFO the command update-rc.d will not update the symbolic link to our /etc/init.d/jenkins file, and also will don't trigger any error (I hate for some seconds the developers of the command :yum: )

```bash
#!/bin/sh
### BEGIN INIT INFO
# Provides:  Jenkins
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts Jenkins
# Description:       starts Jenkins using start-stop-daemon
### END INIT INFO

# Jenkins init.d start script

SERVICE_NAME=Jenkins
JDK_HOME=/home/nardison/base/jdk1.8.0_144

export PATH=$JDK_HOME/bin:$PATH

case "$1" in
start)
                log_daemon_msg "Starting Jenkins"
                nohup java -jar /home/nardison/base/jenkins.war &> /home/nardison/base/jenkins.log
        ;;
stop)
                log_daemon_msg "Stoping Jenkins"
        ;;
esac

exit 0
```

