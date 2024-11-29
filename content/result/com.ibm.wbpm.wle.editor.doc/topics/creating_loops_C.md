# Associating loop activity instances with different items

## About this task

To set up the activity instance-item association, the following key settings are required:

- As a prerequisite, you must already have defined a private variable that holds the list of items
that you want to iterate through, for example, tw.local.ListofItems. This
variable is used in the built-in tw.local.ListofItems.listLength
JavaScript function, where .listLength calculates the length of the item list.
- You associate each activity instance with a specific item in the list by using the
tw.local.ListofItems[tw.system.step.counter] JavaScript, where
[tw.system.step.counter] specifies which item to be retrieved from the list.

## Procedure

1. In the process diagram, select the activity that you want to configure.
2. In the properties, select General.
3. Expand Loop and select Multi-instance Loop
from the Loop type list.
4. Enter tw.local.ListofItems.listLength in the
Start quantity box.
5. On Data Mapping, under Input Mapping,
select, or type the following input string:
tw.local.ListofItems[tw.system.step.counter]
6. For the Ordering and Flow condition
settings, refer to steps 5 and 6 in the procedure described
earlier.
7. Click Save or Finish Editing.