# Fan In mediation primitive

## Introduction

You can use the Fan In mediation
primitive to combine multiple messages, which you create using the
Fan Out mediation primitive.

- Simple count. When a set number of messages are received at the
input terminal, the Fan In mediation primitive fires the output terminal.
The firing of the Fan In output terminal does not stop the Fan Out
mediation primitive from sending messages. Therefore, the decision
point might be reached more than once, resulting in multiple firings
of the output terminal.
- XPath decision. If an XPath evaluation of the input message evaluates
to true, the Fan In mediation primitive fires the output terminal.
- Iterate. The Fan In mediation primitive waits to receive all of
the messages produced by the corresponding Fan Out mediation primitive,
and then fires the output terminal.

The Fan In mediation primitive has two input terminals
(in and stop), two output
terminals (out and incomplete)
and a fail terminal (fail). The input terminals
are wired to accept a message and the other terminals are wired to
propagate a message.

If an exception occurs during the processing
of the input message, the fail terminal propagates
the input message, together with any exception information.

The in terminal
accepts input messages until a decision point is reached. When a decision
point is reached the out terminal is fired.
Although the out terminal is fired when a decision
point is reached, the in terminal can still
accept input messages, under some circumstances. For example, if the
count value is reached, the out terminal is
fired. However, if the Fan Out mediation primitive is still sending
messages, the Fan In  mediation primitive can still receive messages.

You
can stop a Fan In operation by wiring the preceding mediation primitive
to the Fan In stop terminal. The stop terminal
causes the incomplete output terminal to be
fired, and this stops the associated Fan Out mediation primitive from
sending any more messages. The incomplete output
terminal is also fired if a timeout occurs.

## Details

When the out terminal
of the Fan In mediation primitive is fired it propagates the last
message received on its in terminal. The shared
context is also propagated; it is the shared context area of the service
message object (SMO) that enables the aggregation facility. However,
in order to aggregate data, you must transform, or map, the information
in the message and shared context into a form appropriate for the
flow downstream of the Fan In mediation primitive. Equally, you might
need to transform, or map, information from the shared context after
the Fan Out mediation primitive before wiring paths to the in terminal
of the Fan In mediation primitive.

The Fan In mediation primitive
can only be used in combination with the Fan Out mediation primitive
and, therefore, it must always have an associated Fan Out mediation
primitive. WebSphere® Integration
Designer allows you to select which Fan Out mediation primitive to
associate with each Fan In mediation primitive, and displays the associated
Fan Out mediation primitive next to the details of the Fan In properties.

## Usage

The Fan In mediation primitive lets
you wait until certain conditions are met, before processing information
created previously in the mediation flow. In this way, the Fan In
mediation primitive lets you create various decision points (based
upon counts, XPath evaluations and iterations). It does not change
the input message in any way.

After the Fan In mediation primitive
you might want to transform, or map, information from the shared context
into the body of the message (the SMO /body). Alternatively,
you might want to augment the existing type of the message, with aggregated
information. To do this you must use another mediation primitive after
the Fan In mediation primitive. For example, you might use a Mapping
mediation primitive to map information from the shared context into
another part of the message.

You can use the Fan Out and Fan
In mediation primitives to aggregate (combine) the responses from
two service invocations into one output message. For example, you
can retrieve a customer credit score from two credit agencies, then
average the two scores.

The shared context
area of the SMO is a global storage area you can use to aggregate
data. The shared context is a thread-based storage area: it is shared
by all SMOs that are created for a particular thread. However, the
shared context business object does not persist across a request and
response flow, through callout invocation; whatever data is in the
shared context of the request flow cannot be reused during the response
flow.

Like the transient and correlation context, the shared
context is defined as a user-provided business object on the input
node of the mediation flow. After you have defined the shared context
you can use it to store data during aggregation operations. You need
to design the shared context business object carefully, to ensure
it is suitable for all aggregation scenarios in a specific flow.

You
can stop a Fan In operation by wiring a preceding mediation primitive
to the stop input terminal; for example, if
a Service Invocation between the Fan Out and Fan In mediation primitives
fails. This will cause the incomplete terminal to be fired, and will
stop the corresponding Fan Out mediation primitive from firing any
more messages.

## Example of data aggregation

Figure 1. Aggregating data using
Fan Out, Mapping, Service Invoke and Fan In mediation primitives

<!-- image -->

1. FanOut1 fires the input terminal of the
Mapping mediation primitive named XSLT1.
2. XSLT1 creates the appropriate request message
for Service A, and fires the input terminal of ServiceInvoke1.
3. ServiceInvoke1 calls Service A,
and fires the input terminal of the Mapping mediation primitive named XSLT3.
4. XSLT3 maps the response from Service
A into the shared context and fires the input terminal of FanIn1,
for the first time.
5. Because the FanIn1 count value has not been reached
the mediation flow tracks back to the flow path split, at FanOut1.
6. FanOut1 fires the input terminal of the
Mapping mediation primitive named XSLT2.
7. XSLT2 creates the appropriate request message
for Service B, and fires the input terminal of ServiceInvoke2.
8. ServiceInvoke2 calls Service B,
and fires the input terminal of the Mapping mediation primitive named XSLT4.
9. XSLT4 maps the response from Service
B into the shared context and fires the input terminal of FanIn1 for
the second time.
10. The FanIn1 decision point is now met (the count
value has been reached). Therefore, the FanIn1 primitive
fires the input terminal of the Mapping mediation primitive named XSLT5.
11. XSLT5 uses the shared context to create a new
message body in the SMO.

- Fan In mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)