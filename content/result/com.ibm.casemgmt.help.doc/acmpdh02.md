# Primary queue

Only role swimlanes that have a primary queue attribute are used in Step Designer. Roles without
a primary queue are ignored and cannot be added to the task process map as a swimlane. If the same
primary queue is mapped to more than one role, Step Designer displays only one of the roles that
matches the primary queue as an option to add as a role swimlane to the task process map.

The value for the primary queue attribute, CB\_PrimaryQueue, is the queue name that is defined by
Case Builder when you define a role. The format of the value is
<solution prefix>\_<normalized role name>. For example, if you define
role A for a solution that is called My Solution that has the
solution prefix myso, Case Builder defines a
queue name of myso\_roleA and sets the value for the CB\_PrimaryQueue attribute for
role A as myso\_roleA.

- An upgraded solution contains two or more roles that have their first in-basket (with
CB\_Inbasket attribute) and those in-baskets point to the same queue.
- You manually set CB\_PrimaryQueue for two roles to share the same
queue in IBM
FileNet® Process Designer