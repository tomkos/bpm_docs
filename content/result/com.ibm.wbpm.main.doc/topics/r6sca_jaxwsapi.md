<!-- image -->

# File artifacts and XML namespaces for the JAX-WS-based Business
Process Choreographer web services APIs

- HTTP transport layer
- JMS transport layer

## HTTP transport layer

Beginning
with WebSphere® Process
Server Version
7, the JAX-WS-based web services API using the HTTP transport layer
replaces the JAX-RPC-based Business Process Choreographer web services
API. Two Business Process Choreographer web services interfaces are
provided, one for BPEL processes and one for human tasks.

| Business Process Choreographer web services interface   | JAX-WS webs services file artifact   | JAX-WS webs services XML namespace                                                     |
|---------------------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------|
| Business Flow Manager web service                       | BFMJAXWSService.wsdl                 | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0/Binding          |
| Business Flow Manager web service interface             | BFMJAXWSInterface.wsdl               | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0                  |
| Business Flow Manager web service data types            | BFMJAXWSInterface.xsd                | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0                  |
| Business Flow Manager web service data Types            | BFMDataTypes.xsd                     | http://www.ibm.com/xmlns/prod/websphere/business-process/types/7.0                     |
| Business Flow Manager callback web service              | BFMJAXWSCallbackService.wsdl         | http://www.ibm.com/xmlns/prod/websphere/business-process/callback-services/7.0/Binding |
| Business Flow Manager callback web service interface    | BFMJAXWSCallbackInterface.wsdl       | http://www.ibm.com/xmlns/prod/websphere/business-process/callback-services/7.0         |
| Human Task Manager web service                          | HTMJAXWSService.wsdl                 | http://www.ibm.com/xmlns/prod/websphere/human-task/services/7.0/Binding                |
| Human Task Manager web service interface                | HTMJAXWSInterface.wsdl               | http://www.ibm.com/xmlns/prod/websphere/human-task/services/7.0                        |
| Human Task Manager web service data types               | HTMJAXWSInterface.xsd                | http://www.ibm.com/xmlns/prod/websphere/human-task/services/7.0                        |
| Human Task Manager web service data types               | HTMDataTypes.xsd                     | http://www.ibm.com/xmlns/prod/websphere/human-task/types/7.0                           |
| Human Task Manager callback web service                 | HTMJAXWSCallbackService.wsdl         | http://www.ibm.com/xmlns/prod/websphere/human-task/callback-services/7.0/Binding       |
| Human Task Manager callback web service interface       | HTMJAXWSCallbackInterface.wsdl       | http://www.ibm.com/xmlns/prod/websphere/human-task/callback-services/7.0               |
| Common Business Process Choreographer data types        | BPCDataTypes.xsd                     | http://www.ibm.com/xmlns/prod/websphere/bpc-common/types/7.0                           |

## JMS transport layer

Beginning with IBM® Business Process Manager
Advanced Version
8, the SOAP/JMS API replaces the Business Process Choreographer JMS
API. A Business Process Choreographer web services interface for BPEL
processes is provided.

| Business Process Choreographer web services interface   | JAX-WS web services file artifact   | JAX-WS web services XML namespace                                             |
|---------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------|
| Business Flow Manager web service                       | BFMJMSService.wsdl                  | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0/Binding |
| Business Flow Manager web service interface             | BFMJAXWSInterface.wsdl              | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0         |
| Business Flow Manager web service data types            | BFMJAXWSInterface.xsd               | http://www.ibm.com/xmlns/prod/websphere/business-process/services/7.0         |
| Business Flow Manager web service data Types            | BFMDataTypes.xsd                    | http://www.ibm.com/xmlns/prod/websphere/business-process/types/7.0            |