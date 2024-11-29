# Case configuration tasks fail when the external Content Platform Engine is used with existing
IBM Case Manager object stores

```
FINER Wed Aug 14 08:55:58 CDT 2019 THROW
com.filenet.api.exception.EngineRuntimeException  thrown while executing method executeWork() of com.ibm.ecm.configmgr.app.acm.task.DefineDefaultProjectArea$Execution
Stack Trace follows (when available):
com.filenet.api.exception.EngineRuntimeException: FNRCV0006E: EVENT\_HANDLER\_THREW: An exception occurred in the event handler. Message was: Failed to retrieve task subscription class definition: CmAcmTaskWorkflowLaunchSubscription failedBatchItem=0 errorStack={
at com.filenet.engine.handlers.HandlerFactory$HandlerWrapper.standardCatch(HandlerFactory.java:304)
...

Caused by: java.lang.RuntimeException: Failed to retrieve task subscription class definition: CmAcmTaskWorkflowLaunchSubscription failedBatchItem=0
at com.ibm.casemgmt.intgimpl.eventhandler.ProjectAreaEventHandler.invokeBPMUpdate(ProjectAreaEventHandler.java:280)
at com.ibm.casemgmt.intgimpl.eventhandler.ProjectAreaEventHandler.onEvent(ProjectAreaEventHandler.java:104)
at com.filenet.engine.handlers.EventActionWrapper.onEvent(EventActionWrapper.java:60)
... 56 more
```

This error does not occur if the system is configured to use the embedded Content Platform Engine or if you're using an external Content Platform Engine that has new object stores for the design object
store and target object store.

## Workaround

In a development environment

Run the Configure Case Integration with IBM Business Automation
Workflow case configuration task before
running the Define the Default Project Area task. For more information about
these case configuration tasks, see Table 1: Task requirements for a development environment
in Preparing to run the case configuration tasks.

In a production environment

Run the Configure Case Integration with IBM Business Automation
Workflow case configuration task before
running the Define Target Environment case configuration task. For more
information about these case configuration tasks, see Table 1: Task requirements for a production
environment in Preparing to run the configuration tasks