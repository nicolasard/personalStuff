## Apache2

This are my notes about the aventure of compiling Apache2. The most used webserver.

### Environment
SO: Debian GNU/Linux 9.1 (stretch)

### Compiling and runing a fresh new Apache2 Server
1. Install dependencies.
```
apt-get install libapr1-dev libaprutil1-dev 
apt-get install libpcre3-dev 
```

2. Download the source
```
wget http://apache.dattatec.com//httpd/httpd-2.4.39.tar.gz 
```
3. Configure 
```
./configure --prefix=/opt/apache2/
```
4. Make 

5. Install

### Configuration
The apache configuration it's in the file /apache2/conf/httpd.conf. 

To reload the configuration without restart the server run 
```
/apache2/bin/apachectl -k graceful
```
You can test the config syntax running 
```
/apache2/bin/apachectl configtest
```

#### mod_proxy: Using when you want to use apache as proxy between your users and the application server.

It's pretty common that some times you need to configure apache in front of your app to do balancer. (https://httpd.apache.org/docs/trunk/en/howto/reverse_proxy.html)

```
	ProxyPass "/status-sim/" "http://167.71.57.12/"
	ProxyPassReverse "/" "http://167.71.57.12/"
```

Above example will send all the traffic from our clients that goes to `/status-sim/` to `/` in the app host `167.71.57.12`

### mod_proxy + balancer

#### KeepAlive
KeepAlive allows clients to re-use the same channel in each request. (https://httpd.apache.org/docs/2.4/es/mod/core.html#keepalive)

#### Testing some apache behavoirs with Curl
Of course to test a webserver there is nothing like a web browser. Or use curl (https://curl.haxx.se/) that tool that some http clients based in.

*Example 1*: Running multiple queries in the same connection to check how the keeaplive is working.

### Plus! Jenkins file to compile the app
```
pipeline {
    agent any 
    stages {
        stage('Download') { 
            steps {
               sh 'wget http://apache.dattatec.com//httpd/httpd-2.4.39.tar.gz'
            }
        }
        stage('Compile') { 
            steps {
                sh 'tar -zxvf httpd-2.4.39.tar.gz'
                dir("./httpd-2.4.39") {
                    sh "./configure --prefix=/opt/apache2/"
                    sh "make"
                }
            }
        }
        stage('Install Bin') { 
            steps {
                dir("./httpd-2.4.39") {
                    sh "make install"
                }
            }
        }
    }
}
```


