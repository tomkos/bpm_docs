<!-- image -->

# deleteInvalidTaskTemplate.py administrative
script

The deleteInvalidTaskTemplate.py script
removes from the database those templates, and all objects that belong
to them, that are not contained in any corresponding valid application
in the WebSphere® configuration
repository. This situation can occur if deploying an application was
canceled or the application was not stored in the configuration repository
by the user. These templates usually have no impact. They are not
shown in Business Process Choreographer Explorer.

You cannot use this script
to remove templates of valid applications from the database. This
condition is checked and a ConfigurationError exception is thrown
if the corresponding application is valid.

## Prerequisites

- Run the script in the connected mode, that is,
do not use the wsadmin -conntype none option.
- You must have either operator or deployer
authority.
- At least one cluster member must be running.
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

-f deleteInvalidTaskTemplate.py
     -cluster cluster\_name
     -templateName templateName
     -validFromUTC timestamp
     -nameSpace nameSpace
```

## Parameters