# Hiding frequent logging of error messages

## About this task

When tracking is enabled for BPD (Business Process Definition)
variables that have no default value, CWLLG2041E exceptions are written
to the logs. Frequent logging of these error messages can eventually
cause system logs to overwrite each other, causing the loss of valuable
tracing that might help in identifying other issues.

```
E   CWLLG2041E:  TeamWorksJavaScriptException created
non-nested.   Error: [TeamworksException name='TypeError',
message='TypeError: Cannot read property "subBusinessObject"
from undefined (<JSScript&gt;#1)', line=1, pos=0 nested=<none&gt;]
                                 [TeamworksException
name='TypeError', message='TypeError: Cannot read property
"subBusinessObject" from undefined (<JSScript&gt;#1)', line=1,
pos=0 nested=<none&gt;]
         at
com.lombardisoftware.core.script.js.JavaScriptRunner.execute(Jav
aScriptRunner.java:270)
         at
com.lombardisoftware.core.script.js.JavaScriptRunner.evalExpress
ion(JavaScriptRunner.java:367)
         at
com.lombardisoftware.core.script.js.JavaScriptRunner.evalExpress
ion(JavaScriptRunner.java:355)
         at
com.lombardisoftware.bpd.runtime.engine.BPDExecutionTreeNode.eva
luateExpression(BPDExecutionTreeNode.java:689)
...
```

- When this property is set to false, the default
behavior is used. Exceptions are written to the log as SEVERE.
- When this property is set to true, this default
behavior is disabled. Instead, exceptions are written to the log only
if the logging level is set to FINE. Because the default logging level
is INFO, these FINE logged exceptions should not appear in the log
files.

To add the log-tracked-loudly configuration
property to the 100Custom.xml files, complete
the following steps.

## Procedure

1. Stop the server for Workflow Server or Workflow Center.
2. Open the 100Custom.xml files. For
information about the individual 100Custom.xml files
that must be updated and their locations, see the topic Location of 100Custom configuration files.
3. Add the following entry to the 100Custom.xml files
under the <properties> tag: <common>
<log-tracked-loudly merge="replace">true</log-tracked-loudly>
</common>
4. Save your changes in the 100Custom.xml files.
5. Open the 100Custom.xml files in a
browser to make sure that they contain no special characters.
6. In a clustered environment, make sure that the changes
are carried to the nodes by doing a force synchronize and restarting
the deployment environment.
7. In a stand-alone server environment, restart the server.