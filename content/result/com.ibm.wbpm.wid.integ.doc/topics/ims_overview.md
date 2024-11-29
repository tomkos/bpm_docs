<!-- image -->

# IMS TM resource adapter

With the IMS TM resource adapter,
you can build import components that run IMS transactions
by using the SCA/SDO programming model.  You can also create imports
to retrieve undelivered IMS transaction
output. The aspects you must be familiar with conceptually are how
to develop the IMS import with
the external service wizard and the relationship of that import with
the IMS TM resource adapter at
run time.

## Developing the IMS import

An import is a way of letting
an application developed in IBM® Integration
Designer access
enterprise information systems. Creating the import involves providing
your IMS server security and
connection information and specifying an existing COBOL, C, or PL/I
program that you want to invoke on the IMS server.

An IBM Integration
Designer application
that uses the import invokes the transaction on the IMS host system; that is, the IBM Integration
Designer application
initiates the action.

In addition to building import components,
you can also create J2C Java™ code
that accesses an IMS transaction
by using the Java EE perspective and the J2C JavaBean programming
model.

## Relationship of the IMS import and the IMS TM
resource adapter runtime component

Your IMS import is within a module that contains your
application. At run time, when the application is invoked, it triggers
the IMS TM resource adapter deployed
on the IBM Workflow
Server to
access and communicate with IMS transactions.

<!-- image -->

## Additional information

For more information, see IBM Information Management System
(IMS).