# Backing up and restoring an IBM Business Automation
Workflow container
environment

## Procedure

1 Back up the source environment.
    1 Back up the following definition files that are used to deploy the environment:
        - The custom resource (CR) file used to deploy the User Management Service environment.
        - Secure definition used to protect the sensitive data in the User Management Service environment.
        - Persistent Volume (PV) and Persistent Volume Claim (PVC) definition files.
2. Back up all databases for the dependency components, for example the databases for User Management Service, IBM Business Automation
Workflow, IBM Content
Navigator, or Content Platform Engine, by using the database
commands.
3. The container environment uses the PV to store the data. Back up all folders located on the PV.
The file permissions should stay the same after those files are restored.
2 If the data is lost or corrupted for any reason, restore it on the same Kubernetes environmentby completing the following steps:

1. Delete the old deployment.
2. Restore all databases from backup images.
3. Restore all files from backup data, keeping the file permissions the same as before.
4. Deploy the IBM Business Automation
Workflow
container environment with the CR definition.