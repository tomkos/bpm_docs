# Migrating mediation flows to service flows

This document provides a step-by-step guide to migrate a mediation flow to a service
flow, specifically focusing on a use case involving filter, routing, transformation, and fault
handling mediation primitives.

Figure 1. Assembly diagram

<!-- image -->

Figure 2. Existing mediation flow request

<!-- image -->

Figure 3. Existing
mediation flow response

<!-- image -->

To migrate this mediation flow to a service flow, complete the following procedure:

## Create an external service in IBM Process Designer:

1. Complete the steps described in the
procedure to invoke a REST service.
2. Under the Binding tab, specify the hostname and
port number.

## Create a service flow

1. Beside Services in the library navigation, click the
+ sign, and select Service Flow.
2. Specify a name for the service flow, and click Finish.A service flow
editor opens.
3. Go to the Diagram tab, and add a Service task from
the Activity tool in the right panel, between the Start Event and the End
Event in the diagram.
4. Double-click the service task and name it GetBusinessLoans.
5 Select Implementation . Under theImplementation tab:
    1. Choose the LoanApplications external service from the list.
    2. Choose the operation /loan/businessloans GET from the list of
Operations.
    3. Select Data Mapping.. For Input Mapping, click the magic wand icon  and select the Input check
box.
    4. Repeat the previous step for Output Mapping.
6. Add two more service tasks: GetPersonalLoans and
Getallapplications, and repeat step 5 by choosing respectively /loan/personalLoans GET and
/loan/GET.
7. Drag and drop Exclusive Gateway from the right panel to the service flow
editor to add a condition for routing.
8. Add the connections from the Exclusive Gateway to the Service tasks as shown on the following
image:
9 Double click Exclusive Gateway , and under theDecisions tab, set the conditions as follows: The following image shows how conditions were set in IBM IntegrationDesigner using the Message Filter mediation primitive: Similarly, those conditions can be provided in Workflow Process Service , using theExclusive Gateway . The service flow is now created.

<!-- image -->

1. To GetPersonalLoans and To GetBusinessLoans: click
 and set the amount.
2. Default Flow: To End Event.

<!-- image -->

Similarly, those conditions can be provided in Workflow Process Service, using the
Exclusive Gateway.

The service flow is now created.

10. Click the Run icon  to run the service
flow, and click the Debug icon to debug.
11. Under the Variables tab, expand Input, and select
amount. Select the Has default check box, and  enter a
value in the amount field.
12. Test the service flow.

## Known limitations when migrating mediation flows to services flows

- Custom Java code cannot be used in service flows in the same way as it is used in mediation
flows.
- There are no explicit components for (transformation) mapping in service flows.
- Service flows do not provide separate diagrams for request, response and error handling.
- There are fewer components in service flows than in mediation flows.