# Configuring allowed origins for Process Portal

## Before you begin

- If you intend to run BPEL processes and human tasks from Process Portal, the topology for your federated environment
must include an HTTP server in front of the server that hosts the BPEL processes.
- Ensure that single-sign on is configured for all federated servers in the federated environment,
including the server that hosts Process Portal. For
more information, see Configuring SSO for federated environments.

## About this task

To enable the cross-origin requests within the federated environment, you must configure a list
of allowed origins for Process Federation Server and
the federated servers. The allowed origin value is the URL prefix that the clients use to access the
Process Portal web application.

For
more information about the various topologies, see Adding a Business Automation Workflow system to the federated environment.

## Procedure

1 For all federated systems. Configure Process Federation Server forallowed origins.
    1. Open the server.xml configuration
file for editing. 
By default, the configuration file is in the
pfs\_install\_root/usr/servers/server\_name directory on
Process Federation Server.
    2 For each ibmPfs\_federatedSystem elementin the server.xml file, configure the allowedOrigins property. For more information about the allowedOrigins property,see Configuration properties for the Process Federation Server index .
        - The following snippet shows an example of an allowedOrigins property that
allows requests from an originating Process Portal
server:allowedOrigins="https://portal.mycompany.com:9443"Note: Most federated
environments are likely to have only a single originating Process Portal server, because even in clustered Process Portal configurations, typically a single HTTP
server URL is accessed by end users. If you have more than one originating Process Portal server, use commas to separate the servers in
the allowedOrigins property, or use * (asterisk) to allow all originating
servers.
        - The following snippet shows an example of an allowedOrigins property
that allows requests from all originating servers. The value is set
to * (asterisk).allowedOrigins="*"
2 For BPEL federated systems only. Configure allowed origins on the HTTP server in front ofthe server that hosts the BPEL processes.

1. Update the configuration file on the HTTP server, for example
httpd.conf or apache.conf, or the
.htaccess file with the following settings.
Do not use the asterisk (*) wildcard character in any of the
statements.Header set Access-Control-Allow-Origin "https://portal.mycompany.com:9443"
Header set Access-Control-Allow-Credentials "true"
Header set Access-Control-Allow-Headers "DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization"
Header set Access-Control-Allow-Methods "GET,POST,PUT,DELETE,OPTIONS"
2. Allow the HTTP server to modify the request and response headers by enabling
mod\_headers in the configuration file.
3. Restart the HTTP server for the changes to take effect.
3 For BPD federated systems only. Configure each federated server for allowedorigins. In the 100Custom.xml file on each federated server, add anallowed-origins configuration parameter in the <rest> element.

In the 100Custom.xml file on each federated server, add an
allowed-origins configuration parameter in the <rest>
element.

- The following snippet shows an example of an allowed-origins parameter that
allows requests from two originating Process Portal
servers:<server>
   <rest merge="mergeChildren">
      <allowed-origins>
      https://portal.mycompany.com:9443
      </allowed-origins>
   </rest>
</server>Note: Most
federated environments are likely to have only a single originating Process Portal server because even in clustered Process Portal configurations, typically a single HTTP
server URL is accessed by end users. If you have more than one originating Process Portal server, use commas to separate the servers in
the allowedOrigins property, or use * (asterisk) to allow all originating
servers.
- The following snippet shows an example of an allowed-origins parameter that
allows requests from all originating servers. The value is set to *
(asterisk).<allowed-origins>*</allowed-origins>
4. For your updates to take effect, restart WebSphere® Application
Server.