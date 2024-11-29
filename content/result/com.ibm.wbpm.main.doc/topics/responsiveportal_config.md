# Configuring Process Portal for
a federated environment

## Before you begin

## About this task

For Process Portal to work correctly in a
federated environment, you must configure endpoint URLs on the server that hosts Process Portal. You must also configure a list of allowed
origins for cross-domain requests between Process Portal and Process Federation Server and between Process Portal and the federated servers. If you are running
BPEL processes on Process Portal, additional
requirements apply to the allowed origins.

In federated environments,
the Process Portal content
is automatically refreshed every 60 seconds. To change the refresh
interval, update the value of the com.ibm.bpm.portal.federatedRefreshInterval mashups
property. For more information, see Configuring custom properties.

## What to do next

1. Set up single sign-on for the server that hosts Process Portal. For more information, see Configuring SSO for federated environments by using LTPA keys.
2. Set up secure communications between Process Portal and Process Federation Server.
For more information, see Securing SSL communications between client applications and Process Federation Server.

- Federation considerations for Process Portal

Additional considerations apply to Process Portal when it is configured for a federated environment.
- Configuring endpoint URLs for Process Portal

To enable Process Portal for a federated environment, configure endpoint URLs so that Process Portal can communicate with Process Federation Server and the federated systems. You can configure the URLs in the 100Custom.xml configuration file.
- Configuring allowed origins for Process Portal

Process Portal makes requests to Process Federation Server and federated servers. When these services are not on the system that originated Process Portal, cross-origin resource sharing (CORS) is used to enable the browser to trust the cross-origin requests.