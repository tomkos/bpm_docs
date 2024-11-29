<!-- image -->

# Attaching the integration test client to test configuration
modules

## Before you begin

To attach
the integration test client to a test configuration module:

## Procedure

1 To attach to a module from your local system, or from an IBM® WorkflowServer or IBM WorkflowCenter Servercomplete one of the following steps:
    - If the integration test client is not open, right-click your
module or assembly diagram in the Business Integration view and select Test
> Attach to Modules on a Local Server. The integration
test client opens and an Attach event is displayed in the Events area.
    - If the integration test client is already open for your module,
click the down arrow beside the Invoke icon  and then select Attach.
An Attach event is displayed in the Events area.
2 To attach to all modules in a process applicationor a toolkit, complete one of the following steps:

- Right-click the process application in the Business Integration
view and select Test > Attach
to Process Application.
- Right-click the toolkit in the Business Integration view and
select Test > Attach to
Toolkit.
3. In the Events area, ensure that your Attach event is selected
and then click the Continue icon . If the Deployment Location wizard opens,
follow the instructions in the topic Deploying modules from the
integration test client.
4. Start your operation using your preferred method, such
as a JMS message, web service, or JSP.
5. If the test pauses at a manual Emulate event in the Events
area, specify output parameter values in the value editor or select
an exception to throw, then click the Continue icon  to continue the invocation. Information
about specifying output parameter values and selecting exceptions
for manual emulators is found in the topic "Specifying emulation values."
6. If you want to save a test trace of your attach session
to a test trace file, click the Save Test Client icon at any time. Information about saving
test traces is found in the topic "Saving test traces."

## Example