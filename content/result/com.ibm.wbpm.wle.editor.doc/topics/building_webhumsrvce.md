# Building a client-side human service

## About this task

In the client-side human service diagram, you use coaches, which are web-based forms that provide
data to users and collect input from the users. To create the coaches, you can add views such as
text fields, drop-down menus, and buttons.

In the creation wizard, you can specify whether you want the new client-side human service to be
used on multiple device types. When you create a client-side human service that is intended for use
on multiple devices, only responsive views will be used for all the new pages and page content that
are added to that client-side human service. You can also specify how you want to use the new
client-side human service, whether you want it to be a nested service or a root service that
includes other nested services.

For information about data validation practices in client-side human services, see the topic
Validating data in client-side human services.

To build the client-side human service:

## Procedure

1. Open the appropriate process application.
2 Click the plus sign next to User Interface and, underNew , select Client-Side Human Service . Complete thewizard.
    1 Use Intended for use on multiple devices to specify whether you want thenew service to be used on multiple device types.
        - Select Intended for use on multiple devices to use responsive views for
all the new coaches and coach content that is added to the client-side human service.
        - Clear Intended for use on multiple devices to use deprecated coach views
for the new coaches and coach content if a dependency to the Coaches toolkit already exists in the
toolkit list.
2 Select Use as a nested service to create a nested client-side humanservice that can be reused in other client-side human services. Clear Use as a nestedservice to create a root client-side human service, which is a top-level, stand-aloneservice that can contain one or more nested services. See Client-side human services . The new client-side human service opens in the web editor in the form of a diagram thatincludes a start node, a coach, and an end node. The page in the diagram might have a button thatprovides the boundary event that you can use to wire the coach to the end node. You can use thedefault button or you can replace it.
    - Nested client-side human services can be reused in one or multiple other client-side human
services, either root or nested, but cannot be used for a task or instance user interface
directly.
    - Root client-side human services can be used for tasks, cases, or dashboards, cannot be nested,
but can contain one or more single- or multi-layered nested services.Restriction: To avoid unexpected
behavior at run time, do not use a circular nesting pattern when you model your client-side human
services. For example, if your model includes a client-side human service A
that nests a client-side human service B, do not configure
B to circle back and nest A.
3. Optional: 
You can revisit the usage selections that you made in the wizard in the
Overview properties.
4. In the Diagram view, add more elements and wire them together to build the
client-side human service.
5. In the Variables view, add input, output, and private variables to support
your client-side human service flow.
6. In the view for the coach, create the user interfaces to be used in the client-side human
service.
7. Click Save or Finish Editing.
8. To run the client-side human service in the web browser,
click Run .
9. If errors occur during the client-side human service execution,
click Debug  to review the code and
make the necessary corrections.
10. Iterate through steps 5 to 8 until the client-side human
service flows correctly.
11. To use the client-side human service outside of the business process (for example, as a page in
Process Portal), set the usage settings in the Overview properties.

You can use the client-side human service as a dashboard in Process Portal. For more information, see Defining usage settings for client-side human services.