<!-- image -->

# Stand-alone tasks

Stand-alone tasks have an autonomy setting of either peer or child.
Stand-alone tasks with peer autonomy communicate with their partner
components exclusively by SCA means. That is, to-do tasks receive
input messages and return output or fault messages, and invocation
tasks send input messages and receive output or fault messages. No
further information exchange or lifecycle control happens.

- To-do tasks have an interface that can be wired to a client component.
- Invocation tasks have a reference that can be wired to the service
to be invoked.
- Collaboration tasks are self-contained SCA components. Although
collaboration tasks are stand-alone task components they have no SCA
references or SCA interfaces and therefore cannot be wired to other
service components. Instead they provide interfaces so that people
can start them and work with them using the Human Task Manager APIs.

- The task provides just another service
- You intend to replace the stand-alone task later on and don't
want to change the component to which it is wired.