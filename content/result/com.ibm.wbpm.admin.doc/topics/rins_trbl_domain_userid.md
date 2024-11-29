# DB2 log file error: SQL1092N "USERID does not have the authority
to perform the requested command or operation"

```
SQL1092N "USERID does not have the authority to perform the requested command or operation."
```

## Resolving the problem

1. Add the domain user ID to the local group DB2ADMNS.
2. With a user having SYSADM privileges or local administrator authority, open a DB2 command window
and run the following commands from the prompt. (Alternatively, you can open a DB2 administrator
command
window.)db2set DB2\_GRP\_LOOKUP=LOCAL,TOKENLOCAL        
db2 update dbm cfg using sysadm\_group DB2ADMNS
db2stop                                        
db2start
3. Restart the DB2 Windows services with the login ID set to the domain user ID.