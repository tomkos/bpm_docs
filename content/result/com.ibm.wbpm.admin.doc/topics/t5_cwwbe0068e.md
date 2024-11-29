<!-- image -->

# Uninitialized variable or NullPointerException in a Java snippet

## Symptoms

- During the execution of a Java snippet or Java expression, that
reads or manipulate the contents of variables, a NullPointerException
is thrown.
- During the execution of an assign, invoke, reply or throw activity,
the BPEL standard fault "uninitializedVariable"
(message CWWBE0068E) is thrown.

## Reason

All variables in a BPEL process have
the value null when a process is started, the variables are not pre-initialized.
Using an uninitialized variable inside a Java snippet or Java expression
leads to a NullPointerException.

## Resolution

The variable must be initialized
before it is used. This can be done by specifying an initial value
when you define the variable, specifying an assign activity, for example,
the variable needs to occur on the to-spec of an
assign, or the variable can be initialized inside a Java snippet.