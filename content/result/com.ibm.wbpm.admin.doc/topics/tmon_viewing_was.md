<!-- image -->

# Viewing and interpreting service component event log files

Events fired to the logger by service component monitoring are encoded in Common Base Event
format. When published to a log file, the event is included as a single, lengthy line of text in XML
tagging format, which also includes several logger-specific fields. Consult the event catalog
section of this documentation for details on deciphering the Common Base Event coding of the logged
event. Use this section to understand the other fields contained in each entry of the log file, and
how the format you chose for the log file when you configured the logger is structured.

## Basic and advanced format fields

## Basic format

Trace events displayed in basic format use the following format:

```
<timestamp><threadId><shortName><eventType>[className][methodName]<textmessage>
               [parameter 1]
               [parameter 2]
```

## Advanced format

Trace events displayed in advanced format use the following format:

```
<timestamp><threadId><eventType><UOW><source=longName>[className][methodName]
<Organization><Product><Component>[thread=threadName]
<textMessage>[parameter 1=parameterValue][parameter 2=parameterValue]
```

## Log analyzer format

Specifying the log analyzer format allows you to open trace output using the Log Analyzer tool,
which is an application included with WebSphere® Application
Server.
This is useful if you are trying to correlate traces from two different server processes, because it
allows you to use the merge capability of the Log Analyzer.