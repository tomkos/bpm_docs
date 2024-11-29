<!-- image -->

# Optimizing BPEL process administration

## Before you begin

## About this task

| Process administration mode                              | Value of the ProcessAdministration custom property   |
|----------------------------------------------------------|------------------------------------------------------|
| Optimize process administration                          | optimize                                             |
| Restrict process administration to authorization         | useProcessAdminAuthorizationOnly                     |
| Restrict process administration to system administrators | useSystemAdminAuthorizationOnly                      |

## Procedure

1. In the administrative console, click Servers > Clusters > WebSphere
application server clusters, then cluster\_name where Business Process
Choreographer is configured.
2. In the Business Process Manager section, expand Business Process Choreographer and click Business Flow Manager > Custom Properties.
3. Click New to add a new custom property.
4. Enter ProcessAdministration as the
name and the value for the process administration mode. Note: Deleting this custom property will return process administration
to instance-based authorization, but only for new process instances,
activities, and scopes.
5. Save the changes.
6. Activate the changes by restarting the cluster where Business
Process Choreographer is configured.

## Results

- Alternative administration modes for BPEL processes

The alternative administration modes can help you to reduce response times for queries on tasks and processes by reducing the number of objects that are created in the Business Process Choreographer database to administer processes and activities.
- Listing information about process and task templates

Use the listTemplates.py administrative script to list instance and version information about deployed BPEL process and task templates.

<!-- image -->