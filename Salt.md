
## Salt
Salt it's a server-client application that allow sys admin run commands in multiple servers at once, and create custom scripts to run commands in the servers.
So for example if you have to install an apache in your new server. First install the Salt client (aka minion) and then from master run the script you had already made to install an apache server automatically. 

### Installing Salt Master (aka server side)
In debian just apt-get install salt-master https://docs.saltstack.com/en/latest/topics/installation/debian.html#install-packages

(!) First is nice to add the official Salt repository to our package manager https://repo.saltstack.com/ 

### Installing Salt minions (aka client side)
Also I nstalled in salt minion using `apt-get install salt-minion`.

### Configuring the Salt minion (classic way)
Reading the Salt official configurartion about how to configure Salt https://docs.saltstack.com/en/latest/ref/configuration/index.html#configuring-salt

It's a good idea to configure the minion with custom grains in the minions so we can filter them
https://docs.saltstack.com/en/latest/topics/grains/

Example of a minion config file (You can also add, rack number, building, etc)

```shell
#file: /etc/salt/minion

# Your salt master ip address.
master: 192.168.0.247

# The minion custom grains.
grains:
  roles:
    - grafana
    - samba
```
We should restart salt minion in order to make the changes take effect.
```
root@salt-minion:# /etc/init.d/salt-minion restart
```
To get all the roles from salt minions you should run the following command
```
root@salt-minion:# salt '*' grains.get roles
salt-minion-A:
    - saltmaster
    - virtualbox
salt-minion-B:
    - grafana
    - samba
    - influxdb

```
### Configuring the Salt minion (Using saltify)
I didn't went deeper into saltify but it's like a tool to automate the salt-minion installation.
https://docs.saltstack.com/en/master/topics/cloud/saltify.html

#### Adding salt minion in salt master
Change the config file /etc/salt/minion at the minion.

Then in the salt master run the following command to check that the minion it's trying to connect to the master
```shell
root@host01:/srv# salt-key -L
Accepted Keys:
host01
Denied Keys:
Unaccepted Keys:
debian-s-1vcpu-1gb-nyc3-01.localdomain
Rejected Keys:
```
To accept the minion key run `salt-key  -a debian-s-1vcpu-1gb-nyc3-01.localdomain`

### Targeting minions
The simplest example it's target all the minions, for example for get all the grains
```shell
root@salt-master:# salt '*' grains.items
salt-minion:
    ----------
    SSDs:
    biosreleasedate:
        11/16/2016
    biosversion:
        F20
    cpu_flags:
        - fpu
        - vme
        - de
#Output have been cuted
```

#### Writting state .sls
State modules are located in /srv/salt/ and the core of salt stack. 

```shell
apache:                 # ID declaration
  pkg:                  # state declaration
    - installed         # function declaration
```
Salt states are created like this, with an arbitrary ID, the state declaration and the function to apply.

#### Apply a Salt state
If you want to apply salt states 

```shell
salt  server1 state.sls <your-salt-state> test=True
```

with the test=True you just run a test (aka run in drain mode)

If you want to check just the differences 

```shell
salt --state-output=changes  server1 state.sls <your-salt-state> test=True
```

#### Important to know 
Salt Stack uses Python, literally all when you do `salt '*' cmd.run 'hostname'` for example, you are running a Python script that runs the hostname command in the console. So is important to know what Python version it's using  salt. And just to general knowledge, where are located the Python scripts.

To know the python modules installed and the Python version used run the `salt '*' cmd.run 'salt-call --versions-report'` commmand.
```shell
root@host01:/home/nardison# salt '*' cmd.run 'salt-call --versions-report'
host01:
    Salt Version:
               Salt: 3000.3

    Dependency Versions:
               cffi: Not Installed
           cherrypy: Not Installed
           dateutil: 2.7.3
          docker-py: Not Installed
              gitdb: 2.0.5
          gitpython: 2.1.11
             Jinja2: 2.10
            libgit2: Not Installed
           M2Crypto: Not Installed
               Mako: Not Installed
       msgpack-pure: Not Installed
     msgpack-python: 0.5.6
       mysql-python: Not Installed
          pycparser: Not Installed
           pycrypto: 2.6.1
       pycryptodome: Not Installed
             pygit2: Not Installed
             Python: 2.7.16 (default, Oct 10 2019, 22:02:15)
       python-gnupg: Not Installed
             PyYAML: 3.13
              PyZMQ: 17.1.2
              smmap: 2.0.5
            timelib: Not Installed
            Tornado: 4.5.3
                ZMQ: 4.3.1

    System Versions:
               dist: debian 10.4
             locale: ascii
            machine: x86_64
            release: 4.19.0-6-amd64
             system: Linux
            version: debian 10.4

```
