# Error when sending event (message CEIEM0034E)

## Cause

This problem indicates that the JMS
transmission configuration being used by the emitter specifies one
or more JMS resources that are not defined in the JMS configuration.

## Remedy

1. In the administrative console, click Service integration > Common
Event Infrastructure > Event emitter factories > emitter\_factory > JMS
transmission settings. Make sure you are viewing the JMS transmission
for the emitter factory used by your event source application.
2. Check the values specified for the Queue JNDI name and Queue
connection factory JNDI name properties. Make sure the specified
JNDI names exist in the JNDI namespace and are valid JMS objects.
If necessary, modify these properties or create the required JMS resources.