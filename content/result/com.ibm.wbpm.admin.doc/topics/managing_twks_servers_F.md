# Bringing workflow servers back online

## Before you begin

Ensure that you have administrative access to the Workflow Center repository
to remove offline servers. For more information, see Granting access to the Workflow Center repository.

## Procedure

1 If you took a workflow server offline temporarily or didn'tremove the offline record that is associated with it, follow these steps: Note: Only one record can be associated with a deployment environmentregardless of whether that environment has had a name change or beenmoved. If the related record is in an offline state, it must be removedbefore the deployment environment can be brought back online.
    1. Click the Servers tab in Workflow Center.
    2. For the server that you want to bring online, click Remove
Offline Server.
    3. When prompted, confirm that you want to remove the server.
2 Perform the steps in either of the following topics to confirmyou have the proper settings in place to enable the online processserver:

- (Traditional) Customizing the Workflow Server settings used to connect to Workflow Center
- (Traditional) Using the administrative console to customize the Workflow Server used to connect to Workflow Center
- (Containers) Customizing the container runtime environment Workflow Server to connect to Workflow Center
3. Restart the workflow server and confirm you can see it in
Workflow Center.