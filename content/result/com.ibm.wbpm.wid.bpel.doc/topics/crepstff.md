<!-- image -->

# Replacement variables and context variables

- staff queries of tasks
- staff queries of escalations
- in the description and documentation of tasks
- in the description and documentation of escalations
- in notification emails sent by escalations.
- durations of tasks
- priority of tasks
- the type property (business category) of tasks
- custom properties of tasks
- durations of escalations
- custom properties of escalations

## Use of replacement variables

Context variables
might only be available during specific periods of an instance's lifecycle
 (a task owner is only defined once the task has been claimed) and
can resolve either to single or multiple values. Multiple values are
returned in a string array (which is represented as a comma separated
list when used in an email) .

- Using percent signs within variable names is not allowed.
- If you want to use a percent sign in a string within the replacement
variable, then you will need to use two percent signs (%%)
instead of one.
- Variables can contain XPath expressions. If an XPath expression
contains a % sign, it must be escaped as specified by XML (using &#37;).

The categories shown below contain specific details
on which expressions can be used and when.

- Replacement variables in process and activity descriptions

When used in descriptions for processes and activities, replacement expressions can be used to represent context variables that will be fully resolved at run time.
- Replacement variables in people assignment criteria and task descriptions

When used in descriptions for people assignment criteria and human tasks, replacement variables can be used to represent context variables that will be fully resolved in the runtime environment.
- Replacement variables in staff emails

When used in escalation-based staff emails, replacement variables can be used to represent context variables that will be fully resolved in the runtime environment.
- Replacement variables for escalation duration expressions

The Escalate within value can also be represented by a replacement variable that refers to a variable that will get resolved at run time.

## Related concepts

- Using Java methods in process snippets
- Using custom properties for human tasks
- Using event handlers

## Related tasks

- Modifying the properties of an activity
- Modifying the type of an activity
- Working with basic activities
- Working with structured activities
- Modeling human workflows
- Refactoring and business state machines

## Related reference

- Description tab: business state machine editor