<!-- image -->

# Example: Querying tasks in the claimed state

```
query( "DISTINCT TASK.TKIID", 
           "TASK.STATE = TASK.STATE.STATE\_CLAIMED AND " +  
           "TASK.OWNER = 'JohnSmith'", 
           (String)null, (String)null, (Integer)null, (TimeZone)null )
```

```
SELECT DISTINCT TASK.TKIID
   FROM   TASK TA, WORK\_ITEM WI,  
   WHERE  WI.OBJECT\_ID = TA.TKIID
   AND    TA.STATE = 8
   TA.OWNER = 'JohnSmith'                            
   AND  ( WI.OWNER\_ID = 'JohnSmith' OR WI.OWNER\_ID = null AND WI.EVERYBODY = true )
```

```
WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_OWNER
```

```
query( "DISTINCT TASK.TKIID", 
           "TASK.STATE = TASK.STATE.STATE\_CLAIMED AND " +  
           "WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_OWNER", 
           (String)null, (String)null, (Integer)null, (TimeZone)null )
```

- A condition for access control is added to the where clause. This example
assumes that group work items are not enabled.
- Constants, such as TASK.STATE.STATE\_READY, are replaced
by their numeric values.
- A FROM clause and join conditions are added.

```
SELECT DISTINCT TASK.TKIID
   FROM   TASK TA, WORK\_ITEM WI,  
   WHERE  WI.OBJECT\_ID = TA.TKIID
   AND    TA.STATE = 8
   AND    WI.REASON = 4                                
   AND  ( WI.OWNER\_ID = 'JohnSmith' OR WI.OWNER\_ID = null AND WI.EVERYBODY = true )
```

```
SELECT DISTINCT TASK.TKIID
   FROM   TASK TA, WORK\_ITEM WI,  
   WHERE  TA.TKIID = WI.OBJECT\_ID =  
   AND    TA.STATE = 8                            
   AND   TA.OWNER = 'JohnSmith')
```