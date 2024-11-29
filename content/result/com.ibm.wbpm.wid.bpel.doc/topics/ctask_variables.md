<!-- image -->

# Replacement variables in people assignment criteria definitions

For example, a people assignment criteria definition might contain
the %htm:input.\name% replacement variable as a parameter.
This variable denotes the "name" element of the task input message
value that is received by the task when it is initiated. People resolution
dynamically replaces the variable with the task input message value.

If your replacement variable contains an element that is defined
as an array, the variable is replaced by this array. For example,
if the NamedUsers parameter of the Group Members without Named Users people assignment
criteria definition contains the %htm:input.\excludedUsers% replacement
variable, and this "excludedUsers" element is an array, all the user
IDs in the array are removed from the result list.