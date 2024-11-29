# Activities cannot communicate with a workflow process

## Symptoms

- The activity is started, but the web service for the workflow process is not invoked.
- The activity does not receive a response from the web service, so the case properties are not
updated as expected.

On IBM® Business Automation
Workflow, you can use
the failed event manager to find failed events for your web service.

## Causes

- The response address that identifies where the web service is
to send the response is not correct.
- The component manager for the isolated region where the activity is deployed is not started. The
component manager must be started so that it can deliver events from Business Automation Workflow to the web
service.
- The web service was not deployed or was not started. The web service must be available and
running to receive events from Business Automation Workflow.
- The authentication credentials are not set correctly to permit communication between the
activity and the web service.
- If the web service moved to a different server, the XPDL document that contains the activity
might contain the wrong endpoints for the web service. The XPDL document, which is created by
Business Automation Workflow, uses these
endpoints to locate the web service that is associated with an activity.

## Diagnosing the problem

- Set filenet.ws.listener.tracefile to a valid path and file name.
- Set filenet.ws.listener.tracing to true.
- Set filenet.ws.request.tracefile to a valid path and file name.
- Set filenet.ws.request.tracing to true.

1. Open the administrative console.
2. Click Troubleshooting and then click Log and
Trace.
3. Click the server on which your web service is located.
4. Click Change log detail levels and then click the Run
time tab.
5. Expand the tree and select SCA and
com.ibm.ws.webservices to enable tracing.

1. Open the administrative console.
2. Click Integration Applications.
3. Click Failed Event Manager.

## Resolving the problem

1. In Process Task Manager, expand the Component Managers node and select
the component manager for the isolated region where the deployed activity is running.
2. Click Start on the toolbar.

After you correct the problem, you must resubmit the activity request. To do so, use Process
Administrator to locate the request in the Conductor queue and complete the Review step.