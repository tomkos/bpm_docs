# Detecting and ending infinite loops in JavaScript activities

When infinite loops occur in JavaScript code, this affects other resources. For example,
workflow server threads are lost until the server is stopped, which impacts server availability. To
detect infinite loops, Business Automation Workflow monitors the number of
executed JavaScript instructions in each script activity. It sets an instruction threshold and a
timeout to check the duration of the script activity. When the instruction threshold is reached, the
JavaScript engine invokes a callback provided by Business Automation Workflow that checks whether the
script duration exceeded the configured timeout. If it exceeded the timeout, Business Automation Workflow either throws a
loop-detection-exception or logs an error message, depending on the
configuration. The default value of the instruction threshold is 250,000 JavaScript instructions.

- Calls to Java methods or workflow JavaScript API calls, such as
tw.system.executeServiceByName, count as one instruction.
- JavaScript code within managed server-side files that are referenced
by server-side components count as individual instructions, not just
one instruction.

Using the following loop detection parameters,
you can configure the timeout and the instruction threshold at which Business Automation Workflow provides
the callback. If the script duration exceeds the timeout, you can
choose to stop the script.

- loop-detection-duration: If the timeout value
specified by the loop-detection-duration parameter
is exceeded, it is assumed that the activity is in an endless loop.
The default duration is set to 20 seconds, but it is configurable
(see the following example).
- loop-detection-exception : By default, whenan endless loop is detected, the Business Automation Workflow enginewrites a warning to the SystemOut.log file, butthe script activity continues. To configure the Business Automation Workflow engineto stop infinitely looping script activities, set the loop-detection-exception parameterto true . If the loop-detection-exception parameteris set to false , one of the following messages iswritten to the SystemOut.log file: If the loop-detection-exception parameteris set to true , one of the following messages iswritten to the SystemOut.log file:
    - CWLLG2261W: Infinite loop suspected after {0} seconds
in ''UKNOWN'' activity. If this script is not in a loop, increase
the loop-detection-duration property.
    - CWLLG2263W: Infinite loop suspected after {0} seconds
in ''{1}'', for BPD ''{2}'', script activity ''{3}''. If this script
is not in a loop, increase the loop-detection-duration property.
    - CWLLG2265W: Infinite loop suspected after {0} seconds
in service ''{1}''. If this service is not in a loop, increase the
loop-detection-duration property
    - CWLLG2262E: Infinite loop detected after {0} seconds,
''UKNOWN'' activity terminated. If this script is not in a loop, increase
the loop-detection-duration property.
    - CWLLG2264E: Infinite loop detected after {0} seconds in
''{1}'', for BPD ''{2}'', script activity ''{3}'' terminated. If this
script is not in a loop, increase the loop-detection-duration property.
    - CWLLG2266E: Infinite loop detected after {0} seconds,
service ''{1}'' terminated. If this service is not in a loop, increase
the loop-detection-duration property.
- instruction-threshold: When JavaScript code makes Java calls in a loop and
most of the execution time is spent inside the Java code, detecting an infinite loop might take
longer than what is optimal. The default threshold of 250,000 JavaScript instructions could take
much longer than the configured timeout and the script could remain uninterrupted for a long time.
For example, a loop in a JAR file's code path prevents it from returning to the Business Automation Workflow engine for processing, which prolongs the
duration of the JavaScript activity. Using the instruction-threshold property,
you can specify a smaller number of JavaScript instructions between the calls to the callback for
earlier loop detection.Business Automation Workflow multiplies
the configured value by 1000 before it instructs the JavaScript engine to call the loop-detection
callback. The default value is 250. This means that the JavaScript engine calls the Business Automation Workflow loop detection callback every 250,000 JavaScript
instructions.

```
<common merge="mergeChildren">                                       
  <javascript-engine>                                                
    <loop-detection-duration merge="replace">90</loop-detection-duration>            
    <loop-detection-exception merge="replace">true</loop-detection-exception>
    <instruction-threshold merge="replace">250</instruction-threshold>        
  </javascript-engine>                                               
</common>
```