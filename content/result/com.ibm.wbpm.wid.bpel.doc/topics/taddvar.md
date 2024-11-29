<!-- image -->

# Adding a variable to a business state machine

## About this task

## Procedure

1. In the tray, click the plus icon () to the
right of Variables.
2. In the Add Variable wizard, browse to the appropriate data
type or business object or click New to create
one.
3. When you are done, the newly created variable will appear
in the tray. You can change the name of the variable by
clicking it and typing a new one.

## Results

1. If you want to rename the variable later, you will have to update
its occurrences in the Java™ and
visual snippets with the new name.
2 Variable names cannot contain the strings \_Input\_ or \_Output\_ orend with the string TimerValue . In addition, the followingnames are reserved:
    - ActState
    - DisplayState
    - NxtState
    - NxtTrans
    - SkipEntry
    - InstanceInitialize
    - GuardValue
    - TransitionFailure
    - RuntimeFailureData
    - ActTrans
    - NxtDisplayState

- Typing fault variables

A fault variable stores data in the event of a standard or a system fault.
- Declaring a query property for a variable

A query property determines which parts of a global variable are accessible in the runtime environment with the query() API function.

## Related reference

- Description tab: business state machine editor