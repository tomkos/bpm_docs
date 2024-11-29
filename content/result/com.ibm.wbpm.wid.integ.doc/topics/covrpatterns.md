<!-- image -->

# Simple adapter wizard

The simple adapter wizard can save you time in creating a service.
In a few pages containing a few fields, you can generate a service.
In many cases, a service generated from the simple adapter wizard
will meet the requirements for the service you want to create.

The simple adapter wizard can be used with the following adapters:

- WebSphere® Adapter
for Email
- WebSphere Adapter
for FTP
- WebSphere Adapter
for Flat Files.

The following adapters have a simple wizard process:

| Adapter            | Description                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outbound Email     | The Email outbound simple wizard creates a service that sends simple messages using an Email server.                                                                                                                                                                                                                                                                          |
| Inbound FTP        | The FTP inbound simple wizard creates a service that retrieves a file in a specific directory on an FTP server. If the file is not in an XML format, you can specify a data handler that will transform from the file content format to business objects.  The file content can be split if the content contains multiple copies of the data structure for processing.        |
| Outbound FTP       | The FTP outbound simple wizard creates a service that stores data in a file in a specific directory on an FTP server. If the required output format is not an XML format, you can specify a data handler that will transform the business object to the file content format.                                                                                                  |
| Inbound Flat File  | The Flat File inbound simple wizard creates a service that retrieves a file from a directory on the local file system. If the file is not in an XML format, you can specify a data handler that  will transform from the file content format to business objects. The file content can be split if the content contains multiple copies of the data structure for processing. |
| Outbound Flat File | The Flat File outbound simple wizard creates a service that stores data in a file in a directory on the local file system. If the required output format is not an XML format, you can specify a data handler that will transform the business object to the file content format.                                                                                             |

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports