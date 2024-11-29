# Configuring Secure Sockets Layer (SSL) communication in a network deployment
environment

## Before you begin

- IBM® Business Automation
Workflow
generates a default signer certificate during profile creation and uses it to sign personal
certificates for all of the Java virtual machines in the cell. If you do not want to use the default
signer certificate, you must create a personal certificate request to obtain a certificate that is
signed by a certificate authority (CA). Refer to Creating a certificate authority request.
- To import an SSL security certificate into Integration Designer, see Importing an SSL security certificate into Integration
Designer.
- Ensure that the Common Name field of the SSL certificate matches the host name that will be used
to access the server. For information on troubleshooting connection problems, see SSL fails when host name configuration fails.
- If the name of a server certificate does not match the host name of a server, an SSL connection
failure may occur with the IOException message HTTPS hostname wrong. To
help resolve this problem, you can add a Subject Alternative Name (SAN) set to the server
certificate. Information about SAN sets is found in the topic SSL fails when host name configuration fails.

## About this task

## Procedure

1 Import the Workflow Server WebSphere®Application Server root SSL certificateinto Workflow Center .
    1. In the Workflow Center
WebSphere
Application Server administrative
console, click Security > SSL certificate and key
management > Key stores and
certificates > CellDefaultTrustStore > Signer certificates > Retrieve from
port.
    2. Enter the Host name, secure Port of the
Workflow Server profile
(WC\_defaulthost\_secure), and Alias, and click Retrieve signer
information. You can retrieve the signer information for any of the servers
listed.

Note: The WC\_defaulthost\_secure profile is located in the WebSphere
Application Server administrative console.
Navigate to Servers > Server Types > WebSphere Application
Servers > SERVER\_NAME > Ports.
    3. Click Apply and save your changes.
2 Import the Workflow Center root SSL certificate into Workflow Server .

1. In the Workflow Server
WebSphere
Application Server administrative
console, click Security > SSL certificate and key management > Key stores and certificates > CellDefaultTrustStore > Signer certificates > Retrieve from port.
2. Enter the Host name, secure Port of the Workflow Center profile
(WC\_defaulthost\_secure), and Alias, and click Retrieve signer
information. You can retrieve the signer information for any of the servers
listed.

Note: The WC\_defaulthost\_secure profile is located in the WebSphere
Application Server administrative console.
Navigate to Servers > Server Types > WebSphere Application Servers > SERVER\_NAME > Ports.
3. Click Apply and save your changes.
3. Open WAS\_HOME\bin and run the following commands on
both Workflow Center and
Workflow Server to change
internal links to use HTTPS and secured port.

Note: You only need to run this command if you have upgraded from a version prior to 8.5.0.1. 
For example:
# Run the following commands on both the Workflow Center and Workflow Server.
wsadmin -conntype NONE -lang jython
wsadmin> ps = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name
    /BPMClusterConfigExtension:/environment\_type:/")
# For the environment\_type variable, specify "BPMProcessCenter" when running in a
# Workflow Center environment or specify "BPMProcessServer" when running in a Workflow Server environment.
wsadmin> print ps # See how many Workflow Servers you listed 
wsadmin> print AdminConfig.show(ps) #look at useHTTPSURLPrefixes to see the current value 
wsadmin> AdminConfig.modify(ps, [['useHTTPSURLPrefixes', 'true']]) 
wsadmin> print AdminConfig.show(ps) #verify your change
wsadmin> AdminConfig.save()
wsadmin> exit
4 Optional: Disable all unsecured ports on all Workflow Center and Workflow Server servers.

1. Log in to the WebSphere
Application Server administrative console
and navigate to Servers > Server Types > WebSphere Application
Servers.
2. For each server, click the server link, then go to Container Settings > Web Container Settings > Web
container transport chains.
3. Click each link for the unsecured port, for example,
HttpQueueInboundDefault, and clear the Enabled check
box.
4. Repeat these steps for all WebSphere
Application Server cluster members on all
nodes. For example, if the xxx.AppTarget cluster has members on
Node1 and Node2, these steps must be performed on both nodes.
5. Optional: In the Workflow Center
WebSphere
Application Server administrative
console, click Security > Global
security > Web and SIP security > Single sign-on (SSO) and check the Requires
SSL check box.
6. Optional: In the Workflow Server
WebSphere
Application Server administrative
console, click Security > Global
security > Web and SIP security > Single sign-on (SSO) and check the Requires
SSL check box.
7 Specify HTTPS URLs and ports for all Representational State Transfer (REST) services foryour environment by using the REST service administrative console page.

