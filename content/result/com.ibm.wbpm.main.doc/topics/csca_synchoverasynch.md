<!-- image -->

# Synchronous-over-asynchronous invocation

When synchronous-over-asynchronous invocation is detected at run time, the Service Component
Architecture (SCA) automatically changes the synchronous call to an asynchronous call, which creates
a new transaction boundary and can cause one or more of the following problems:

- Lack of transaction propagation
- Multiple retries that result in multiple invocations of the same service
- Time outs when the default wait time for invocations is exceeded
- Blocked threads and thread pool depletion, which are caused when a thread is allocated for each
asynchronous call and waits for a response

Most synchronous-over-asynchronous invocations occur when you have a component that synchronously
calls one of the following components that typically have asynchronous implementations:

- Long-running BPEL and BPMN business processes
- Human tasks
- JMS imports
- MQ imports
- Java POJO components that implement the ServiceAsynchImpl interface

For example, a web service export always performs a synchronous call. If an export synchronously
calls a long-running BPEL process, a synchronous-over-asynchronous invocation occurs. Similarly, a
microflow always performs a synchronous call for a request-response operation. If a microflow
invokes an MQ import for a request-response operation, a synchronous-over-asynchronous invocation
occurs.

In general, avoid the following scenarios that might result in a synchronous-over-asynchronous
invocation:

- A web services export calling a long-running BPEL or BPMN business process
- A web services export calling a message-binding import, such as an MQ or JMS import
- A BPEL microflow calling a long-running BPEL or BPMN process for a request-response
operation
- A BPEL microflow calling a message-binding import (such as an MQ or JMS import) for a
request-response operation

When a synchronous-over-asynchronous invocation is detected, the following warning message is
displayed in the SystemOut.log file:

```
000000ac Core          W   CWSCA2011W: Service Component Architecture (SCA) is switching a synchronous call to an asynchronous call.
Request will be sent in a new local transaction. Default timeout is 115000 milliseconds.
```

Depending on your specific application scenario, there are several approaches to avoiding a
synchronous-over-asynchronous invocation. For example, if you have a microflow that invokes a
long-running BPEL process over MQ for a request-response operation, you might want to incorporate a
briefly persisted process to avoid a synchronous-over-asynchronous invocation.

For general information about invocation styles, see the Invocation styles topic.