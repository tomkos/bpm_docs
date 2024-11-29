# Getting case data from an external data source

## About this task

For example, you might have a database that contains detailed customer records. When a
case worker enters a customer’s serial number, the external data service can get the name and
address of the customer from that database. These values are then incorporated into the case data
and stored in Content Platform Engine.

In addition to getting property
values, you can use an external data source to modify property attributes such as minimum value or
maximum value. The external data service must work within any constraints placed on the property
attributes in Content Platform Engine. For example, if a minimum value is
specified for the property in Content Platform Engine, the external data
service cannot make the setting less restrictive. That is, the service can set the minimum only to a
larger value. It cannot decrease the minimum value.

## Procedure

To get data from an external data source:

1. Use the workflow APIs to implement a service to extract case data from the external data
source.
2. Use the Case configuration tool to
register the external data service for use with your solution.

Restriction: You can register only one external data service for a solution.
3. Import the certificate of the External Data Services (EDS) server.
4. Deploy or redeploy the solution and run it.
5. Optional: If the EDS application is configured with a
secured login, in the WebSphere® Application
Server, under Security role to user/group for the EDS application, map the
All Authenticated role to the special subject All Authenticated in
Application's Realm.

## Results

After you register the external data service, Case Client communicates with the service
to get case data whenever case workers create cases or modify cases. This communication is handled
automatically through the workflow APIs.

For properties that are associated with an external data service choice list, only
the value, not the display name, is persisted. The Search widget, which generates a result set for
the Case List widget, does not call the external data service to retrieve the display names for
these properties. However, selecting the case from the Case List widget does cause the external data
service to retrieve the property display names.

- Implementing an external data service by using the REST protocol

To use external data with your solution, you must create a service that implements the external data service REST protocol. This protocol provides for the communication between Case Client and the external data source.