<!-- image -->

# Mediation policy usage scenarios

## Lookup from different tables in a database

In this example a message that flows through a IBM® Business Automation Workflow mediation is updated with information from a database. Depending on
the context of the message, information might be required from different database tables and the
system can be expanded later to extract from further tables.

The context for a message can vary with an employee's department, and additional departments can
be created in the future. In the database, data about employees is held in different schemas
depending on the department. For example, there can be ACCOUNTS,
HUMANRESOURCES, WAREHOUSE, and
TRANSPORT schemas. Each of these schemas contains an
EMPLOYEE table and one of the items in that table is the vacation usage of
each employee.

The mediation flow takes a request message, which contains the employee identifier and department
name. The flow then looks up the vacation usage details in the appropriate table, and returns the
number of vacation days used and vacation days remaining for that employee. Because the employee
tables are in different departmental schemas you can use a filter node to check the department value
in the message and then route the message to a database lookup node appropriate to that schema, as
shown in Figure 1.

Figure 1. Flow with separate database lookup mediation primitives

<!-- image -->

Figure 2. Flow with policy resolution and single database lookup mediation primitive

<!-- image -->

If any new departments are created then the only changes required are a new policy attachment and
gate condition, applied in WSRR.

## Log a message depending on the target service

In this example, mediation flows are used to perform common processing on messages for two
different target services. One is a test system and the other is a production system. Any messages
that go to the production system must be logged for regulatory purposes, whereas messages bound for
the test service do not need to be logged.

You can create a separate flow to deal with each target service. However, the same logic is then
reproduced twice and any additional future target service requires a new separate flow to handle it.
It is more flexible to use a service gateway pattern, which can accept messages from different
clients and pass them on to different target services.

You can use an Endpoint Lookup mediation primitive within the service gateway to query WSRR and
find the URL to which to route the client message. The target service information that is stored in
WSRR can also have policies attached to it. In this example the Test target
service has a policy that disables a downstream Message Logger mediation primitive. The
Production target service has a policy that enables a downstream Message
Logger mediation primitive, which ensures that all messages to the production target service are
logged. See Figure 3.

If an additional service is added in the future (for example, a
Development service), that service can be loaded into WSRR. You can attach an
appropriate policy to the new target service. For example, you can add a policy to disable logging.
The Service Gateway mediation primitive can process messages for, and route messages to, the new
target service without modification.

Figure 3. Flow with policy resolution and optional logging

<!-- image -->