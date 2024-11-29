# Workflow REST API programming

- Authorization for Workflow REST APIs

The Workflow REST APIs use authorization roles to determine the actions that a user can take on objects, such as processes, tasks, and user data.
- Starting a process by calling an Business Automation Workflow REST API

You can start a process and create a new process instance by calling a REST API.
- Processing a user task by calling Business Automation Workflow REST APIs

A user task is assigned to one or more teams. A team member claims the task, provides the relevant information, and then completes the task.
- Preventing cross site request forgery

To prevent cross site request forgery attacks, the Workflow REST API operations require that the HTTP header BPMCSRFToken is set with every request.