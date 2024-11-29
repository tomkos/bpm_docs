# Configuring Workplace on-premises for a
federated environment

## About this task

In a federated environment, you must configure the endpoint URLs on the server that hosts
Workplace. You must also
configure a list of allowed origins for cross-domain requests between Workplace and Process Federation Server, and between
Workplace and the
federated servers.

## What to do next

1. Retrieve the 36 lowercase-character identifier of the target object store for the case system to
be federated from the target object store details in the Administration Console for Content Platform
Engine (ACCE). The
lowercase-character identifier is the name of the index that is created and populated by the case
system in the Process Federation Server federated data
repository.Tip: Note that ACCE might display the identifier by using uppercase
characters, however, for Process Federation Server configuration
you must use only lowercase characters. For example, if the identifier is displayed as
93844FD1-5A75-4809-9369-EA9C6AOC96F6 in ACCE, use
93844fd1-5a75-4809-9369-ea9c6a0c96f6 instead in the Process Federation Server
server.xml configuration file.
2. Add the following XML configuration elements to the Process Federation Server
server.xml configuration file, replacing
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx with the target object store identifier that
you retrieved earlier and also case.server.host and
case.server.port with the host and port number of the Business Automation Workflow server case
system:<ibmPfs\_federatedSystem
    id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    indexProcessInstances="true"
    displayName="Case system xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    indexName="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    allowedOrigins="*"
    systemType="SYSTEM\_TYPE\_CASE"
    restUrlPrefix="https://case.server.host:case.server.port/CaseManager/" />

&lt;ibmPfs\_caseRetriever
    federatedSystemRef="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    internalRestUrlPrefix="https://case.server.host:case.server.port/CaseManager/CASEREST/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" />

1. Set up single sign-on for the server that hosts Workplace. For more information,
see Configuring SSO for federated environments by using LTPA keys.
2. Set up secure communications between Workplace and Process Federation Server. For more
information, see Securing SSL communications between client applications and Process Federation Server.

- Federation considerations for Workplace

Additional considerations apply to Workplace when it is configured for a federated environment.
- Configuring endpoint URLs for Workplace

To enable Workplace for a federated environment, configure endpoint URLs so that Workplace can communicate with Process Federation Server and the federated systems. You can configure the URLs in the 100Custom.xml configuration file.
- Configuring allowed origins for Workplace

Workplace makes requests to Process Federation Server and federated servers. When these services are not on the system that originated Workplace, cross-origin resource sharing (CORS) is used to enable the browser to trust the cross-origin requests.