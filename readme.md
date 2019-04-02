### Some Sub Pages
 1. [ReactJs](https://github.com/nicolasard/personalStuff/blob/master/reactJs.md)
 2. [Grafana](https://github.com/nicolasard/personalStuff/blob/master/Grafana.md)
 3. [Salt](https://github.com/nicolasard/personalStuff/blob/master/Salt.md)
 4. [Kubernates](https://github.com/nicolasard/personalStuff/blob/master/Kubernates.md) 

### Personal stuff
This pretend to be a personal guide about how to setup a new development environment. I think that for this things it's cool to don't use autoinstallers.

**Profile of the developer:** A guy running windows 7/10, who wants to deploy in Java for backend using Maven or Gradle. And for frontend wants to use Node with NPM.

Don't use installers if you can. (This it's going to help you if you don't have admin/root privileges in your computer. )

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

#### Making a Debian Linux init.d service script
I used this fabolous [this](https://debian-administration.org/article/28/Making_scripts_run_at_boot_time_with_Debian) fabolous guid from Debian.
Let's say that we have a 
