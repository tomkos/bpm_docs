<!-- image -->

# manageTemplates.py command

## Prerequisites

- Run the script in connected mode, that is, do not use the wsadmin -conntype
none option.
- At least one cluster member must be running.
- If your user ID does not have administrator authority, include
the wsadmin -user and -password options
to specify a user ID that has administrator authority.
- If you are not working with the default profile,
use the wsadmin -profileName profile option
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
 -f manageTemplates.py
  -stop application\_name
  -start application\_name
  -uninstall BPEL\_application\_name [-force][-wait seconds]
```

## Parameters

## Example: Starting an application

```
wsadmin -f manageTemplates.py -start application\_name
wsadmin.sh -f manageTemplates.py -start application\_name
```

## Example: Stopping an application

```
wsadmin -f manageTemplates.py -stop application\_name
wsadmin.sh -f manageTemplates.py -stop application\_name
```

## Example: Uninstalling a BPEL application

```
wsadmin -f manageTemplates.py -uninstall application\_name
wsadmin.sh -f manageTemplates.py -uninstall application\_name
```