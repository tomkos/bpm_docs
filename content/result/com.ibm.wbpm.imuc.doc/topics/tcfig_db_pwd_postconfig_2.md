# Updating the messaging engine data store authentication alias

## Before you begin

- For a network deployment environment, make sure all sending of
requests is stopped. Stop all the clusters.
- For a stand-alone profile, make sure all sending of requests is
stopped.
- You must start the deployment manager and all node agents after
stopping the network deployment clusters and servers and before changing
the alias.

## Procedure

To change the messaging engine data store authentication
alias, complete the following steps:

1. Login to the administrative console.
2. Select Service Integration > Buses.
3 To update the authentication alias for each bus, completethe following steps:
    1. Select Buses > [Bus\_NAME] > Messaging Engines > [MESSAGING\_ENGINE] > Data Store . Remember: Make sure you write
down and save the Authentication Alias value
in the Data Store.
    2. Select the Related Items section and click JAAS
- J2C authentication data.
    3. Select the value noted in step a. Edit the password,
and then click OK to save the change.
    4. Save the updates and click Full Synchronize to
synchronize the information to all the nodes.

## Related tasks

- Updating the data source authentication alias