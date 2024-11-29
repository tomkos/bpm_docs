<!-- image -->

# Limitations for the integration test client

Some known limitations are:

- Null pointer exception (NPE) when testing in Business Process
Choreographer Explorer and Web Services Explorer
- Duplicate names in an XSD not supported in the test client
- The Save Resource window does not contain a Cancel button
- Events for only one node are received when running a business
process on multiple nodes

These limitations are discussed in the following sections.

## Null pointer exception (NPE) when testing in Business
Process Choreographer Explorer and Web Services Explorer

After
testing an application in the integration test client no errors may
be shown; however, when the application is deployed to the server
and tested in the Business Process Choreographer Explorer and the
Web Services Explorer, it can still result in a null pointer exception
(NPE).

The integration test client has different behavior than
the Business Process Choreographer Explorer and the Web Services Explorer.
The test client is used to unit test the components, so by default,
they are sending empty strings for the data for all of the values
that you leave blank.

In comparison, Business Process Choreographer
Explorer and the Web Services Explorer are sending in data only when
you specify it, null or otherwise. Many of your rules or code might
be accessing items that are null or undefined, resulting in errors.

During
the integration test, if you receive a null pointer exception in the
root exception stack, check to see if the data that was passed in
(or received) is a null value.

## Duplicate names in an XSD not supported in the test
client

This limitation is only applicable in cases where
an XSD for a business object is created outside of the business
object editor. (The editor will not allow you to create an XSD that
exposes this limitation.)

The limitation manifests itself when
using the test client to enter values into a business object based
on an XSD that contains duplicate names. When the business object
is created you will notice that all values belonging to elements with
the same name, except for the last one, will be null by the time the
business object is received by an operation.

This limitation
results from the way that business objects are created internally.
Since each property is stored by name, duplicate names are not allowed.

The
solution is to ensure that XSDs created outside of the business object
editor have no duplicate names.

## The Save Resource window does not contain a Cancel
button

When you close the integration test client, a Save
Resource window opens to ask you whether you want to save your changes.
This window only contains a Yes button and
a No button. Regardless of which button you
select, the integration test client will close. Due to a limitation
of the Eclipse framework, the Save Resource window does not contain
a Cancel button that would enable you to cancel
the window and keep the integration test client open.

## Events for only one node are received when running
a business process on multiple nodes

When a single run of
a business process occurs on multiple IBM® Process
Center server nodes, events from only one node might be received by
the test client. Try testing the business process components on an IBM Process Server unit test environment
to verify that the problem is not with the application being tested.
The loss of events in a network deployment environment is a known
limitation.