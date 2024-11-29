# Case configuration tool task
fails with 414 error

## Symptoms

```
An error occurred while running New\_Register Target Environment
The task failed because of the following error: 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>414 Request-URI Too Large</title>
<head><body>
<h1>Request-URI Too Large</h1>
<p>The request could not be processed by the server. The request URI
is longer than the permissible limit.</p>
</body></html>
```

## Causes

The size of the HTTP request line is larger than 8190 bytes.

## Resolving the problem

1. Increase the size of the HTTP request line that is accepted from a client by updating the
httpd.conf file for Oracle HTTP server to contain the following
line:LimitRequestLine 16384For complete information about the
LimitRequestLine parameter, see the "LimitRequestLine Directive" section of the Oracle documentation
at http://docs.oracle.com/cd/B14099\_19/web.1012/q20206/mod/core.html.
2. Restart the Oracle HTTP Server.