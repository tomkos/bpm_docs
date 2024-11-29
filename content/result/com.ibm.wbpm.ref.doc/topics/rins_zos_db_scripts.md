# Sample Db2 for z/OS commands for allocating buffer pools

```
-ALTER BUFFERPOOL (BPn) VPSIZE(yyyyy)
```

```
-ALTER BUFFERPOOL (BP1) VPSIZE(20000)
```

```
//JOBLIB  DD  DISP=SHR,DSN=db2hlq.SDSNLOAD
//STEP1   EXEC PGM=IKJEFT01,DYNAMNBR=20
//SYSTSPRT DD  SYSOUT=*
//SYSPRINT DD  SYSOUT=*
//SYSUDUMP DD  SYSOUT=*
//SYSTSIN  DD  *
  DSN SYSTEM(ssid)
  -ALTER BUFFERPOOL (BPn) VPSIZE(yyyyy)
  RUN PROGRAM(DSNTIAD)  PLAN(DSNTIAnn) -
       LIBRARY('db2hlq.RUNLIB.LOAD')
  END
//SYSIN    DD  *
GRANT USE OF BUFFERPOOL BPn TO PUBLIC ;
/*
```

If you are in data sharing mode, make sure that you define the cache XCF structures for the group
buffer pools being used. For further information, see Cross-system coupling facility component of z/OS in the Db2 for z/OS documentation.