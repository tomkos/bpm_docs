# Trace mediation primitive

## Introduction

You can use the Trace mediation
primitive to develop and debug mediation flows, and to specify trace
messages to be logged to the server logs or to  a file. The trace
messages can contain service message object (SMO) message content
and other information about the mediation flow.

The Trace mediation
primitive has one input terminal (in), one
output terminal (out) and one fail terminal
(fail). The in terminal is wired to accept
a message and the other terminals are wired to propagate a message.
The input message triggers the writing of a trace message and if the
tracing is successful, the out terminal propagates the original message.
If an exception occurs during the processing of the input message,
the fail terminal propagates the original message, together with any
exception information.

## Usage

You can use the Trace mediation primitive
to write your own trace messages to help with developing and debugging
mediation flows.

You can use the Destination property to determine
where a trace message is written to: either the server system logs,
the User Trace log file, or to a specified file.

- {0} is substituted with the Time Stamp value.
- {1} is substituted with the SMO Message ID value.
- {2} is substituted with the Mediation Name value.
- {3} is substituted with the Module Name value.
- {4} is substituted with the SMO part defined by the Root property
XPath. By default this is the entire SMO.
- {5} is substituted with the SMO Version value.

```
29/04/09 15:11, 9A85B1D2-0119-4000-E000-13E4091443BC, Trace1, MyModule, 
		<?xml version="1.0" encoding="UTF-8"?><smo>...</smo>, 6
```

You
can use the Enabled property to determine whether the Trace primitive
is mediated and is promotable, so that tracing can be switched off
at run time.

- Trace mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)