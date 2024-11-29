# Modifying the IBM® Workflow
Server environment
name

## Procedure

1. Stop the Workflow Server.
2. Start the wsadmin scripting tool as
described in the topic "updateBPMConfig command."
3. Run the updateBPMConfig administrative
command to update the environment name, as shown in the following
example: AdminTask.updateBPMConfig( [ '-de', 'deployment\_environment\_name', '-environmentName', 'environment\_name' ] )
AdminConfig.save()
4. Start the Workflow Server.