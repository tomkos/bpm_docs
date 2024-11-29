# Deleting a proxy server

## Procedure

1. In the administrative console, click Servers > Server Types > WebSphere proxy servers, and delete the proxy server.
2 Click Environment > Virtual hosts > default\_host > Host Aliases and remove the followinghost aliases:
    - Host name: * Port: proxy\_http\_port
    - Host name: * Port: proxy\_https\_port
3. Click Environment > Virtual hosts  and delete the
virtual host.