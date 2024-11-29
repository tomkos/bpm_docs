# Interacting with a parent case from a process

Processes that are running under a case activity can interact with their parent case using the
methods provided in the TWProcessInstanceParentCase JavaScript API. For example:

```
tw.system.currentProcessInstance.parentCase.addCommentToCase("Hello world!", true);
```

For more information about the TWProcessInstanceParentCase JavaScript API, see TWProcessInstanceParentCase.

For information about using new or existing processes to implement case activities, see Adding an activity with a new process and Adding an activity with an existing process.

- ECM Update Content Object Properties Service
- ECM Get Content Object Property Service
- ECM Get Content Object Properties Service
- ECM Update Content Object Property Service

To work with the parent case from your process instance, you can use the
parentCaseId and parentCaseServerName properties that are
available in the TWProcessInstance object.

## Runtime synchronization of content objects

When a workflow process runs from a case activity, the process has access to the case content
objects. Any updates to content objects in a workflow process show up synchronously in the case or
activity. Similarly, content object updates from within the case or activity are synchronously made
available to the workflow process.