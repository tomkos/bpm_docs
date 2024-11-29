# Calling another service

## About this task

To call another service from your service flow, add an activity of Linked Service Flow type to
the diagram, and then specify the service that you want the linked service flow to call. A linked
service flow can call another service flow or a heritage service such as an Ajax,
general system, integration, or advanced integration service.

To
call another service through a linked service flow, complete the following
steps:

## Procedure

1. Open the designer.
2. In the library, click Services and open the service flow that you
want to work with, or create a service flow as described in Creating a service flow.
3. In the Diagram view of the service
flow, click the arrow on the Activity tool , and select Linked Service Flow  to add a linked service
flow node to the canvas. In the service flow diagram, wire the linked
service flow node as required.
4. Select the linked service flow node to open its properties.
In the Implementation tab, click Select next
to Called service to specify the service flow
or heritage service that you want the linked service flow to call.
To create the service flow that you want to call, click New and
complete the wizard.
5. On the Data Mapping tab, set the
input and output mapping for the linked service flow.
6. Click Save or Finish Editing.