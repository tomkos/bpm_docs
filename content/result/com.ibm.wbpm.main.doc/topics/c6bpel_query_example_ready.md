<!-- image -->

# Example: Querying tasks in the ready state

```
query( "DISTINCT TASK.TKIID", 
           "TASK.KIND IN ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) 
             AND " +  
           "TASK.STATE = TASK.STATE.STATE\_READY AND " +  
           "WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_POTENTIAL\_OWNER", 
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
   AND    TA.KIND IN ( 101, 105 )       
   AND    TA.STATE = 2   
   AND    WI.REASON = 1           
   AND  ( WI.OWNER\_ID = 'JohnSmith' OR WI.OWNER\_ID = null AND  WI.EVERYBODY = true )
```

```
query( "DISTINCT TASK.TKIID", 
           "PROCESS\_TEMPLATE.NAME = 'sampleProcess' AND "+
           "TASK.KIND IN ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) 
             AND " +  
           "TASK.STATE = TASK.STATE.STATE\_READY AND " +  
           "WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_POTENTIAL\_OWNER", 
            (String)null, (String)null, (Integer)null, (TimeZone)null )
```