1. Click Services > REST services > REST service providers.
2. Select all from the Scope selection
pull-down menu.
3. Click on the REST service provider in Provider Application
field and specify the Host name or virtual host in a load-balanced
environment and the Port.

Important: For a REST Services Gateway deployment manager, use the deployment manager
host name and port; do not use the IHS host name and port.
4. Click Apply and save your changes.
8. To make sure that Workflow Server connects to Workflow Center using SSL, specify an
HTTPS URL for the processCenterUrl variable, as described in Customizing the Workflow Server settings used to connect to Workflow Center. 
Note: This step is not required if you have already provided the intended
processCenterUrl value when running the BPMConfig
command.
9 Set the deploySnapshotUsingHttps property to true tomake sure that the Workflow Center connects to theWorkflow Server using SSL foronline deployment. Run the following commands on both the Workflow Center and the Workflow Server . # Run the following commands on both the Workflow Center and Workflow Server .wsadmin -conntype NONE -lang jythonwsadmin> ps = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name /BPMClusterConfigExtension:/environment\_type:/BPMServerSecurity:/") # For the environment\_type variable, specify "BPMProcessCenter" when running in a# Workflow Center environment or specify "BPMProcessServer" when running in a Workflow Server environment.wsadmin> print AdminConfig.show(ps) #look at deploySnapshotUsingHttps to see the current valuewsadmin> AdminConfig.modify(ps, [['deploySnapshotUsingHttps', 'true']]) # default value is falsewsadmin> print AdminConfig.show(ps) #verify your change wsadmin> AdminConfig.save()wsadmin> exit Note: Version support differences:

```
# Run the following commands on both the Workflow Center and Workflow Server.
wsadmin -conntype NONE -lang jython
wsadmin> ps = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name
    /BPMClusterConfigExtension:/environment\_type:/BPMServerSecurity:/") 
# For the environment\_type variable, specify "BPMProcessCenter" when running in a
# Workflow Center environment or specify "BPMProcessServer" when running in a Workflow Server environment.
wsadmin> print AdminConfig.show(ps) #look at deploySnapshotUsingHttps to see the current value
wsadmin> AdminConfig.modify(ps, [['deploySnapshotUsingHttps', 'true']]) # default value is false
wsadmin> print AdminConfig.show(ps) #verify your change 
wsadmin> AdminConfig.save()
wsadmin> exit
```

- IBM Business Automation Workflow V8.5.0.1
and later Workflow Centers
will use the deploySnapshotUsingHttps property setting for IBM Business Automation Workflow V8.5.0.0 Workflow Servers.
- IBM Business Automation Workflow V8.5.0.1
and later Workflow Centers
will not use the deploySnapshotUsingHttps property setting for IBM Business Automation Workflow V8.5.0.1 Workflow Servers. They will use the
full URL, including protocol, as it was sent by the Workflow Server.
- IBM Business Automation Workflow V8.5.0.0
Workflow Centers will use the
deploySnapshotUsingHttps property setting for IBM Business Automation Workflow V8.5.0.0 Workflow Servers.
10 Restart the Workflow Server and Workflow Center servers.

1. Use the WebSphere
Application Server administrative console to stop the clusters.
2. Stop the node agent and deployment manager.
3. Restart the deployment manager.
4. Restart the node agent.
5. Use the WebSphere
Application Server administrative console to start the clusters.
11 Verify your configuration.

1. Log in to Workflow Center using an https
connection.
2. From the Server tab, click runtime
server > configure server and confirm that it is
opened in a secure browser with https.

- Re-enabling HTTP access in Business Automation Workflow temporarily

IBM Business Automation Workflow doesn't support HTTP by default. It is not recommended that you switch to HTTP because it makes Business Automation Workflow less secure. However, if you are upgrading from IBM BPM V8.5 and can't immediately modify your connections to use secure HTTPS, you can temporarily re-enable HTTP access to web user interfaces that were available over unencrypted HTTP in  Business Automation Workflow 8.5.7.201612.
- Reverting to secure HTTPS

After you change all your server communications to use HTTPS to connect to IBM Business Automation Workflow, set Business Automation Workflow to once again enforce HTTPS-only policies.

## Related information

- SSL handshake failure with an external HTTP server