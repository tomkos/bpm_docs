<!-- image -->

# Example: Including query properties in a query

```
query ( " DISTINCT TASK.TKIID, TASK\_TEMPL.NAME, TASK.STATE,  
                    PROCESS\_INSTANCE.NAME",
           " QUERY\_PROPERTY.NAME = 'customerID' AND " +  
           " QUERY\_PROPERTY.STRING\_VALUE = 'CID\_12345' AND " + 
           " QUERY\_PROPERTY.NAMESPACE = 
              'http://www.ibm.com/xmlns/prod/websphere/mqwf/bpel/' AND " +
           " TASK.KIND IN 
              ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) AND " +  
           " TASK.STATE = TASK.STATE.STATE\_READY ",
           (String)null, (String)null, (Integer)null, (TimeZone)null );
```

```
query ( " DISTINCT TASK.TKIID, TASK\_TEMPL.NAME, TASK.STATE,  
                    PROCESS\_INSTANCE.NAME",
           " QUERY\_PROPERTY1.NAME = 'customerID' AND " +  
           " QUERY\_PROPERTY1.STRING\_VALUE = 'CID\_12345' AND " + 
           " QUERY\_PROPERTY1.NAMESPACE = 
                   'http://www.ibm.com/xmlns/prod/websphere/mqwf/bpel/' AND " +
           " QUERY\_PROPERTY2.NAME = 'Priority' AND " +  
           " QUERY\_PROPERTY2.NAMESPACE = 
                   'http://www.ibm.com/xmlns/prod/websphere/mqwf/bpel/' AND " +
           " TASK.KIND IN 
              ( TASK.KIND.KIND\_HUMAN, TASK.KIND.KIND\_PARTICIPATING ) AND " +  
           " TASK.STATE = TASK.STATE.STATE\_READY ",
           (String)null, (String)null, (Integer)null, (TimeZone)null );
```