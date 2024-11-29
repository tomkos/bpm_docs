<!-- image -->

# Inline and stand-alone human tasks

If the task is implemented within a BPEL process, it is called
an inline task. Otherwise, it is referred to as a stand-alone task.

- Stand-alone tasks

Stand-alone tasks follow the service-oriented architecture (SOA) pattern and they are loosely coupled with the components that invoke them (to-do tasks), or the components that are invoked by them (invocation tasks). They can be wired to another component using the Service Component Architecture (SCA) infrastructure.
- Inline tasks

Inline tasks are an integral part of the BPEL process. Inline tasks can be to-do tasks, invocation tasks, or administration tasks. Because collaboration tasks rely on the interaction between people and do not directly interact with processes, they cannot be inline tasks. Inline tasks are neither visible as SCA components (cannot be wired), nor are they reusable in other processes or activities.

## Related concepts

- Types of human task
- Task templates
- Task instances
- Human task clients
- Human task user interfaces
- Versioning of human tasks
- To-do tasks and collaboration tasks with parallel ownership
- Lifecycle of a human task
- Using human tasks in different scenarios in IBM WebSphere® Integration Developer

## Related tasks

- Setting human task preferences
- Improving performance when using human task list widgets