<!-- image -->

# Example: Querying escalations

```
query( "DISTINCT ESCALATION.ESIID, ESCALATION.TKIID", 
         "WORK\_ITEM.REASON = WORK\_ITEM.REASON.REASON\_ESCALATION\_RECEIVER",  
           (String)null, (String)null, (Integer)null, (TimeZone)null )
```

- A condition for access control is added to the where clause. This example
assumes that group work items are not enabled.
- Constants, such as TASK.STATE.STATE\_READY, are replaced
by their numeric values.
- A FROM clause and join conditions are added.

```
SELECT DISTINCT ESCALATION.ESIID, ESCALATION.TKIID
   FROM   ESCALATION ESC, WORK\_ITEM WI 
   WHERE  ESC.ESIID = WI.OBJECT\_ID
   AND    WI.REASON  = 10                                 
   AND  
  ( WI.OWNER\_ID = 'MaryJones' OR WI.OWNER\_ID = null AND  WI.EVERYBODY = true )
```