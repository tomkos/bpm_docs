# WebSphere
Application Server warnings in the Workflow Center
log file

These WebSphere® Application
Server messages are written to the
SystemOut.log file for  Workflow Center in situations where the Process Designer web editor has been running for a long period
of time. They do not affect any functionality and can be safely ignored.

```
0000035e async W com.ibm.ws.webcontainer.async.ListenerHelper \_invokeAsyncErrorHandling
SRVE8092W: An exception occurred invoking the async error mechanism.
000001b0 LTPAServerObj W
SECJ0371W: Validation of the LTPA token failed because the token expired
```

```
[4/15/14 10:03:03:611 CEST] 0000035e async W
com.ibm.ws.webcontainer.async.ListenerHelper \_invokeAsyncErrorHandling
SRVE8092W: An exception occurred invoking the async error mechanism.

com.ibm.wsspi.webcontainer.security.SecurityViolationException: Basic realm="BPMRESTAPI"
at com.ibm.ws.webcontainer.collaborator.WebAppSecurityCollaboratorImpl.convertWebSecurityException(WebAppSecurityCollaboratorImpl.java:193)
at com.ibm.ws.webcontainer.collaborator.WebAppSecurityCollaboratorImpl.preInvoke(WebAppSecurityCollaboratorImpl.java:239)
at com.ibm.wsspi.webcontainer.collaborator.CollaboratorHelper.preInvokeCollaborators(CollaboratorHelper.java:432)
at com.ibm.ws.webcontainer.async.ListenerHelper.\_invokeAsyncErrorHandling(ListenerHelper.java:174)
at com.ibm.ws.webcontainer.async.ListenerHelper.invokeAsyncErrorHandling(ListenerHelper.java:129)
at com.ibm.ws.webcontainer.async.AsyncTimeoutRunnable.run(AsyncTimeoutRunnable.java:28)
at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:450)
at java.util.concurrent.FutureTask$Sync.innerRun(FutureTask.java:314)
at java.util.concurrent.FutureTask.run(FutureTask.java:149)
at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$301(ScheduledThreadPoolExecutor.java:109)
at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:217)
at java.util.concurrent.ThreadPoolExecutor$Worker.runTask(ThreadPoolExecutor.java:906)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:929)
at java.lang.Thread.run(Thread.java:796)
Caused by: com.ibm.ws.security.web.WebSecurityException: Basic realm="BPMRESTAPI"
at com.ibm.ws.security.web.EJSWebCollaborator.preInvoke(EJSWebCollaborator.java:441)
at com.ibm.ws.webcontainer.collaborator.WebAppSecurityCollaboratorImpl.preInvoke(WebAppSecurityCollaboratorImpl.java:230)
... 12 more
[4/15/14 10:03:04:625 CEST] 000001b0 LTPAServerObj W SECJ0371W: Validation of the LTPA token failed because the token expired
```