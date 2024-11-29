<!-- image -->

# A fault is not caught by the fault handler

## Reason

- The name of the fault handler matches the fault name and it has
a fault variable with a data type that matches the type of the data
associated with the fault
- The fault handler does not specify a fault name but it has a fault
variable with a data type that matches the type of the data associated
with the fault
- The catchAll fault handler is specified

## Resolution