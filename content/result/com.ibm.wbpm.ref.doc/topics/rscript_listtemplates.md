<!-- image -->

# listTemplates.py administrative script

Over time, new versions of applications
are installed, but an old version cannot be uninstalled until there
are no more active instances of the old version.

Use
the listTemplates.py administrative script to display
which versions of applications are deployed, and for each version,
how many instances there are of it. This helps you to identify applications
that can be uninstalled.

## Prerequisites

- Include the wsadmin -user and -password options
to specify a user ID that has operator authority.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## Location

```
install\_root\ProcessChoreographer\admin
install\_root/ProcessChoreographer/admin
```

## Syntax

```
install\_root/bin/wsadmin.sh 
install\_root\bin\wsadmin

-f listTemplates.py
     -cluster clusterName
     [-templateName templateName]
     [-applicationName applicationName]
     (-all | -active | -stopped | -invalid | -superseded)
     [-countInstances]
     [-groupBy (application | template)]
```

## Parameters

## Example

For example, to list information
about all versions of the application myapp that
are deployed on the cluster myCluster:

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