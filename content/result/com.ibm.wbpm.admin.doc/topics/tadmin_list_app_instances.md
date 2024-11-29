<!-- image -->

# Listing information about process and task templates

## Before you begin

- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## Procedure

1. Change to the Business Process Choreographer
subdirectory where the administrative script is located.  Enter the following
command:cd install\_root/ProcessChoreographer/admin
Enter the following command:cd install\_root\ProcessChoreographer\admin
2 Run the script to display the information. Where:-cluster clusterName The name of the cluster where Business Process Choreographer isconfigured. In a multicluster setup, you must specify the applicationcluster because that is where Business Process Choreographer is configured. -templateName templateName Optionally restricts the list to a particular temple. -applicationName applicationName Optionally restricts the reported information to the specifiedapplication. The default is to report information about all applicationson the cluster. -all | -active | -stopped |-invalid | -superseded You can specify one of these options to restrict the list to asubset of the instances.-all Lists all valid templates. That is, templates that belong to adeployed application. This behavior is the default. -active This option lists only valid templates that are in the state active . -stopped This option lists only valid templates that are in the state stopped . -invalid This option lists only templates that are in the Business ProcessChoreographer database, but do not belong to any deployed application.This is the only option that displays invalid templates.Important: If you use this option, the script requires accessto the Business Process Choreographer database, so you must run thescript in connected mode and at least one cluster member must be running. -superseded This option lists only templates for which a newer version isavailable in the runtime system, regardless of their state. -countInstances Optionally provides a count of how many instances of each templateare in the system. Important: If you use this option,the script requires access to the Business Process Choreographer database,so you must run the script in connected mode, and at least one clustermember must be running. -groupBy (application |template ) Optionally groups the information by application or by template. For example, to list informationabout all versions of the application myApp that are deployed on the cluster myCluster , including how many instances there are of each template version: Enter the following command:wsadmin.sh -f listTemplates.py -cluster myCluster -application myApp -all -countInstances Enter the following command:wsadmin -f listTemplates.py -cluster myCluster -application myApp -all -countInstances Thescript outputs the information in a table that has the following columns:
    - Enter the following
command:
install\_root/bin/wsadmin.sh -f listTemplates.py
     -cluster clusterName
     [-templateName templateName]
     [-applicationName applicationName]
     (-all | -active | -stopped | -invalid | -superseded)
     [-countInstances]
     [-groupBy (application | template)]
    - Enter the following command:
install\_root\bin\wsadmin -f listTemplates.py
     -cluster clusterName
     [-templateName templateName]
     [-applicationName applicationName]
     (-all | -active | -stopped | -invalid | -superseded)
     [-countInstances]
     [-groupBy (application | template)]

For example, to list information
about all versions of the application myApp that are deployed on the cluster myCluster, including how many instances there are of each template version:

<!-- image -->

<!-- image -->

```
wsadmin.sh -f listTemplates.py  -cluster myCluster -application myApp -all -countInstances
```

<!-- image -->

```
wsadmin -f listTemplates.py  -cluster myCluster -application myApp -all -countInstances
```

    - Application name
    - Version
    - Template name
    - Valid-from date
    - Number of instances
3. Optional: If you want to identify application
templates that could be removed, look for superseded versions that
have zero instances. Then perform Browsing and administering modules to check whether
any SCA modules depend on the services exported by the application.
By removing applications that are no longer needed, you can
speed up how fast your server starts.
4 Optional: If you want to uninstall a particularapplication template, but it still has running instances, considerperforming any of the following.

- Allow more time for the running instances to reach an end state,
then run the script again.
- Identify whether the running BPEL process instances can be migrated
to a newer template instance.
- Investigate the reasons why particular instances have not reached
an end state, and consider whether it is acceptable to force any of
then into an end state.

## Results

<!-- image -->