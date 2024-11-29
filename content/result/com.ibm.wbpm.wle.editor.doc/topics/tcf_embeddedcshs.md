# Reusing client-side human services

## About this task

You can reuse the nested services in other client-side
human services, which can be either top-level, root client-side human
services or other nested client-side human services. Root services
can contain one or more single- or multi-layered nested services.

When you build the service logic for your tasks or instance user interfaces in the designer, you
might want to reuse common steps that are defined in other client-side human services. For example,
creating an insurance claim might include a common set of steps. If you define the steps in a nested
client-side human service, you can reuse them in other client-side human services. At run time, the
nested client-side human service or services run as part of the parent root service.

When you create a client-side human service, you can specify whether it
can be used as a nested service or as a root service. You can revisit the selection that you made in
the Overview properties.

The following procedure describes how to nest
a reusable client-side human service in another client-side human
service. A step-by-step example is also provided.

## Procedure

To nest a reusable client-side human service in another client-side human
service:

1. Open the process application that contains the root client-side human service.
2. Build the nested client-side human service that contains
the common steps that you want to reuse. See Building a client-side human service. In the creation
wizard, select Use as a nested service to ensure
that the client-side human service that you are building is configured
for reuse. To specify that you want to use the new service on multiple
device types, select Intended for use on multiple devices.
After the service is configured as a nested service, its
name becomes available to select in step 6.
3. Open the root client-side human service that you want to work with.
4. In the Diagram view, add the nested client-side human service  and wire it as required in the root service diagram.
5. In the Implementation properties of the nested service node, under
Behavior, specify the client-side human service to be nested. Click
Select to select an existing client-side human service, or click
New to create one. See Building a client-side human service.

Restriction: To avoid unexpected
behavior at run time, do not use a circular nesting pattern when you model your client-side human
services. For example, if your model includes a client-side human service A
that nests a client-side human service B, do not configure
B to circle back and nest A.
6. In the diagram, double-click the nested service node to open the service and edit it as
needed.
7. Optional: 
In the diagram of the root service, use the Data Mapping options to
initialize the variables in the nested service. See Data mapping for nested client-side human services.
8. Click Save or Finish Editing.

- Input and output data mapping in nested client-side human services

You can pass variables between a parent client-side human service and its nested service or services by setting the input and output data mapping. The parent service can be either a root client-side human service or a nested client-side human service that contains other nested client-side human services.
- Example: Reusing a nested client-side human service

This example shows how you can build a nested client-side human service and reuse it in a root client-side human service.