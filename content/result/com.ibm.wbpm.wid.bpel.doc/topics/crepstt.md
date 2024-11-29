<!-- image -->

# Replacement variables in process and activity descriptions

```
%[<variableName>]\[<partName>][\<xpath>]%
```

## <variableName>

The name of the variable
is optional in cases where a default message is defined. For example,
the description of an invoke activity uses the invoke's input message
as the default variable.

| Entity                                               | Default Message                      |
|------------------------------------------------------|--------------------------------------|
| Process                                              | The input message of the process     |
| Invoke activity                                      | The input message of the invoke.     |
| Human task activity (embedded inline in the process) | The input message of the human task. |
| Receive activity                                     | The message received                 |
| Pick (Receive choice) activity                       | The message received                 |
| Reply activity                                       | The reply message                    |

For a process instance description, the default variable
is the actual input message that started the process. For processes
with multiple creating activities, the replacement string must be
applicable for all the different types of input messages. In addition,
the process variables are not initialized when the process description
is resolved, meaning that the input message of the process is the
only source that can be used in the replacement strings.

## <partName>

The part name of the expression
can only be specified for interface typed variables.

## <xpath>

Variables can contain XPath expressions.
If an XPath expression contains a "%" sign, it must be escaped as
specified by XML (using &#37;).

It is expected that XPath
will point to objects of type String, or String List. In general,
and object will be replaced by what the toString() method returns.

## Example

```
Waiting for '%user\name%' to return '%book\title%'
```

```
Waiting for 'Anke' to return 'Computer Networks'
```

## Related concepts

- Replacement variables in people assignment criteria and task descriptions
- Replacement variables in staff emails
- Replacement variables for escalation duration expressions