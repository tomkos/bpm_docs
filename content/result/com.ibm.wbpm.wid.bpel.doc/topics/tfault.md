<!-- image -->

# Using fault handlers

## About this task

- Catch a fault and try to correct the problem so that the business
process continues to normal completion.
- Catch a fault and find that it is not resolvable at this scope.In this case, you have the following additional options:
    - Throw a new fault.
    - Rethrow the original fault so that another scope can handle it.
    - Reply with a fault to the process initiator.
    - Start a human task to correct the issue. If the fault handler
cannot resolve the issue, you might need to roll back the process
and compensate it.
    - For long-running processes, consider using the Stop
on unhandled faults property on the process to handle
a fault situation administratively.

To create a fault
handler on an activity, do the following instructions:

## Procedure

1. Click the scope or invoke activity for which you want to
handle a fault. The action bar displays.
2. In the action bar, click the fault handler icon as shown
in this image.  A fault handler
is created with one default catch element, and shown in the canvas
in association with the parent activity. You can place as many paths
in this handler as necessary, and each one is preceded by either of
the following elements:

Option
Description

Catch element 
Use this element to intercept and deal with a specific fault.
You can use as many of these elements as is appropriate.

Catch all element
Use this element to intercept and deal with any fault that
is not already defined in an existing catch element. You can use only
one per fault handler.
3. Populate the existing catch path with the activities that
are appropriate to deal with the specific exception that has occurred.
4. To add another path, click the fault handler to launch
the action bar, and choose the appropriate element.

## Results

- If the fault has no associated fault data, a catch activity with
the matching fault name is selected (providing the fault handler has
no variable assigned). Otherwise, the default catch-all element is
chosen.
- If the fault does have fault data associated with it, then a catch
element with matching fault name and variable values is selected.
If there is no fault name specified, then a fault with a matching
fault type is selected. Otherwise, the default catch-all element is
chosen.

## Example

## Related concepts

- Fault activities
- Raising faults
- BPEL process compensation
- Fault handling and compensation handling in BPEL processes

## Related tasks

- Continue processing upon unhandled faults
- Typing fault variables