# Configuring the  User Management Services dedicated
pods option

Containers: 
User Management Services provides different
capabilities. The default is to run each capability in a dedicated pod so that each capability can
scale horizontally as required. It is also possible to have a single pod that contains all UMS
capabilities.

## About this task

- UMS SSO
- UMS Users and Groups (based on SCIM)
- UMS Teams

This is option is selected by the UMS configuration parameter
dedicated\_pods, which defaults to the value true, which is better
suited for  production environments.

## Procedure

Later, when you are customizing your custom resource file in the task tsk\_config\_ums.html:

- To have dedicated pods for each UMS capability:
You will use the default dedicated\_pods: true option and can adjust any
configuration parameters to suit your requirements for each pod type.  For the
replica\_count, resources, autoscaling and
logs parameters, default values are provided, so it is optional to set their values
explicitly.
- To have all UMS capabilities in one pod:
You must specify dedicated\_pods: false and specify the configuration
parameters for the all-in-one pod type. For the replica\_count,
resources, autoscaling and logs parameters,
default values are provided, so it is optional to set their values explicitly.