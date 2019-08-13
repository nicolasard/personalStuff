
## Salt
Salt it's a server-client application that allow sys admin run commands in multiple servers at once, and create custom scripts to run commands in the servers.
So for example if you have to install an apache in your new server. First install the Salt client (aka minion) and then from master run the script you had already made to install an apache server automactly 

### Installing Salt Master (aka server side)
In debian just apt-get install salt-master https://docs.saltstack.com/en/latest/topics/installation/debian.html#install-packages

### Installing Salt minions (aka client side)

### Configuring the Salt minion
Reading the Salt official configurartion about how to configure Salt https://docs.saltstack.com/en/latest/ref/configuration/index.html#configuring-salt

It's a good idea to configure the minion with custom grains in the minions so we can filter them
https://docs.saltstack.com/en/latest/topics/grains/

Example of a minion config file

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
