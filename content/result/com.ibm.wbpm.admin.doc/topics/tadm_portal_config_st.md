# Configuring Sametime
Connect integration for
Process Portal
(deprecated)

## Before you begin

Before
you begin this task, Process Portal must be
started.

## About this task

- The two environments must share a common user registry, and it
must be available as a base entry in your Business Automation Workflow federated repositories.
- To support the use of short names and email addresses for system
login, the federated repository entry must contain login properties
of either uid, mail, or uid;mail
- The two environments must share the same federated repositories
realm name.
- The two environments must share a Lightweight Third Party Authentication
(LTPA) key for single sign-on (SSO) functionality. This requires that
common domain names and interoperability mode are enabled
globally.
- You must import LTPA keys from one environment to the other.
- If you use SSL communication, it must be enabled on all the servers
in the configuration, including the Workflow Center server,
process server, and Sametime
Connect server. Normal
SSL configuration is required, including certificate exchange across
all servers.

## Procedure

1. Configure Business Automation Workflow and Sametime
Connect to share
the same user registry and the same federated repositories realm
name. For information, see Managing the realm in a federated repository
configuration.
2. Configure Business Automation Workflow and Sametime
Connect to share
an LTPA key for SSO functionality, which would include common domain
names and interoperability mode to be enabled in the Global
security panel and the Global
security > Single sign-on (SSO) panel in the administrative console. For information,
see Implementing single sign-on to minimize
web user authentications.
3. Import LTPA keys from one environment to the other. For
example, you must either import the Sametime
Connect LTPA keys
into Business Automation Workflow or
import the Business Automation Workflow LTPA
keys into Sametime
Connect.
For information, see Importing Lightweight Third Party Authentication
keys.
4 Configure the Sametime Proxy Server so that the domainthat is specified in the SSO settings is in the allowed list of domains. All subsequent access to Process Portal and SametimeConnect must be donethrough a host name that ends in this domain name.
    1. Log in to the Sametime System Console as the Sametime
administrator.
    2. Click Sametime Servers > Sametime Proxy Servers.
    3. From the Proxy Servers list,
select the name of a Sametime Proxy Server to open its Configuration
page.
    4. In the Domain list of Sametime Proxy Server section,
enter the same domain name that you used in the WebSphere
Application Server SSO settings, for
example, ibm.com.
    5. Click OK and restart all the WebSphere
Application Server Sametime servers.
5. Configure the Process Portal endpoint.
 
For Process Portal
Configure the PROCESS\_PORTAL\_SUPPORT scenario
key to use the WCCMConfigStrategy strategy and point
to a virtual host information object that identifies the Process Portal server. 
For Heritage Process Portal
Configure the PROCESS\_PORTAL\_JS scenario key
to use the WCCMConfigStrategy strategy and point
to a virtual host information object that identifies the Process Portal server.

Perform the appropriate steps that are described
in Configuring endpoints to match your topology.
6. Restart the Business Automation Workflow servers.

## Results

## What to do next