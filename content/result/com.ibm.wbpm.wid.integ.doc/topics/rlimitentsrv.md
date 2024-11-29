<!-- image -->

# Limitations for adapter imports and exports

- General limitations
- Connections
- Languages
- JMS bindings
- WebSphere Business Integration adapters
- WOLA Resource Adapter
- WebSphere runtime environment variables
- Bidirectional support
- Generated interfaces

## General limitations

- Programmatically accessing the data binding is not supported.
- IMS multisegment messages
are not supported.
- Only one instance of a resource adapter that uses native libraries
can be used in each session.During each IBM® Integration
Designer session,
the tools can use only one instance of the resource adapter that uses
native libraries.
For example, if you import a resource adapter
that uses native libraries into two connector projects, A and B, then
you will have created two instances of this resource adapter in the
workspace. If you try to run the external service wizard and select
the resource adapter from connector project A, everything will function
as usual. However, if you then try to run the external service wizard
again, this time choosing connector project B, you will receive an
error message similar to the following, where the name of the resource
adapter and library name would differ for your situation, when you
attempt to connect to the Enterprise Information System (EIS):
The
resource adapter named 'JDBC EMD Adapter' returned the following error:
'Failure in connection to EIS java.lang.UnsatisfiedLinkError: db2jdbc
(Library is already loaded in another ClassLoader)'
This error
occurs because of a Java™ Virtual
Machine (JVM) limitation. Each JVM allows only one class loader to
load a native library at a time. Each connector project has its own
class loader to load the classes that the connector provides. Therefore,
only the first connector project can load the native library until
that library is released.
To use the second resource adapter
instance, you need to exit IBM Integration
Designer,
and then restart it.
- Importing a C struct with an anonymous struct declaration requires
a modification.When you import a data structure to create a business
object, note that the C importer does not correctly handle anonymous
structure declarations, such as in the following code:typedef struct {
	char loanId[20];
	double loanAmount;
	char date[20];
	struct {
		char taxPayerId[10];
		char firstname[20];
		char lastname[20];
		char email[50];
	} Customer[1];
} LoanInfo;

To enable the code to import correctly, modify
the declaration to put the anonymous structure declaration outside
the main structure declaration as a named structure.
The following
declaration is equivalent to the previous code but will import correctly:typedef struct {
	char taxPayerId[10];
	char firstname[20];
	char lastname[20];
	char email[50];
} Taxpayer;

typedef struct {
	char loanId[20];
	double loanAmount;
	char date[20];
	Taxpayer Customer[1];
} LoanInfo;

## Connections

For CICS® and IMS, you can statically set values on the connectionSpec
and interactionSpec properties. You cannot dynamically (programmatically)
set or get their values.

## Languages

C, COBOL and
PL/I

For a C union, PL/I union, COBOL REDEFINE, or a sparsely
populated commarea, all of the data is converted on a best effort
basis. A commarea is used to pass data between transactions, however,
the commarea is not necessarily filled in a transaction leading to
a sparsely populated commarea which may contain old or unusable data.
If any errors are encountered while trying to convert the data from
the C, COBOL, or PL/I program, they are ignored, and data conversion
continues until finished. It is up to the application program to examine
the returned data to ensure that it is valid. For example, for a union
or REDEFINE, an attempt will be made to convert all views of the data,
so results may exist for views which are not valid. Your application
program must determine which views are valid.

## JMS bindings

- If you select text for how the data will be serialized between
the business object and the JMS message, your wrapped data objects
must be a complex type; they cannot be a simple type.
- In the JMS destination properties, if you specify nothing in the
queue name or topic space field, a default value will be created.
If you specify a queue name or a topic space, this value will remain
even if you then clear the field. The only way to change the value
is to specify a different value.

## WebSphere Business
Integration adapters

The WSDL file generated when working
with a WebSphere® Business
Integration adapter cannot be used in a web service call because the
WSDL file contains import statements that do not have valid schemaLocations,
which is required by WebSphere web
services.

## WOLA Resource Adapter

<!-- image -->

The RAR file used while generating the WOLA import and
external service is not supported when embedded in the application.
For installing it on the server, follow the steps in the topic Enabling the server environment to use optimized
local adapters. The minimum version of the RAR file used should
be version 2 from WebSphere Application Server
for z/OS® 8.0.0.3.

## WebSphere runtime
environment variables

WebSphere runtime
environment variables are useful in situations where you have multiple
modules using the same adapter. By using a variable such as FTP\_SERVER\_DIR
when creating your import or export, you would only need to add extensions
like FTP\_SERVER\_DIR/customer and FTP\_SERVER\_DIR/invoice at deployment
or post-deployment time to identify the directories your service wants
to use on the FTP server. You can enter these variable names when
using the external service wizard to create a service and they will
be passed on to the runtime.

## Bidirectional support

Only
ASCII characters are supported for Java Naming
and Directory Interface (JNDI) names at run time.

## Generated interfaces

An
interface generated by the external service wizard cannot be shared
in a library, as the interface requires other files not contained
in a library.

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
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