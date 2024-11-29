<!-- image -->

# Differences between WebSphere Adapters and WebSphere Business Integration Adapters

There are several differences between WebSphere Adapters
and WebSphere Business Integration Adapters.
These distinctions are most important during development of applications.
When deploying applications to a running server, the nature of the
adapters used affects some of the steps that need to be followed.

Adapters provide communication mechanisms between enterprise information
systems (EISs) and Integration Designer applications. To illustrate
the operation of the adapters, Figure 1 
provides details of the communication between the server and the EIS
for the two types of adapters.

Figure 1. Detailed schematic of a WebSphere Adapter

<!-- image -->

Figure 1  depicts
a WebSphere Adapter managing the connectivity
between a Java EE component supported by the server and the EIS. The WebSphere Adapter resides inside the server.

| Feature              | WebSphere Adapters                                                                                                                                                                              | WebSphere Business Integration Adapters                                                                                                      |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| JCA Compliance       | Fully JCA compliant (version 1.5).                                                                                                                                                              | Not JCA-compliant.                                                                                                                           |
| Connectivity Manager | Rely on standard JCA contracts to manage lifecycle tasks such as starting and stopping.                                                                                                         | Rely on WebSphere Adapter Framework to manage connectivity.                                                                                  |
| Event Notification   | Use an EventStore subclass to retrieve events from an EIS.                                                                                                                                      | Manage event notification using a pollFor Events method.                                                                                     |
| Request Processing   | Clients directly invoke one of several interaction contracts to query or modify data in the EIS.                                                                                                | Rely on an integration server and the WebSphere Adapter Framework to initiate and help process requests.                                     |
| Data Models          | Use an Enterprise Metadata Discovery (EMD) utility to parse an EIS and develop Service Data Objects (SDOs) and other useful artifacts. The EMD is part of the WebSphere Adapter implementation. | Use a separate Object Discovery Agent (ODA) to introspect an EIS and generate business object definition schemas.                            |
| Integration          | Run on the server.                                                                                                                                                                              | Reside outside the server. The server or integration broker communicates with the adapter via a Java™ Message Service (JMS) transport layer. |