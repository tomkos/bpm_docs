# Verifying Process Portal on a Business Automation Workflow server

## Procedure

1 Verify that all the applications used by Process Portal are accessible.
    1. Using a web browser, open the URL for the IBM® Process
Portal verification page.

Table 1. Process Portal URLs for HTTP and
HTTPS

Protocol 
Port
Process Portal URL

HTTP
Default (80)
http://BPM\_host/ProcessPortal/web\_test

HTTP
Non-default
http://BPM\_host:port/ProcessPortal/web\_test

HTTPS
Default (443)
https://BPM\_host/ProcessPortal/web\_test

HTTPS
Non-default
https://BPM\_host:port/ProcessPortal/web\_test

Where BPM\_host is the host name or IP address of your Business Automation Workflow server or routing server, and
port is the port number used for the Process Portal service.
    2. If you are prompted for them, enter a valid user ID and password.
    3 If you cannot log in to Process Portal ,perform the following actions:
        1. Make sure that you are using the correct URL. Try using an IP address instead of a host
name.
        2 If you get no logon window, or you get an HTTP error 404 , page not found, orWebGroup/Virtual Host error, try the following actions.
            - If you use a proxy server:
                - Check the proxy server's SystemOut.log file. Any messages similar to the
following message: TCPC0003E: TCP Channel TCP\_7 initialization failed. The socket bind
failed for host * and port 80. The port may already be in use. probably indicate that
another service is using the same port number. If there is a conflict, you must change the proxy
port number and virtual host port number manually to avoid any possible conflicts. Tip: To check or change the virtual host settings for the proxy server, in the administrative console,
click Environment > Virtual Hosts.
Important: If you change the proxy server port number, also check
whether step iv
applies.
                - Check that the /ProcessPortal context root for the Process Portal web application is correctly mapped.
        - If you are using an HTTP server as a routing server, check the web module mapping.
3. Make sure that you are using a valid user ID and password to access Process Portal.
4 If you use a proxy server and are not using the default ports for http and https(80 or 443) perform the following actions:
    1. Make sure that the non-default ports that you are using for HTTP and HTTPS are redirected. Using
the administrative console, click Environment > Virtual Hosts, and add the non-default host aliases for your servers to the
default\_host list. For example if you use port 81 for HTTP and port 444 for HTTPS,
add *:81 and *:444 .
    2. If you use host names for the proxy servers rather than IP addresses, for each proxy server,
make sure that host name of the proxy server is in the host files for the deployment manager and the
proxy server itself.
    3. Restart the deployment manager.
    4. Configure the proxy server to add a rewriting rule for the application server SSL host name and
port. On the admin console, Servers > WebSphere proxy servers > server\_nameProxy Settings > HTTP Proxy Server Settings > Rewriting rules > New, for From URL pattern enter the protocol, host, port, and
wildcard for the application server SSL service, for example
https://app\_server\_host\_name:9483/* . For To URL pattern
enter the protocol, host, port, and wildcard for the proxy server SSL service, for example,
https://proxy\_server\_host\_name:444/*.
    5 Synchronize the managed nodes with the deployment manager using the syncNode command from the profile\_root/bin directory or from the Quick start console forthe profile. Use the following syntax: Where deployment\_manager is the host name or IP address of the deploymentmanager, and port is the port number. For more information about thesyncNode command, see syncNode command in the WebSphere® ApplicationServer documentation.
        - syncNode.sh deployment\_manager
port
        - syncNode.bat deployment\_manager
port
5. Try to open the Process Portal URL again.
4 If the Process Portal verification page isdisplayed, verify that each application listed on the page has a check mark next to it. If any applications are marked with an x , there is a problem that must beresolved with that application before Process Portal can work fully. If there are problems, consider the following. Table 2. Troubleshooting problems shown on the Process Portal verification page Application Application name prefix Things to check Process Portal IBM\_BPM\_Responsive\_Portal\_ Process Portal Notification IBM\_BPM\_Responsive\_Portal\_Notification\_ WLE REST Services IBM\_BPM\_Teamworks\_

- Click the application name for more information about it.
- For the applications that have a problem, perform the corresponding checks that are listed in
the following table.

| Application                 | Application name prefix                 | Things to check                                                                                                                                                                                                        |
|-----------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process Portal              | IBM\_BPM\_Responsive\_Portal\_              | Verify that Process Portal is configured. Check that the EAR files are available on the routing server.                                                                                                                |
| Process Portal Notification | IBM\_BPM\_Responsive\_Portal\_Notification\_ | Verify that Process Portal is configured. Check that the EAR files are available on the routing server.                                                                                                                |
| WLE REST Services           | IBM\_BPM\_Teamworks\_                      | Make sure that application deployment target cluster is available. Make sure that the IBM\_BPM\_Teamworks\_ application is installed. Make sure that the web modules in the EAR file are available on the routing server. |

2 Verify that Process Portal works.

1. Open Process Portal. 
Using a web browser to access the URLs for your Process Portal. 
Table 3. Process Portal URLs for HTTP and
HTTPS

Protocol 
Port
Process Portal URL

HTTP
Default (80)
http://BPM\_host/portal

HTTP
Non-default
http://BPM\_host:port/portal

HTTPS
Default (443)
https://BPM\_host/portal

HTTPS
Non-default
https://BPM\_host:port/portal

Where BPM\_host is the host name or IP address of your Business Automation Workflow server or routing server, and
port is the port number used for the Process Portal service.If you use HTTP and HTTPS
protocols, verify both URLs.
2. Verify that Process Portal is displayed and
can be used.

## Results