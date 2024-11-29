<!-- image -->

# Function selectors in export bindings

Consider an SCA export that exposes an interface. The
interface contains two operations-Create and Update. The export has
a JMS binding that reads from a queue.

When a message
arrives on the queue, the export is passed the associated data,
but which operation from the export's interface should be invoked
on the wired component? The operation is determined by the function
selector and the export binding configuration.

Figure 1. The function selector

<!-- image -->

If the interface has only one operation, there is no
need to specify a function selector.

Several prepackaged function
selectors are available and are listed in the sections that follow.

## JMS bindings

- JMS bindings
- Generic JMS bindings
- WebSphere MQ JMS bindings

| Function selector                                  | Description                                                                                                         |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| JMS function selector for simple JMS data bindings | Uses the JMSType property of the message to select the operation name.                                              |
| JMS header property function selector              | Returns the value of the JMS String Property, TargetFunctionName, from the header.                                  |
| JMS service gateway function selector              | Determines if the request is a one-way or two-way operation by examining the JMSReplyTo property set by the client. |

## WebSphere MQ bindings

The following table
lists the function selectors that can be used with WebSphere MQ bindings.

| Function selector                              | Description                                                                                                                                 |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| MQ handleMessage function selector             | Returns handleMessage as a value, which is mapped using the export method bindings to the name of an operation on the interface.            |
| MQ uses JMS default function selector          | Reads the native operation from the TargetFunctionName property of the folder of an MQRFH2 header.                                          |
| MQ uses message body format as native function | Finds the Format field of the last header and returns that field as a String.                                                               |
| MQ type function selector                      | Creates a method in your export binding by retrieving a URL containing the Msd, Set, Type and Format properties found in the MQRFH2 header. |
| MQ service gateway function selector           | Uses the MsgType property in the MQMD header to determine the operation name.                                                               |

## HTTP bindings

The following table lists
the function selectors that can be used with HTTP bindings.

| Function selector                                                          | Description                                                                                                                                |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| HTTP function selector based on the TargetFunctionName header              | Uses the TargetFunctionName HTTP header property from the client to determine which operation to invoke at run time from the export.       |
| HTTP function selector based on the URL and HTTP method                    | Uses the relative path from the URL appended with the HTTP method from the client to determine the native operation defined on the export. |
| HTTP service gateway function selector based on URL with an operation name | Determines the method to invoke based on the URL if "operationMode = oneway" has been appended to the request URL.                         |