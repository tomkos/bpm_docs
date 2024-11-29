# Security in human tasks and BPEL processes

Human tasks, by definition, require human intervention to complete
them. Some business processes might also require human intervention.
These human tasks and business processes are developed using Integration Designer and are
invoked using Business Process Choreographer. When you develop the
task or process, you must assign roles to users or groups involved
in the human tasks and BPEL processes.

The Human Task Manager uses the roles to determine the users' capabilities
on a production system.

- Authorization roles for BPEL processes

A role is a set of people who share the same level of authorization. Actions that you can take on BPEL processes depend on your authorization role. This role can be a Java EE role or an instance-based role.
- Authorization roles for human tasks

Actions that you can take on human tasks depend on your authorization role. This role can be a system-level Java EE role or an instance-based role. Role-based authorization requires that administration and application security is enabled for the application server.