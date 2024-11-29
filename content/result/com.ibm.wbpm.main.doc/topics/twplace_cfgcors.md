# Configuring allowed origins for Workplace

## Before you begin

## About this task

To enable the cross-origin requests within the federated environment, you must configure a list
of allowed origins for Process Federation Server and the
federated servers. The allowed origin value is the URL prefix that the clients use to access the
Workplace web
application.

For example, if the server that hosts Workplace is available at
https://workplace.mycompany.com:9443, configure this URL to be an allowed origin on
Process Federation Server, and
on each federated server. The allowed origin indicates to Process Federation Server and federated
servers that REST requests that originate from https://workplace.mycompany.com:9443
are trusted and are to be allowed. If you use an HTTP server in front of Workplace, use the HTTP server
URL prefix as the allowed origin.

## Procedure

1 For all federated systems. Configure Process Federation Server for allowedorigins.
    1. Open the server.xml configuration file for editing. 
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2 For each ibmPfs\_federatedSystem element in theserver.xml file, configure the allowedOrigins property. For more information about the allowedOrigins property, seeConfiguration properties for the Process Federation Server index .
        - The following snippet shows an example of an allowedOrigins property that
allows requests from an originating Workplace
server:allowedOrigins="https://workplace.mycompany.com:9443"Note: Most
federated environments are likely to have only a single originating Workplace server, because even in
clustered configurations, typically a single HTTP server URL is accessed by end users. If you have
more than one originating Workplace server, use commas to
separate the servers in the allowedOrigins property, or use * (asterisk) to
allow all originating servers.
        - The following snippet shows an example of an allowedOrigins property that
allows requests from all originating servers. The value is set to *
(asterisk).allowedOrigins="*"
2. For your updates to take effect, restart WebSphere® Application
Server.