<!-- image -->

# Defaults tab: BPEL process editor

## Process level

- Java™
- This is the default setting for processes that use BPEL extensions,
otherwise XPath 1.0 will be the default . If you choose this, then
you will be able to compose the expressions in the Java programming language using either the visual
snippet editor, or a text editor.

- Simple
- Choose this to always have a user interface prompt you for your
expression choices. For example, when you are required to compose
a condition, you will be able to work with the appropriate fields
and drop down menus.

- XPath 1.0
- Choose this to compose the expressions in the XPath 1.0 programming
language, using either the XPath Expression Builder, or a text editor.

- Yes
- When used on the process as a whole, this setting suppresses
the joinFailure fault for all activities in the process,
skips the activities that throw the fault, and continues with the
running of the process. When used on an individual activity, it overrides
the setting at the process level.

- No
- Use this setting to stop the process if the activity encounters
a fault in one of the incoming links.

- Yes
- When Yes is chosen, and there is no fault handler defined
on the enclosing scope, then the activity is put into the stopped
state, and a work item for the process administrators is created so
that the problem can be repaired. Potentially, this option allows
you to simply pause the process to have the problem fixed. This is
especially useful in a process that has been running for a long time.

- No
- When No is selected, then in the event of a fault during
process execution, the fault is sent to the fault handler of the activity's
enclosing scope. If this is insufficient to deal with the fault, then
it is rethrown to the next enclosing scope. If the fault reaches the
outermost scope, the process will terminate.

## Related concepts

- Correlating BPEL processes

## Related reference

- Correlation tab: BPEL process editor
- Description tab: business state machine editor