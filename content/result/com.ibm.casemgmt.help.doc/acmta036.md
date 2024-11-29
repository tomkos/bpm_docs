# Troubleshooting business rule errors

## Symptoms

## Resolving the problem

1. Determine which business rules are the source of the problem by checking the workflow deployment
log in Case Builder.
Alternatively, you can validate each case type. For more details about the errors, see the Content Platform Engine server logs.
2. Open each of the problematic business rules in the rules designer
in Case Builder and fix any
errors that are listed.

To troubleshoot any errors that might be due to business rules
when you run IBM Business Automation
Workflow,
check the messages in the Content Platform Engine server
logs. You can view all information and trace messages from the rule
operations component in the Content Platform Engine trace
log file (pesvr\_trace.log) if the TRACE\_CM trace
option is enabled for Content Platform Engine.
For information about configuring the Content Platform Engine trace log file options,
see the trace topic in the IBM
FileNet® P8 documentation.