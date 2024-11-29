# Configuring Oracle Real Application Cluster (RAC) for use with IBM Business Automation Workflow

## About this task

Consider the following scenarios:

- If you use Oracle 11g R2 with the Oracle Single Client Access Name (SCAN) feature, no additional
manual configuration is required.
- If you do not use the SCAN feature or use an earlier version of Oracle that does not support the
SCAN feature, then you must specify the bpm.de.db.#.url property described in
Configuration properties for the BPMConfig command. For more information, see Mapping IBM Business Automation Workflow configuration parameters to Oracle setup parameters.

```
jdbc:oracle:thin:@//LISTENER\_HOST:LISTENER\_PORT/SERVICE\_NAME
```

```
jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS\_LIST= 
                  (ADDRESS=(PROTOCOL=TCP)(HOST=rac-node1)(port=1521))
                  (ADDRESS=(PROTOCOL=TCP)(HOST=rac-node2)(port=1521)))
                  (FAILOVER=on)(LOAD\_BALANCE=on)
                  (CONNECT\_DATA=(SERVER=DEDICATED)
                  (SERVICE\_NAME=<service\_name>)))
```

If a Oracle RAC node failover occurs, IBM Business Automation Workflow stops processing and
you might need to restart all of the IBM Business Automation Workflow nodes. If you
experience process-recovery issues, refer to Process recovery issues with business process definitions (BPD) in
IBM Business Process Manager (BPM) V7.5 and V8.

## Related information

- Configuration properties for the BPMConfig command

## Mapping IBM Business Automation Workflow configuration
parameters to Oracle setup parameters

### About this task

```
jdbc:oracle:thin:@//LISTENER\_HOST:LISTENER\_PORT/SERVICE\_NAME
```

- LISTENER\_HOST represents the RAC SCAN name
that is defined during the Oracle RAC setup. If you are using the
SCAN feature, it is specified with the IBM BPM
configuration property bpm.de.db.#.hostname.
If you are not using the SCAN feature, you specify it as part of the bpm.de.db.#.url property.
- LISTENER\_PORT represents the RAC SCAN listener
port that is defined during the Oracle RAC setup. If you are using
the SCAN feature, it is specified with the IBM BPM profile configuration property bpm.de.db.#.portNumber.
If you are not using the SCAN feature, you specify it as part of the bpm.de.db.#.url property.
- SERVICE\_NAME represents the RAC service that
is configured during the Oracle RAC setup. It is always specified
with the IBM BPM profile configuration
property bpm.de.db.#.databaseName, for example, SID.
If you are not using the SCAN feature, you must also specify it as
part of the bpm.de.db.#.url property.