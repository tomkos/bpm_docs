# Reviewing DB2 diagnostic
information

## About this task

Review DB2 diagnostic
information when your systems are not working well. This is a way
to see if the log files are full.

## Procedure

```
2008-04-03-11.57.18.988249-300 I1247882009G504    LEVEL: Error
PID     : 16020                TID  : 3086133792  PROC : db2agent (WPRCSDB) 0
INSTANCE: db2inst1             NODE : 000         DB   : WPRCSDB
APPHDL  : 0-658                APPID: 9.5.99.208.24960.080403084643
AUTHID  : DB2INST1
FUNCTION: DB2 UDB, data protection services, sqlpWriteLR, probe:6680
RETCODE : ZRC=0x85100009=-2062548983=SQLP\_NOSPACE
          "Log File has reached its saturation point"
          DIA8309C Log file was full.

2008-04-03-11.57.18.994572-300 E1247882514G540    LEVEL: Error
PID     : 16020                TID  : 3086133792  PROC : db2agent (WPRCSDB) 0
INSTANCE: db2inst1             NODE : 000         DB   : WPRCSDB
APPHDL  : 0-658                APPID: 9.5.99.208.24960.080403084643
AUTHID  : DB2INST1
FUNCTION: DB2 UDB, data protection services, sqlpgResSpace, probe:2860
MESSAGE : ADM1823E  The active log is full and is held by application handle
          "274".  Terminate this application by COMMIT, ROLLBACK or FORCE
          APPLICATION.
```

In the preceding example,
looking at the DB line, you can see that the WPRCSDB is experiencing
full transaction logs.

```
su -l db2inst1
	db2diag | less
```