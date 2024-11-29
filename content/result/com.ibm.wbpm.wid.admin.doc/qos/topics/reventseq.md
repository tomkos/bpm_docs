<!-- image -->

# Event sequencing qualifier

The event sequencing qualifier places a control on the
order in which the runtime environment processes events. You specify
a group of one or more operations and a key. When two or more events
are received that invoke any of those operations that have the same
key, the event sequencing qualifier ensures that they are processed
in the order they are received. Without a keyed qualifier, the multithread
runtime environment does not necessarily process events in the order
that they are received.

Location: You can only apply
event sequencing qualifiers to interface operations.

- Group name  - The group identifies which operations will
participate in a particular sequence. For example, operations involved
in reserving a hotel room might be in one group and operations involved
in renting out the convention hall in another group, assuming operations
on hotel rooms are completely independent from operations on convention
halls.
- Key definition - The key is a set of XPath expressions
that identify the object being manipulated. The keys for the first
set of operations are the room numbers, such as 201 (second floor,
room 01). The keys for the second set of operations might be room
names like "Main ball room" and "West projection room." Once you have
identified those properties, you need to add an event sequencing qualifier
on all the operations, specifying that key.
- Order - The sequence in which the XPath expressions appear
in the key may matter. For room numbers, the value showing the floor
must always appear first.

Application: Event sequencing is supported only
for components that are invoked using the SCA asynchronous invocation
style. Invocations have parameters, which are business objects or
simple types. The key is a combination of one or more business object
attributes. You can set the event sequencing qualifier after you develop
the business logic; it is independent of the implementation. See the
related tasks at the end of this topic for a link to information about
using event sequencing.

The event sequencing feature includes some tuning parameters that you must consider when the
system processes large numbers of sequenced events. You set these parameters in the
eventsequencing.properties file in the
WAS\_home/properties directory.