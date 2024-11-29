# Modifying the IBM Workflow
Server environment
type

## About this task

For example, load testing might be done on a test server,
while a staging environment type might be used as a temporary location
to host changes before putting those changes into a production environment.
You might specify Staging as the environment
type if the server you are configuring is accessed and used to review
content and new functionality.

To change the environment type for a Workflow Server, perform
the following steps.

## Procedure

1. Stop the Workflow Server.
2. Start the wsadmin scripting tool as
described in the topic "updateBPMConfig command."
3. Run the updateBPMConfig administrative
command to update the environment type, as shown in the following
examples: AdminTask.updateBPMConfig( [ '-de', 'deployment\_environment\_name', '-environmentType', 'environment\_type' ] )
AdminConfig.save()
4. Start the Workflow Server.