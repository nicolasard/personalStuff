
##  Apache2 KeepAlive Issue

This are my notes about an issue detected that makes apache close a connection when sending a 500 http response code.

I wasn't able to find a configuration that allow us to fix this so I started to dig in to the apache code, I forked it in to my github so then I can change/version it to have
a version that works as expect.

Found in this(https://github.com/nicolasard/httpd/blob/c77e6abe3b1d3d612bcf5ce694c8c937cf031fbb/modules/http/http_core.c#L183) in the http module where if `c->aborted aborted` is true we close de keepalive connection.

Also found this header where is defined the https://github.com/nicolasard/httpd/blob/c77e6abe3b1d3d612bcf5ce694c8c937cf031fbb/include/httpd.h#L569 the ap_status_drops_connection where with a comment `/** should the status code drop the connection */`.
