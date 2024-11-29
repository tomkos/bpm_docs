<!-- image -->

# CICS ECI resource adapter

The aspects you must be familiar with conceptually are how to develop
the CICS import with the external
service wizard and the relationship of that import with the CICS adapter at run time.

- Developing the CICS import
- Relationship of the CICS import with the CICS adapter at run time
- Additional information about CICS

## Developing the CICS import

An import is a way of
letting an application developed in IBM® Integration
Designer invoke
a transaction on a CICS server.
Creating the import involves using the external service wizard, which
generates the import for you after you follow a sequence of steps.
In these steps, you specify configuration information such as the
RAR file to be used, the host name of the server, the userid and password,
and so on. You then import a COBOL file of the program you want to
invoke on the CICS server.
Following another set of steps, the external service wizard generates
the completed service for you.

Your CICS import results in outbound processing at
run time. Outbound processing means that the IBM Integration
Designer application
using the import invokes the transaction on the CICS server; that is, the IBM Integration
Designer application
initiates the action.

<!-- image -->

## Relationship of the CICS import with the CICS adapter at run time

Your import
is within a module containing your application. At run time when the CICS transaction needs to be invoked,
the CICS adapter is used to
invoke the COBOL program on the CICS server.

<!-- image -->

In more detail at run time, your application uses the
import and then the CICS adapter
to invoke the CICS transaction
at the CICS server. The resulting
data is passed back to the application.

<!-- image -->

## Additional information about CICS

Several sources of documentation, such as IBM
Documentation, books, and white papers are available if
you want to know CICS in detail. The Secure and fast CICS transactions will help you understand the relationship
between the CICS transaction gateway and a CICS server.

The
following IBM Redbooks® provide practical, detailed information
on working with the CICS transaction
gateway and CICS servers:

- Java™ Connectors
for CICS: Featuring the Java
EE Connector Architecture
- CICS Transaction
Gateway: The WebSphere® Connector
for CICS
- CICS Transaction
Gateway for z/OS®

Programming information with respect to CICS can be found
in CICS Transaction Gateway Base API
Programming Reference v8.1.0.2.