<!-- image -->

# Choosing the appropriate compensation for your process

- If you do not have IBM® extensions
enabled for this process, then you cannot use compensation pairs and
must use a compensation handler. The compensation tab
in the business process editor is an IBM enhancement
of the BPEL programming language, and so will not be available if
this option was disabled when the process was initially created.
- You cannot use a compensation handler with a microflow. Since
microflows run within a single transaction, you must use the compensation
tab of the business process editor to store the original properties
of each invoke activity in the event that the process fails.

So, if you are designing a long-running process, then you can use
either of these options. If the compensation characteristics of each
activity are fairly simple (in that compensation can be achieved in
a single step), then consider using compensation pairs for each of
these activities. If, however, you require compensation that makes
use of more complicated logic, assign a compensation handler to each
activity, and populate it with the necessary objects.

## Example

## Related concepts

- Working with BPEL extensions
- Best Practice: When to not use the BPEL extensions

## Related reference

- Compensation tab: BPEL process editor