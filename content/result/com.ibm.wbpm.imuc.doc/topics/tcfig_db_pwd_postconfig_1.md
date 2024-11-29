# Updating the data source authentication alias

## Before you begin

- For a Network deployment environment, make sure all sending of
requests is stopped. You must also  stop all the clusters.
- For a Standalone profile, make sure all sending of requests is
stopped.
- You must start the DMGR and all node agents after stopping the
network deployment clusters and servers before changing the alias.

## Procedure

To change the data source authentication alias, complete
the following steps:

1. Login to the administrative console.
2. Select Resources > JDBC > Data sources. Note: Make sure you write down the values
that are configured for Component-managed authentication
alias and Authentication alias for XA recovery.
3. Select the datasource.
4. Select the Related Items section  and then select JAAS
- J2C authentication data.
5. Select the appropriate Component-managed authentication
alias value noted in step 2. Edit the password, and then
click OK to save the change.
6. Go back to the JAAS - J2C authentication data panel
and select the Authentication alias for XA recovery value
noted in step 2. Edit the password, and then click OK to
save the change.
7. Save the updates and click Full Synchronize to
synchronize the information to all the nodes.

## Related tasks

- Updating the messaging engine data store authentication alias