<!-- image -->

# Retrying alternate endpoints of the same service

## Before you begin

## About this task

## Procedure

1. Create a mediation flow and add all necessary primitives
along with creating interfaces and references as needed. Then add
the Endpoint Lookup primitive  to the
canvas and wire it to a Service Invoke or Callout.
2. To enable retrying of alternate endpoints of the same service
you have to set the properties of the Endpoint Lookup primitive as
well as those of the Service Invoke primitive.
3 For the Endpoint Lookup primitive:
    1. Right click it and select Show in Properties, then click
Details. The details view is presented to you.
    2. To populate the Name and Namespace of the Port Type
(also called interface) click Browse. In the
Interface Selection window, choose an interface and click OK.
    3. Type in a registry name or leave <Use default registry>
to use the default WSRR.
    4. The Match policy dictates the type of search to be done.
Set it to "Return all matching endpoints" to try all alternate endpoints
available.
4 For the Service Invoke:

1. Set the Retry on property to "Any Fault."
2. Set the Retry count property to any number greater than
0.
5. If any fault is returned by the initial service request,
the first endpoint in the list populated by the Endpoint Lookup primitive
is used. Subsequent retry attempts use the other endpoints in the
list, in the order they appear.