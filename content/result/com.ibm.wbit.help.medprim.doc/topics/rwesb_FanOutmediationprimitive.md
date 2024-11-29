# Fan Out mediation primitive

## Introduction

You can use the Fan Out mediation
primitive to iterate through an input message that contains a repeating
element, and store each instance of the repeating element in the service
message object (SMO) context. The Fan Out mediation primitive does
not change the body of the input message.

- Default mode sends the entire input message once.
- Iterate mode lets you iterate through a single input message that
contains a repeating element. Every occurrence in the repeating element,
which you specify using an XPath, is processed.

The Fan Out mediation primitive has one input terminal
(in), two output terminals (out and noOccurrences),
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message.

If an exception occurs during the processing
of the input message, the fail terminal propagates
the input message, together with any exception information.

In
default mode, the out terminal is used to propagate
the input message and the terminal is fired only once. In iterate
mode, the out terminal is also used to propagate
the input message, but the terminal is fired once for each occurrence
of the repeating element. Each time the terminal is fired the value
of the current element is placed in the FanOutContext.
The noOccurrences terminal is only used in
iterate mode, and is used if the input message does not contain any
occurrences in the repeating element.

## Details

When in iterate mode the out terminal
is fired once for each occurrence of the repeating element that you
specify, using an XPath expression. Each occurrence of the repeating
element is stored in a FanOutContext field.

If
you use a Fan Out mediation primitive followed by a Fan In mediation
primitive, you can aggregate the responses from two or more service
invocations; the group of mediation primitives that occur between
a Fan Out and a Fan In is called an aggregation block.
If an aggregation block contains Service Invoke mediation primitives
on multiple branches, and the Service Invoke primitives are configured
for asynchronous invocation, the service calls are processed in parallel.
The parallel processing occurs in the following way: there is only
one thread, but that thread makes all the service calls and then checks
for the responses. You can configure when the responses are checked,
using the Batch Count property.

## Usage

You can use the Fan Out and Fan In
mediation primitives to aggregate the responses from two service invocations
into one output message. For example, you could retrieve a customer
credit score from two credit agencies, then average the two scores.

The
shared context area of the SMO is for storing aggregation data between
a Fan Out primitive and a Fan In primitive. The shared context is
a thread-based storage area that is shared in the same thread. The
content of the shared context business object does not persist across
a request flow and a response flow, through callout invocation. Whatever
data is in the shared context of the request flow cannot be reused
during the response flow. Therefore, you can only aggregate in a particular
flow: a Fan In mediation primitive in a response flow cannot be used
to aggregate messages from a Fan Out mediation primitive in a request
flow.

Like the transient and correlation context, the shared
context is defined as a user-provided business object on the input
node of the mediation flow. After you have defined the shared context
you can use it to store data during aggregation operations. You need
to design the shared context business object carefully, to ensure
it is suitable for all aggregation scenarios in a specific flow.

The
Fan In primitive allows for the aggregation of data that results from
the use of a Fan Out primitive. You can aggregate data by processing
the shared context, using transformations or mappings in other mediation
primitives.

## Example of data aggregation

Figure 1. Figure 1. Aggregating
data using Fan Out, Mapping, Service Invoke and Fan In mediation primitives. In this case the Mapping primitives have all been configured
to use the XSLT engine. The Fan Out mediation primitive is wired to
two Mapping mediation primitives. Each Mapping mediation primitive
is wired to a different Service Invoke mediation primitive, which
calls a service. The Service Invoke mediation primitives are wired
to different Mapping mediation primitives, and these are both wired
to one Fan In mediation primitive. The Fan In waits until both service
invocations have been completed before firing a final Mapping mediation
primitive.

<!-- image -->

1. FanOut1 fires the input terminal of XSLT1.
2. XSLT1 creates the appropriate request message
for Service A, and fires the input terminal of ServiceInvoke1.
3. ServiceInvoke1 calls Service A,
and fires the input terminal of XSLT3.
4. XSLT3 maps the response from Service
A into the shared context and fires the input terminal of FanIn1,
for the first time.
5. Because the FanIn1 count value has not been reached
the mediation flow tracks back to the flow path split, at FanOut1.
6. FanOut1 fires the input terminal of XSLT2.
7. XSLT2 creates the appropriate request message
for Service B, and fires the input terminal of ServiceInvoke2.
8. ServiceInvoke2 calls Service B,
and fires the input terminal of XSLT4.
9. XSLT4 maps the response from Service
B into the shared context and fires the input terminal of FanIn1 for
the second time.
10. The FanIn1 decision point is now met (the count
value has been reached). Therefore, the FanIn1 primitive
fires the input terminal of XSLT5.
11. XSLT5 uses the shared context to create a new
message body in the SMO.

- Fan Out mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)