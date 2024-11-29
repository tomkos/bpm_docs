<!-- image -->

# Example: Including custom properties in a query

```
query ( " DISTINCT TASK.TKIID ",
           " TASK\_CPROP.NAME = 'customerID' AND " +  
           " TASK\_CPROP.STRING\_VALUE = 'CID\_12345' AND " + 
           " TASK.KIND IN 
              ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) AND " +  
           " TASK.STATE = TASK.STATE.STATE\_READY ",
           (String)null, (String)null, (Integer)null, (TimeZone)null );
```

```
query ( " DISTINCT TASK.TKIID, TASK\_CPROP.NAME, TASK\_CPROP.STRING\_VALUE",
           " TASK.KIND IN 
              ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) AND " +  
           " TASK.STATE = TASK.STATE.STATE\_READY ",
           (String)null, (String)null, (Integer)null, (TimeZone)null );
```

```
SELECT DISTINCT TA.TKIID , TACP.NAME , TACP.STRING\_VALUE  
   FROM  TASK TA LEFT JOIN TASK\_CPROP TACP ON (TA.TKIID = TACP.TKIID), 
         WORK\_ITEM WI 
   WHERE WI.OBJECT\_ID = TA.TKIID 
   AND    TA.KIND IN ( 101, 105 )       
   AND    TA.STATE = 2                  
   AND  (WI.OWNER\_ID = 'JohnSmith' OR WI.OWNER\_ID IS NULL AND WI.EVERYBODY = 1 )
```