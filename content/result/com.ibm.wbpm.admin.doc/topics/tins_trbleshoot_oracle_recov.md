# Troubleshooting Oracle transaction recovery messages

## About this task

```
[4/19/12 13:44:50:062 EDT] 00000007 WSRdbXaResour E   DSRA0304E:  XAException occurred. XAException contents and details are: The cause is               : null.
[4/19/12 13:44:50:062 EDT] 00000007 WSRdbXaResour E   DSRA0302E:  XAException occurred.  Error code is: XAER\_RMERR (-3).  Exception is: <null>
```

If
there is a system failure, or the server was not stopped properly
during a distributed transaction, the WebSphere Application Server
transaction manager attempts to clean up any failed transactions that
are found in the transaction logs. The Oracle database requires that
you have special permissions for transaction recovery. The previous
error occurs when a user that attempts to run the recover method does
not have sufficient privileges.

- grant select on pending\_trans$ to user\_name;
grant select on dba\_2pc\_pending to user\_name; 
grant select on dba\_pending\_transactions to user\_name;
- If you are using Oracle V10.2.0.3 or a previous version of the
JDBC driver:grant execute on dbms\_system to user\_name;
- If you are using Oracle V10.2.0.4 or a more recent of the JDBC
driver:grant execute on dbms\_xa to user\_name;

Repeat the previous steps for each Oracle user that
is defined during deployment environment creation.