# Implementing an external data service by using the REST protocol

## About this task

In addition to implementing the REST protocol, the external
data service must implement any authentication that is required by
the external data source.

## Procedure

To implement an external data service:

1. Implement the POST method for the particular object type resource. 
This method is called automatically by the REST protocol in response to requests from Case Client to create or modify a case.
The external data service must submit the data for the case properties that it manages back to the
REST protocol in the response to the POST method.
2. If the service modified any attributes for the case properties
that it manages, retrieve the property attributes.
To retrieve
property attributes, you can use the Content Platform Engine Java™ protocol or IBM® CMIS for FileNet® Content Manager in the external data
service.
3. If the external data service needs to authenticate users,
configure authentication for users.

- Particular object type resource

The particular object type resource represents a case type in which property values are obtained from an external data source. When a case of the specified case type is created or modified, the workflow REST protocol uses this resource to obtain data for that case from the external data source.
- Authentication for external data services

If your external data service needs to authenticate users, it must participate in the same single sign-on authentication configuration as the other Business Automation Workflow components, such as Case Client or the REST protocol.
- Persistence of case data

When a case worker saves a new case or an updated case, the workflow REST protocol makes a final call to the external data service. The REST protocol uses the response returned by the service to determine which values are to be saved to the repository for the case.
- Example data flow for case creation

If an external data service is registered for a solution, data for a new case is automatically obtained from that service. The workflow REST protocol handles the exchange of data between Case Client and the external data service.