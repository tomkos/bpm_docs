# Customizing Business Automation Workflow on containers with multiple target object stores

## About this task

You can add additional target object stores by updating the Custom Resource (CR) file to include
the additional target object store under the baw\_configuration section for IBM® Business Automation
Workflow
and by
updating the target object store configuration under the initialize\_configuration
section and datasource\_configuration sections.

## Procedure

To create an additional target object store:

1. Follow the steps in Optional: Adding additional object stores post-deployment
for adding more object stores.
2. Use the existing target object store configuration as a guide to fill in the values for
the required parameters under
initialize\_configuration.ic\_obj\_store\_creation.object\_stores.
3. Compared to object stores, target object stores require the following additional
parameters: 
oc\_cpe\_obj\_store\_enable\_workflow: true
oc\_cpe\_obj\_store\_workflow\_data\_tbl\_space: 
oc\_cpe\_obj\_store\_workflow\_admin\_group:
oc\_cpe\_obj\_store\_workflow\_config\_group:
4. Create the database and tablespace that are required by the target object
store.
5 Edit the CR file and add the additional target object store tobaw\_configuration.case.tos\_list for Business Automation Workflow Runtime. A Business Automation Workflow Runtimeexample:baw\_configuration:- name: instance1 case: tos\_list: - object\_store\_name: "TOS1" connection\_point\_name: "cpe\_conn\_tos1" desktop\_id: "navigator\_desktop\_id" target\_environment\_name: "project\_area\_name\_or\_target\_env\_name\_1" is\_default: true - object\_store\_name: "TOS2" connection\_point\_name: "cpe\_conn\_tos2" desktop\_id: "navigator\_desktop\_id" target\_environment\_name: "project\_area\_name\_or\_target\_env\_name\_2" is\_default: false Notes:

```
baw\_configuration:
-  name: instance1
   case: 
      tos\_list:
          - object\_store\_name: "TOS1"
            connection\_point\_name: "cpe\_conn\_tos1"
            desktop\_id: "navigator\_desktop\_id"
            target\_environment\_name: "project\_area\_name\_or\_target\_env\_name\_1"
            is\_default: true
          - object\_store\_name: "TOS2"
            connection\_point\_name: "cpe\_conn\_tos2"
            desktop\_id: "navigator\_desktop\_id"
            target\_environment\_name: "project\_area\_name\_or\_target\_env\_name\_2"
            is\_default: false
```

    - Make sure that the value of tos\_list.connection\_point\_name is the same as the
value of oc\_cpe\_obj\_store\_workflow\_pe\_conn\_point\_name in the same object
store.
    - The value of target\_environment\_name must be different for each target object
store.
    - The URL of the Case client is displayed in the access information ConfigMap and CR endpoints
only if the value of desktop\_id is defined in the CR. If not, users can find other
desktops in the desktop list page of the IBM Business Automation
Navigator.
6. Apply the updated CR.