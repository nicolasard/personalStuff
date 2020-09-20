
##  Apache2 KeepAlive Issue

This are my notes about an issue detected that makes apache close a connection when sending a 500 http response code.

I wasn't able to find a configuration that allow us to fix this so I started to dig in to the apache code, I forked it in to my github so then I can change/version it to have
a version that works as expect.

