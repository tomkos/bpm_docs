# Configuring Oracle Data Guard for IBM Business Automation Workflow

You can configure Oracle Data Guard
to be used with IBM® Business Automation Workflow. Oracle
Data Guard provides high availability, disaster recovery, and data
protection and is used to create, manage, and monitor one or more
standby databases so that production Oracle databases can survive
disasters and data corruptions.

When IBM Business Automation Workflow is
configured to use Oracle Data Guard, you typically have one production
database, which is your primary database, and several standby databases.
Then Oracle Data Guard automatically maintains each standby database
by transmitting redo data from the primary database and applying the
redo data to the standby database. If your production database becomes
unavailable because of a planned or an unplanned outage, Oracle Data
Guard enables you to switch any standby database to the production
role, minimizing the downtime that is associated with the outage.

Oracle
Data Guard automatically maintains each standby database by transmitting
redo data from the primary database and then applying the redo to
the standby database.

A Typical Data Guard Configuration

<!-- image -->

## Procedure

1. Set up the Oracle Data Guard environment.
2. Create a database service from the primary database:
Exec DBMS\_SERVICE.CREATE\_SERVICE('BPM','BPM');
3. Create a trigger from the primary database by running the
following command: CREATE OR REPLACE TRIGGER START\_SERVICES AFTER STARTUP ON DATABASE 
DECLARE
 ROLE VARCHAR(30);
BEGIN 
 SELECT DATABASE\_ROLE INTO ROLE FROM V$DATABASE;
 IF ROLE = 'PRIMARY' THEN
  DBMS\_SERVICE.START\_SERVICE('ORCL');  END IF;
END; 
/Note: When you start a database, your primary database
always starts a BPM service. Therefore, your client always connects
to the primary database.
4. Restart the primary database or start the following service
by running the following command:  EXEC DBMS\_SERVICE.START\_SERVICE('BPM');

## What to do next

IBM
Business Process Manager creates the JDBC URL in the following default
format:

```
jdbc:oracle:thin:@//LISTENER\_HOST:LISTENER\_PORT/SERVICE\_NAME
```

To
use the Net connection descriptor URL, specify it in a format similar
to the following example (but in a single input line) using the bpm.de.db.#.url property:

```
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS\_LIST=
                  (ADDRESS=(PROTOCOL=TCP)(HOST=host\_A)(PORT=1521))
                  (ADDRESS=(PROTOCOL=TCP)(HOST=host\_B)(PORT=1521))
                  (LOAD\_BALANCE=off)(FAILOVER=on))
                  (CONNECT\_DATA=(SERVICE\_NAME=service\_name)))
```

## Related concepts

- System requirements
- Considerations for HADR setup and configuration

## Related tasks

- Preparing operating systems for product installation